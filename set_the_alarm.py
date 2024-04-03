'''
❓ PROMPT
You're exhausted after a long day and heading to bed, but you still have to set the alarm clock on your phone. You already have one you set the day before, so all you have to do is update it.

To set your alarm, the hours and minutes are set independently, each by scrolling upwards or downwards. One shift changes an hour or minute value by one, up or down. The values are organized cyclically, which means that dragging 0 minutes downwards turns it into 59, and dragging 59 upwards turns it into 0 (similarly, 0 hours can become 23 in one shift and vice versa).

Given the time of the previous alarm and the new desired time, what is the minimum number of scroll moves to set the new time?

Example(s)
For setTime = "07:30" and timeToSet = "08:00", the output should be
minScrollToSet(oldTime, newTime) = 31.

Shifting hours upwards once will change the alarm to "08:30", and shifting minutes 30 times downwards will change it to "08:00".

minScrollToSet("7:30", "8:00") === 31
minScrollToSet("7:00", "6:31") === 30
minScrollToSet("7:00", "6:25") === 26
'''
def convert_time_str(arg):
    str_arr = arg.split(':')
    for idx in range(len(str_arr)):
        str_arr[idx] = int(str_arr[idx])
    return str_arr

def find_hour_count(arg, target):
    if arg == 0:
        return abs(target - 12)
    return abs(arg - target)

def find_min_count(arg,target):
    if arg == 0:
        return abs(target - 60)

    return abs(arg - target)

def minScrollToSet(old_time, new_time):
    old_int_arr = convert_time_str(old_time)
    new_int_arr = convert_time_str(new_time)
    min_count = find_min_count(old_int_arr[1], new_int_arr[1])
    hour_count = find_hour_count(old_int_arr[0], new_int_arr[0])
    return min_count + hour_count




oldTime = '7:30'
newTime = '8:00'
# print(minScrollToSet(oldTime, newTime)) # 31 
print(minScrollToSet("7:00", "6:31"))
# print(minScrollToSet("7:00", "6:25"))
