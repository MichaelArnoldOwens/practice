'''
You are given a series of inputs representing delivery events. Each event is represented by an array of length 3:

[1, 1591846068, 0]

- The first number is an order number
- The second number is the timestamp
- The third number is either 0 (representing a pickup) or 1 (representing a dropoff)

Given a series of events, return the total active time, calculated by the period of time where they have an active delivery (if they've dropped everything off, they are not considered active until they pick something up again).



EXAMPLE(S)
Input:
[1, 1591846068, 0] #ACTIVE TIME 1 START
[2, 1591846070, 0]
[2, 1591846071, 1]
[1, 1591846080, 1] #ACTIVE TIME 1 END
[3, 1591846090, 0] #ACTIVE TIME 2 START
[3, 1591846102, 1] #ACTIVE TIME 2 END

cart = 1
total_active_time = 1591846080 - 1591846068 + 1591846102 - 1591846090
start_work_time = 1591846090

Output: 24

(71-68)+(80-70)+(102-90)=3+10+12=25

1: 1591846068, 1591846071
2: 1591846070, 1591846080
3: 1591846090, 1591846102

[68, 71], [70, 80], [90, 102]
[68, 80], [90, 102]
12 + 12 = 24

FUNCTION SIGNATURE
function activeDeliveryTime(events) {
def activeDeliveryTime(events: [int]) -> int:
  if len(events) < 2:
    return 0

  orders = 0
  total_time = 0
  start_time first time in your input array
  loop through _, time, is_dropof in events:
    if pickup:
      if orders = 0
        update start_time
      increment orders
    else:
      if orders = 0
        update total_time with curr_time - start_time
      decrement orders
  return total_active_time

- Timestamps are not increasing
- A pickup is dropped off an incorrect number of times (0 or 2+ times)
- A dropoff occurs before a pickup, or the pickup does not exist
'''


# def activeDeliveryTime(events: [int]) -> int:
#   orders = 0
#   total_time = 0
#   start_time = None
#   last_timestamp = None
#   for _, curr_time, order_type in events:
#     if curr_time <= last_timestamp:
#       return -1
#     if order_type == 0:
#       if orders == 0:
#         start_time = curr_time
#       orders += 1
#     else:
#       orders -= 1
#       if orders == 0:
#         total_time += curr_time - start_time

#   return total_time

def activeDeliveryTime(events: [int]) -> int:
    orders = set()
    total_time = 0
    start_time = None
    last_timestamp = None
    for order_num, curr_time, order_type in events:
        print(order_num, curr_time, order_type, orders)
        if not last_timestamp:
            last_timestamp = curr_time
        if curr_time < last_timestamp:
            raise ValueError("data out of order")

        if order_type == 0:
            if len(orders) == 0:
                start_time = curr_time
            orders.add(order_num)
        else:
            if order_num not in orders:
                raise ValueError("missing pickup log")
            orders.remove(order_num)
            if len(orders) == 0:
                print(start_time)
                if not start_time:
                    raise ValueError("Order doesn't exist")
                total_time += curr_time - start_time
    if len(orders) != 0:
        raise ValueError("Not all orders picked up")

    return total_time


orders = [[1, 1591846068, 0], [2, 1591846070, 0], [2, 1591846071, 1], [1, 1591846080, 1], [3, 1591846090, 0],
          [3, 1591846102, 1]]
print(activeDeliveryTime(orders))

print(activeDeliveryTime([]) == 0)

print(activeDeliveryTime(
    [
        [1, 1591846068, 0],
        [1, 1591846072, 1]
    ]) == 4)

print(activeDeliveryTime(
    [
        [1, 1591846068, 0],
        [1, 1591846072, 1],
        [2, 1591846073, 0],
        [2, 1591846078, 1]
    ]) == 9)

print(activeDeliveryTime(
    [
        [1, 1591846068, 0],
        [2, 1591846070, 0],
        [1, 1591846072, 1],
        [2, 1591846078, 1]
    ]) == 10)

print(activeDeliveryTime(
    [
        [1, 1591846068, 0],
        [2, 1591846070, 0],
        [1, 1591846071, 1],
        [2, 1591846080, 0],
        [3, 1591846090, 0],
        [3, 1591846102, 1],
    ]) == 24)
print(activeDeliveryTime([[1, 1591846068, 0]]) == 0)
print(activeDeliveryTime([[1, 1591846072, 1]]) == 0)

'''
**Follow-up**
Now, let's say the input is not guaranteed to be valid. What are some ways that the input could be invalid?

- Timestamps are not increasing
- A pickup is dropped off an incorrect number of times (0 or 2+ times)
- A dropoff occurs before a pickup, or the pickup does not exist

For any pickups and dropoffs that are invalid, ignore them entirely. Add one restriction at a time and have their code test for that conditio

'''


def activeDeliveryTime(events: [int]) -> int
    active_jobs = 0
    total_time = 0
    start_time = None

    for delivery in events:
        if delivery[2] == 0:
            if active_jobs == 0:
                start_time = delivery[1]
            active_jobs += 1
        elif delivery[2] == 1:
            if active_jobs == 1:
                total_time += delivery[1] - start_time
            active_jobs -= 1

    return total_time


'''
function activeDeliveryTime(events) {
  const PICKUP = 0, DROPOFF = 1;
  let activeCount = 0;
  let totalTime = 0;
  let firstActiveTime = undefined;

  for (const [id, time, action] of events) {
    if (action === PICKUP) {
      if (activeCount === 0) {
        firstActiveTime = time;
      }
      activeCount++;
    } else if (action === DROPOFF) {
      // must be a drop off
      activeCount--;
      if (activeCount === 0) {
        totalTime += time - firstActiveTime;
        firstActiveTime = undefined;
      }

    }
  }

  return totalTime;
}
'''