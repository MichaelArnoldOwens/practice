import collections.abc
import unittest
from os.path import exists
import subprocess

"""
We are writing software to analyze logs for toll booths on a highway. This highway is a divided highway with limited access; the only way on to or off of the highway is through a toll booth.

There are three types of toll booths:
* ENTRY (E in the diagram) toll booths, where a car goes through a booth as it enters the highway.
* EXIT (X in the diagram) toll booths, where a car goes through a booth as it exits the highway.
* MAINROAD (M in the diagram), which have sensors that record a license plate as a car drives through at full speed.


        Entry Booth                      Exit Booth
            |                                |
            E                                X
           /                                  \
---<------------<---------M---------<-----------<---------<----
                                         (West-bound side)

===============================================================

                                         (East-bound side)
------>--------->---------M--------->--------->--------->------
           \                                    /
            X                                  E
            |                                  |
        Exit Booth                     Entry Booth

For our first task:
1-1) Read through and understand the code and comments below. Feel free to run the code and tests.
1-2) The tests are not passing due to a bug in the code. Make the necessary changes to LogEntry to fix the bug.
"""


class LogEntry:
    """
    Represents an entry from a single log line.

    Log lines look like this in the file:

    34400.409 SXY288 210E ENTRY # string here

    Where:
    * 34400.409 is the timestamp in seconds since the software was started.
    * SXY288 is the license plate of the vehicle passing through the toll booth.
    * 210E is the location and traffic direction of the toll booth. Here, the
        toll booth is at 210 kilometers from the start of the tollway, and the E
        indicates that the toll booth was on the east-bound traffic side.
        Tollbooths are placed every ten kilometers.
    * ENTRY indicates which type of toll booth the vehicle went through. This is
        one of "ENTRY", "EXIT", or "MAINROAD".
    """
    """
    We are interested in how many people are using the highway, and so we would like to count how many complete journeys are taken in the log file.

    A complete journey consists of:
    * A driver entering the highway through an ENTRY toll booth.
    * The driver passing through some number of MAINROAD toll booths (possibly 0).
    * The driver exiting the highway through an EXIT toll booth.

    For example, the following log lines represent a single complete journey:

    90750.191 JOX304 250E ENTRY
    91081.684 JOX304 260E MAINROAD
    91483.251 JOX304 270E MAINROAD
    91874.493 JOX304 280E EXIT

    You may assume that the log only contains complete journeys, and there are no missing entries.

    2-1) Write a function in LogFile named count_journeys() that returns how many
        complete journeys there are in the given LogFile.
    """
    """
    We would like to catch people who are driving at unsafe speeds on the highway. To help us do that, we would like to identify journeys where a driver does either of the following:
    * Drive an average of 130 km/h or greater in any individual 10km segment of tollway.
    * Drive an average of 120 km/h or greater in any two 10km segments of tollway.

    For example, consider the following journey:
    1000.000 TST002 270W ENTRY
    1275.000 TST002 260W EXIT

    In this case, the driver of TST002 drove 10 km in 275 seconds. We can calculate
    that this driver drove an average speed of ~130.91km/hr over this segment:

    10 km * 3600 sec/hr
    ------------------- = 130.91 km/hr
        275 sec

    Note that:
    * A license plate may have multiple journeys in one file, and if they drive at unsafe speeds in both journeys, both should be counted.
    * We do not mark speeding if they are not on the highway (i.e. for any driving between an EXIT and ENTRY event).
    *!! Speeding is only marked once per journey. For example, if there are 4 segments 120km/h or greater, or multiple segments 130km/h or greater, the journey is only counted once.

    3-1) Write a function catch_speeders in LogFile that returns a collection of license plates that drove at unsafe speeds during a journey in the LogFile.
        If the same license plate drives at unsafe speeds during two different journeys, the license plate should appear twice (once for each journey they drove at unsafe speeds).

* Drive an average of 130 km/h or greater in any individual 10km segment of tollway.
we keep track 
* Drive an average of 120 km/h or greater in any two 10km segments of tollway.
- journey of the car
- isSpeeding # only add it once for one journey
- is > 120 kmh - if this is true and this condition is satisfied again, then we set isSpeeding for the journey



calculate_speed(distance, start, end) => speed


use license_plates_en_route set() to keep track of if they're on a trip or not
iterate through the logs
    calculate speed for currEntry and prevEntry:
        if not isSpeeding and >= 130, 
            set isSpeeding = true, 
            append to result list
        if not isSpeeding and >= 120,
            if is120:
                isSpeeding = true
                append to the result list
            else:
                is120 = true












"""

    def __init__(self, log_line):  # '34400.409 SXY288 210E ENTRY'
        tokens = log_line.split(" ")  # ['34400.409', 'SXY288', '210E', 'ENTRY']
        self.timestamp = float(tokens[0])  # '34400.409'
        self.license_plate = tokens[1]  # 'SXY288'
        self.booth_type = tokens[3]  # 'ENTRY'
        self.location = int(tokens[2][:-1])  # 210
        direction_letter = tokens[2][-1]  # 'E'
        if direction_letter == "E":  # only supports E/W
            self.direction = "EAST"  # setting direction
        elif direction_letter == "W":
            self.direction = "WEST"
        else:
            raise ValueError

    def __str__(self):
        return "<LogEntry timestamp: %f  license: %s  location: %d  direction: %s  booth type: %s>" % (
            self.timestamp, self.license_plate, self.location, self.direction, self.booth_type)


class LogFile(collections.abc.Sequence):
    """
    Represents a file containing a number of log lines, converted to LogEntry objects.
    """

    def __init__(self, file_handle):
        self.log_entries = []  # "44776.619 KTB918 310E MAINROAD"
        self.license_plates_en_route = set()
        self.completed_journeys_counter = 0
        for line in file_handle:  # this is probably the problem
            log_entry = LogEntry(line.strip())
            self.log_entries.append(log_entry)
            # ['4','4','7',...]

    def __getitem__(self, index):
        return self.log_entries[index]

    def __len__(self):
        return len(self.log_entries)

    def count_journeys(self):
        for entry in self.log_entries:
            license_plate = entry.license_plate
            booth_type = entry.booth_type
            if license_plate in self.license_plates_en_route and booth_type == 'EXIT':
                self.license_plates_en_route.remove(license_plate)
                self.completed_journeys_counter += 1
            else:
                self.license_plates_en_route.add(license_plate)
        return self.completed_journeys_counter

    #     calculate_speed(distance, start, end) => speed

    # use license_plates_en_route set() to keep track of if they're on a trip or not
    # iterate through the logs
    #     calculate speed for currEntry and prevEntry:
    #         if not isSpeeding and >= 130,
    #             set isSpeeding = true,
    #             append to result list
    #         if not isSpeeding and >= 120,
    #             if is120:
    #                 isSpeeding = true
    #                 append to the result list
    #             else:
    #                 is120 = true
    def calculate_speed(self, distance, starttime, endtime):
        return distance * 3600 / (endtime - starttime)

    def catch_speeders(self):
        isSpeeding = False
        is120 = False
        result = {}
        for index in range(1, len(self.log_entries)):
            prev = self.log_entries[index - 1]
            curr = self.log_entries[index]
            # license_plate = curr.license
            license_plate = curr.license_plate
            # curr_booth_type = curr.booth_type
            # curr_location = curr.location
            speed = self.calculate_speed(curr.location - prev.location, prev.timestamp, curr.timestamp)
            if not isSpeeding and speed >= 130:
                isSpeeding = True
                if license_plate in result:
                    result[license_plate] += 1
                else:
                    result[license_plate] = 1
            if not isSpeeding and not is120 and speed >= 120:
                if is120:
                    isSpeeding = True
                    if license_plate in result:
                        result[license_plate] += 1
                    else:
                        result[licencse_plate] = 1
                else:
                    is120 = True
        return result


class TestSuite(unittest.TestCase):
    # These tests are not meant to be exhaustive, and primarily show usage.
    def test_log_file(self):
        with open("/content/test/tollbooth_small.log") as fh:
            log_file = LogFile(fh)
        self.assertEqual(len(log_file), 13)
        for entry in log_file:
            self.assertTrue(type(entry) == LogEntry)

    def test_log_entry(self):
        log_line = "44776.619 KTB918 310E MAINROAD"
        log_entry = LogEntry(log_line)
        # print('$%$$$$$$$$$$$$$$$$$$$$$$$$$log_entry.timestamp:', log_entry.timestamp)
        self.assertEqual(log_entry.timestamp, 44776.619)  # issue here
        self.assertEqual(log_entry.license_plate, "KTB918")
        self.assertEqual(log_entry.location, 310)
        self.assertEqual(log_entry.direction, "EAST")
        self.assertEqual(log_entry.booth_type, "MAINROAD")
        log_line = "52160.132 ABC123 400W ENTRY"
        log_entry = LogEntry(log_line)
        self.assertEqual(log_entry.timestamp, 52160.132)
        self.assertEqual(log_entry.license_plate, "ABC123")
        self.assertEqual(log_entry.location, 400)
        self.assertEqual(log_entry.direction, "WEST")
        self.assertEqual(log_entry.booth_type, "ENTRY")

    def test_count_journeys(self):
        with open("/content/test/tollbooth_small.log") as fh:
            log_file = LogFile(fh)
        self.assertEqual(3, log_file.count_journeys())
        with open("/content/test/tollbooth_medium.log") as fh:
            log_file = LogFile(fh)
        self.assertEqual(63, log_file.count_journeys())

    def test_catch_speeders(self):
        with open("/content/test/tollbooth_speeders.log") as fh:
            log_file = LogFile(fh)
        ticket_list = log_file.catch_speeders()
        # ticket_list should be a list similar to
        # ["TST002", "TST003", "TST003"]
        # In this case, TST002 had one journey with unsafe driving, and
        # TST003 had two journeys with unsafe driving. The license plates
        # may be in any order.
        ticket_counts = collections.Counter(ticket_list)
        self.assertEqual(1, ticket_counts["TST002"])
        self.assertEqual(2, ticket_counts["TST003"])
        self.assertEqual(2, len(ticket_counts))
        with open("/content/test/tollbooth_medium.log") as fh:
            log_file = LogFile(fh)
        ticket_list = log_file.catch_speeders()
        self.assertEqual(10, len(ticket_list))
        with open("/content/test/tollbooth_long.log") as fh:
            log_file = LogFile(fh)
        ticket_list = log_file.catch_speeders()
        self.assertEqual(129, len(ticket_list))


if __name__ == "__main__":
    unittest.main()

# log_line = "44776.619 KTB918 310E MAINROAD"
# for line in log_line:
#      print('line:', line)