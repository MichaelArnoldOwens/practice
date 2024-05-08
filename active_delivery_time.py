'''
You are given a series of inputs representing delivery events. Each event is represented by an array of length 3:

[1, 1591846068, 0]

- The first number is an order number
- The second number is the timestamp
- The third number is either 0 (representing a pickup) or 1 (representing a dropoff)

Given a series of events, return the total active time, calculated by the period of time where they have an active delivery (if they've dropped everything off, they are not considered active until they pick something up again).

 

EXAMPLE(S)
Input:
[1, 1591846068, 0] 
[2, 1591846070, 0]
[1, 1591846071, 1] 
[2, 1591846080, 1] 
[3, 1591846090, 0] 
[3, 1591846102, 1]

Output: 24
 

FUNCTION SIGNATURE
function activeDeliveryTime(events) {
def activeDeliveryTime(events: [int]) -> int:
'''

def activeDeliveryTime(events: [int]) -> int:
    active = set()
    order_time_dict = {}
    for event in events:
        [order_number, timestamp, inactive] = event
        print(order_number,timestamp,inactive)


events1 = [ [1, 1591846068, 0], 
[2, 1591846070, 0],
[21, 1591846071, 1],
[22, 1591846080, 1], 
[23, 1591846090, 0], 
[23, 1591846102, 1]
]

print(activeDeliveryTime(events1))
