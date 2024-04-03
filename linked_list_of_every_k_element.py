'''
❓ PROMPT
Given a linked list and a target k, return a linked list containing every kth element.

Example(s)
head = 1 -> 3 -> 6 -> 2 -> 8 -> 9
everyKthNode(head, 3) == "6 -> 9"
'''

class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

six = Node(9)
fifth = Node(8, six)
fourth = Node(2, fifth)
third = Node(6, fourth)
second = Node(3, third)
head = Node(1, second)


def get_every_k_node(head, k):
    result = Node(-1)
    before_head = Node(-1, result)
    curr = head 
    counter = 0
    while curr:
        print('curr.value,', curr.value)
        counter += 1
        if counter == k:
            print(curr.value)
            result.next = Node(curr.value)
            result = result.next
            counter = 0
        curr = curr.next
    return before_head.next.next


def output_node(head):
    curr = head
    while curr:
        print(curr.value, end='->')
        curr = curr.next
    print('None')

print(output_node(get_every_k_node(head, 3)))

output_node(head)
