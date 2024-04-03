'''
Coding Drills: Recursion on Linked Lists

1. Given a linked list and an integer, find whether the integer exists in the linked list. Return a boolean.

2. Given a linked list and an integer, return how many times the integer exists in the list.

3. Find mean of a linked list of integers
4. Replace all negative values with a 0

5. Reverse the linked list
'''
# 1
def find(ll, target):
    if not ll:
        return False
    if ll.value == target:
        return True
    return find(ll.next, target)

# 2
def count(ll):
    if not ll:
        return 0
    return 1 + count(ll.next)

#3
def mean(ll, counter = 0, sum = 0):
   if not ll:
       return sum / counter
   return mean(ll.next, counter + 1, sum + ll.value)

# 4
def replace_negatives(ll):
    if not ll:
        return
    if ll.value < 0:
        ll.value = 0
    return replace_negatives(ll.next)

def reverse(ll):
    if not ll.next:
        return ll
    next = ll.next

