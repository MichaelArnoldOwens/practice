'''
❓ PROMPT
Given a linked list of positive integers, count the elements with odd values from the list using a recursive approach.

Note that 0 is an even number.

Example(s)
head = 1 -> 1 -> 1 -> 1
countOdd(head) == 4

head = 1 -> 2 -> 3 -> 4
countOdd(head) == 2
'''
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def count_odd_ll(root):
    def helper(curr, count = 0):
        if not curr:
            return count
        if curr.value % 2 == 1:
            return helper(curr.next, count + 1)
        else:
            return helper(curr.next, count)
    return helper(root)

test1 = Node(1, Node(1, Node(1, Node(1))))
print(count_odd_ll(test1))

test1 = Node(1, Node(2, Node(3, Node(4))))
print(count_odd_ll(test1))
print(count_odd_ll(test1))

