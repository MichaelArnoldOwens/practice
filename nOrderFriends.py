def nOrderFriends(name, n, friends):
    if n <= 0:
        return  # precondition

    queue = [name]
    nextLevelFriends = set()
    for _ in range(n):  # repetitive iteration to generate next order friends
        nextLevelFriends = set()  # reset each iteration
        while len(queue) > 0:
            nextFriendsFriendsToAdd = queue.pop(0)
            nextLevelFriends = nextLevelFriends.union(set(friends.get(nextFriendsFriendsToAdd, [])))
        queue = list(nextLevelFriends)

    return queue


def getOrderBetween(name1, name2, friends):
    # usage of helper function
    orderNum = 1
    while orderNum <= 6:  # upper limit based on "six degrees of separation"
        friend1OrderFriends = nOrderFriends(name1, orderNum, friends)
        friend2OrderFriends = nOrderFriends(name2, orderNum, friends)

        if name1 in friend2OrderFriends or name2 in friend1OrderFriends:
            return orderNum
        orderNum += 1

    return "more than 6 degrees of separation"


def getOrderBetweenOptimized(name1, name2, friends):
    # optimized to integrate with nOrderFriends code; prevents excessive generation of smaller n values
    orderNum = 1

    queue1 = [name1]
    queue2 = [name2]
    nextLevelFriends1 = set()
    nextLevelFriends2 = set()
    for orderNum in range(1, 7):
        while len(queue1) > 0:
            # generate friend 1's next level friends
            nextFriend1sFriendsToAdd = queue1.pop()
            nextLevelFriends1 = nextLevelFriends1.union(set(friends.get(nextFriend1sFriendsToAdd, [])))

        while len(queue2) > 0:
            # generate friend 2's next level friends
            nextFriend2sFriendsToAdd = queue2.pop()
            nextLevelFriends2 = nextLevelFriends2.union(set(friends.get(nextFriend2sFriendsToAdd, [])))

        if name1 in nextLevelFriends2 or name2 in nextLevelFriends1:
            # O(1) search
            return orderNum

        queue1 = nextLevelFriends1
        queue2 = nextLevelFriends2

    return "more than 6 degrees of separation"