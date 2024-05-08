'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed).

Input: 1->2->3->4
Output: 2->1->4->3

Input: 1->2->3
Output: 2->1->3
 

FUNCTION SIGNATURE
def swapPairs(self, head: ListNode) -> ListNode:

Follow-up:
Another way of stating the initial problem would be to reverse sub-lists of length 2. Write a new version of the function that takes a second parameter, k. For k = 2, the result is just like the original function: adjacent pairs are swapped. But for larger values of k, the function should now reverse longer sub-lists, again modifying the pointers to rethread the list in the new order. As an example, for a list [sentinel -> 1 -> 2 -> 3 -> 4 -> 5] we get the following results for different values of k:


https://leetcode.com/problems/reverse-nodes-in-k-group/description/
'''

def toString(head):
    result = ''
    while head:
        result += str(head.value) + '->'
        head = head.next
    return result

class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def swap(h1, h2, prev=None):
    if not h2:
        return h1
    temp = h2.next
    h1.next = temp
    h2.next = h1
    if prev:
        prev.next = h2
    return h1

def swapPairs(head: ListNode, target) -> ListNode:
    if not head:
        return head
    sentinel = ListNode(-1, head)
    prev = sentinel
    left = head
    right = head
    counter = target
    while right:
        while right and counter > 0:
            counter = counter - 1 
            right = right.next
            counter = target
        prev = swap(left, right, prev)
        right = prev.next
        left = right
    return sentinel.next

head1 = ListNode(1, ListNode(2, ListNode(3)))
print(toString(head1))
print(toString(swapPairs(head1, 2)))
