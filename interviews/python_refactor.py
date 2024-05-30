"""

Note that this example WILL NOT RUN in CoderPad, since it does not provide a Django environment in which to run. This is an extracted sample from production (at one point).

"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from django import db
from django.db.models import Q
from django.utils import timezone
from hyke.api.models import EmailView
from hyke.automation.jobs import nps_calculator_onboarding, nps_calculator_running
from hyke.email.jobs import send_transactional_email
from hyke.fms.jobs import create_dropbox_folders
from hyke.scheduled.base import next_annualreport_reminder
from hyke.scheduled.service.nps_surveys import schedule_next_running_survey_sequence, schedule_onboarding_survey_sequence, send_client_onboarding_survey
from structlog import get_logger

logger = get_logger(__name__)

class ProgressStatus(models.Model):
    PENDING = "pending"
    COMPLETED = "completed"
    email = models.CharField(max_length=100, default="---")
    llcformationstatus = models.CharField(max_length=50, default="---")
    postformationstatus = models.CharField(max_length=50, default="---")
    einstatus = models.CharField(max_length=50, default="---")
    businesslicensestatus = models.CharField(max_length=50, default="---")
    bankaccountstatus = models.CharField(max_length=50, default="---")
    contributionstatus = models.CharField(max_length=50, default="---")
    SOIstatus = models.CharField(max_length=50, default="---")
    FTBstatus = models.CharField(max_length=50, default="---")
    questionnairestatus = models.CharField(max_length=50, default="---")
    bookkeepingsetupstatus = models.CharField(max_length=50, default="---")
    taxsetupstatus = models.CharField(max_length=50, default="---")
    clientsurveystatus = models.CharField(max_length=50, default="---")
    bk_services_setup_status = models.CharField(max_length=50, choices=[(PENDING, PENDING), (COMPLETED, COMPLETED)], default=PENDING)

    class Meta:
        verbose_name = "ProgressStatus"
        verbose_name_plural = "ProgressStatuses"

    def __str__(self):
        return "%s - %s" % (self.id, self.email)

class StatusEngine(models.Model):
    FAILED = -4
    SECOND_RETRY = -3
    FIRST_RETRY = -2
    SCHEDULED = -1
    COMPLETED = 1
    UNNECESSARY = 4
    OFFBOARDED = 5
    OUTCOMES = [
        (SCHEDULED, "Scheduled"),
        (COMPLETED, "Completed"),
        (UNNECESSARY, "Cancelled due to Completed Task"),
        (OFFBOARDED, "Cancelled due to Offboarding"),
        (FIRST_RETRY, "Retrying previously failed"),
        (SECOND_RETRY, "Retrying previously failed again"),
        (FAILED, "Gave up retrying due to multiple failures"),
    ]
    email = models.CharField(max_length=50, blank=True)
    process = models.CharField(max_length=100)
    formationtype = models.CharField(max_length=20, default="---")
    processstate = models.IntegerField(default=1)
    outcome = models.IntegerField(choices=OUTCOMES, default=SCHEDULED)
    data = models.CharField(max_length=1000, default="---")
    created = models.DateTimeField(default=timezone.now)
    executed = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "StatusEngine"
        verbose_name_plural = "StatusEngines"

    def __str__(self):
        return "%s - %s - %s" % (self.id, self.email, self.process)

def update_progress_status(progress_status, statuses, keys):
    if len(statuses) != len(keys):
        raise ValueError('There must be a status for every key')
    for i in range(len(statuses)):
        key = keys[i]
        status = statuses[i]
        progress_status[key] = status
    progress_status.save()

def handle_client_onboarding_survey(item):
    if item.processstate == 1:
        try:
            send_client_onboarding_survey(email=item.email)
        except Exception as e:
            logger.exception(f"Can't process Onboarding NPS Survey for status engine id={item.id}")

def handle_payment_error_email(item):
    if item.processstate == 1:
        send_transactional_email(email=item.email, template="[Action required] - Please update your payment information")
        print("[Action required] - Please update your payment information email is sent to " + item.email)

def handle_running_flow(item):
    email = item.email
    if item.processstate == 1:
        progress_status = ProgressStatus.objects.get(email=email)
        update_progress_status(progress_status=progress_status, statuses=['completed', 'completed2'], keys=['bookkeepingsetupstatus', 'taxsetupstatus'])
        StatusEngine.objects.get_or_create(
            email=email,
            process="Schedule Email",
            formationtype="Hyke Daily",
            processstate=1,
            outcome=StatusEngine.SCHEDULED,
            data="What's upcoming with Collective?",
            defaults={"executed": timezone.now() + relativedelta(days=1)},
        )
        StatusEngine.objects.get_or_create(
            email=email,
            process="Running flow",
            formationtype="Hyke System",
            processstate=2,
            defaults={"outcome": StatusEngine.SCHEDULED, "data": "---"},
        )
        schedule_onboarding_survey_sequence(email=email)
        schedule_next_running_survey_sequence(email=email)
        create_dropbox_folders(email=email)
        print("Dropbox folders are created for " + email)
        has_run_before = StatusEngine.objects.filter(
            email=email, process=item.process, processstate=item.processstate, outcome=StatusEngine.COMPLETED,
        ).exists()
        if has_run_before:
            print(
                "Not creating form w9 or emailing pops because dropbox folders job has already run for {}".format(
                    email
                )
            )
    elif item.processstate == 2:
        EVs = EmailView.objects.filter(type="annual", legacy=True)
        for ev in EVs:
            templatedate = ev.date.split("-")
            emaildate = datetime.now()
            emaildate = emaildate.replace(month=int(templatedate[0]), day=int(templatedate[1]))
            emaildate = emaildate.replace(hour=23, minute=59, second=59)
            se = StatusEngine(
                email=email,
                process="Reminder",
                formationtype="Hyke System",
                processstate=1,
                outcome=StatusEngine.SCHEDULED,
                data=ev.title,
                executed=emaildate,
            )
            se.save()

def handle_annual_report_uploaded(item):
    reportdetails = item.data.split("---")
    reportname = reportdetails[1].strip()
    reportyear = reportdetails[0].strip()
    reportstate = reportdetails[2].strip() if len(reportdetails) == 3 else None
    data_filter = Q(data=f"{reportyear} --- {reportname}")
    if reportstate:
        data_filter |= Q(data=f"{reportyear} --- {reportname} --- {reportstate}")
    SEs = StatusEngine.objects.filter(email=item.email, process="Annual Report Reminder", outcome=-1).filter(data_filter)
    for se in SEs:
        se.outcome = StatusEngine.COMPLETED
        se.executed = timezone.now()
        se.save()
    item.outcome = StatusEngine.COMPLETED
    item.executed = timezone.now()
    item.save()
    next_annualreport_reminder(item.email, reportname, reportstate)

def handle_calc_nps_running(item):
    nps_calculator_running()
    print("Running NPS is calculated for " + item.data)

def handle_calc_nps_onboarding(item):
    nps_calculator_onboarding()
    print("Onboarding NPS is calculated for " + item.data)

def handle_kickoff_generic(item, status):
    if item.processstate == 1:
        progress_status = ProgressStatus.objects.filter(email__iexact=item.email).first()
        if progress_status:
            update_progress_status(progress_status=progress_status, statuses=[status], keys=['questionnairestatus'])
            StatusEngine.objects.create(
                email=item.email,
                processstate=1,
                formationtype="Hyke Salesforce",
                outcome=StatusEngine.SCHEDULED,
                process=item.process,
                data=item.data,
            )

def handle_kickoff_questionnaire_completed(item):
    handle_kickoff_generic(item=item, status='scheduled')

def handle_kickoff_call_scheduled(item):
    handle_kickoff_generic(item=item, status='scheduled')

def handle_kickoff_call_cancelled(item):
    handle_kickoff_generic(item=item, status='rescheduled')

def handle_transition_plan_submitted(item):
    if item.processstate == 1:
        email = item.email
        progress_status = ProgressStatus.objects.get(email__iexact=email)
        update_progress_status(progress_status=progress_status, statuses=['submitted'], keys=['questionnairestatus'])
        StatusEngine.objects.create(
            email=email,
            process="Transition Plan Submitted",
            formationtype="Hyke Salesforce",
            processstate=1,
            outcome=StatusEngine.SCHEDULED,
            data="---",
        )
        StatusEngine.objects.get_or_create(
            email=email,
            process="Schedule Email",
            formationtype="Hyke Daily",
            processstate=1,
            outcome=StatusEngine.SCHEDULED,
            data="Welcome to the Collective community!",
            defaults={"executed": timezone.now() + relativedelta(days=1)},
        )

def handle_bk_training_call_scheduled(item):
    if item.processstate == 1:
        StatusEngine.objects.create(
            email=item.email,
            processstate=1,
            formationtype="Hyke Salesforce",
            outcome=StatusEngine.SCHEDULED,
            process="BK Training Call Scheduled",
            data=item.data,
        )

def handle_bk_training_call_cancelled(item):
    if item.processstate == 1:
        progress_status = ProgressStatus.objects.get(email__iexact=item.email)
        update_progress_status(progress_status=progress_status, statuses=['reschedule'], keys=['bookkeepingsetupstatus'])
        status_engine = StatusEngine(
            email=item.email,
            process="Followup - BK Training",
            formationtype="Hyke Daily",
            processstate=1,
            outcome=StatusEngine.SCHEDULED,
            data="---",
            executed=timezone.now() + relativedelta(days=2),
        )
        status_engine.save()
        StatusEngine.objects.create(
            email=item.email,
            processstate=1,
            formationtype="Hyke Salesforce",
            outcome=StatusEngine.SCHEDULED,
            process="BK Training Call Cancelled",
        )

def handle_bank_connect(item):
    email = item.email
    if item.processstate == 1:
        send_transactional_email(
            email=email,
            template="SP.ONB.0021 - Account is created before, bank is connected later",
        )
        print("SP.ONB.0021 - Account is created before, bank is connected later email is sent to " + email)
        item.outcome = StatusEngine.COMPLETED
        item.executed = timezone.now()
        item.save()
    elif item.processstate == 2:
        send_transactional_email(
            email=email,
            template="SP.ONB.0010 - Account is created",
        )
        print("SP.ONB.0010 - Account is created email is being sent to " + email)
        item.outcome = StatusEngine.COMPLETED
        item.executed = timezone.now()
        item.save()
    elif item.processstate == 3:
        if item.executed is None:
            connection_reference_time = item.created
        else:
            connection_reference_time = item.executed
        passed_seconds = (datetime.datetime.now(timezone.utc) - connection_reference_time).total_seconds()
        if passed_seconds < 259200:
            return
        print(str(int(passed_seconds)) + " seconds passed...")
        send_transactional_email(
            email=email,
            template="SP.BNK.0010 - Please connect your bank (remind every 3 days)",
        )
        print("SP.BNK.0010 - Please connect your bank (remind every 3 days) email is sent to " + email)
        item.outcome = StatusEngine.COMPLETED
        item.executed = timezone.now()
        item.save()

def scheduled_system():
    print("Scheduled task is started for Hyke System...")
    items = StatusEngine.objects.filter(Q(outcome=StatusEngine.SCHEDULED) & Q(formationtype__startswith="Hyke System"))
    print("Active items in the job: " + str(len(items)))
    db.close_old_connections()
    item_process_action = {
        'Client Onboarding Survey': handle_client_onboarding_survey,
        'Payment error email': handle_payment_error_email,
        'Running flow': handle_running_flow,
        'Annual Report Uploaded': handle_annual_report_uploaded,
        'Calculate NPS Running': handle_calc_nps_running,
        'Calculate NPS Onboarding': handle_calc_nps_onboarding,
        'Kickoff Questionnaire Completed': handle_kickoff_questionnaire_completed,
        'Kickoff Call Scheduled': handle_kickoff_call_scheduled,
        'Kickoff Call Cancelled': handle_kickoff_call_cancelled,
        'Transition Plan Submitted': handle_transition_plan_submitted,
        'BK Training Call Scheduled': handle_bk_training_call_scheduled,
        'BK Training Call Cancelled': handle_bk_training_call_cancelled,
        'Bank connect': handle_bank_connect
    }
    for item in items:
        if item.outcome == StatusEngine.SCHEDULED:
            action = item_process_action[item.process]
            if action:
                action(item)
            else:
                logger.exception(f'Missing handler for process {item.process}!')
    print("Scheduled task is completed for Hyke System...\n")

if __name__ == "__main__":
    scheduled_system()

