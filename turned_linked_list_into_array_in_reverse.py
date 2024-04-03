'''
❓ PROMPT
Given a linked list, return an array with all the elements in reverse.

Example(s)
head = 1 -> 3 -> 5 -> 2
createArrayInReverse(head) == [2,5,3,1]
'''
class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

tail = Node(2)
third = Node(5, tail)
second = Node(3, third)
head = Node(1, second)

def createArrayInReverse(head):
    arr = []
    curr = head
    while curr:
        arr.insert(0, curr.value)
        curr = curr.next
    return arr


print(createArrayInReverse(head) == [2,5,3,1])
