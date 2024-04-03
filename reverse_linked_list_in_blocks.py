'''
❓ PROMPT
Given a linked list and a positive number, *k*, reverse *k* items in the list at a time and reverse the remaining fragment if any.

Example(s)
head = 1 -> 2 -> 3
reverseBlocks(head, 2) == "2 -> 1 -> 3"

head = 1 -> 2 -> 3 -> 4 -> 5 -> 6
reverseBlocks(head, 3) == "3 -> 2 -> 1 -> 6 -> 5 -> 4"
'''
class Node:
  def __init__(self,val, next=None):
    self.value = val
    self.next = next

tail = Node(3)
second = Node(2, tail)
head = Node(1, second)

def print_ll(head):
  curr = head
  while curr:
    print(curr.value, end=', ')
    curr = curr.next

def build_ll_from_list(arr):
  result = Node(-1)
  curr = result
  for i in arr:
    new_node = Node(i)
    curr.next = new_node
    curr = curr.next

  print_ll(result.next)
  print('\n')
  print(result.next.value)
  print(result.next.next.value)
  print(result.next.next.next.value)
  print(result.next.next.next.next.value)
  print(result.next.next.next.next.next.value)
  print(result.next.next.next.next.next.next.value)
  
  return result.next


def reverseBlocks(head, k):
  curr = head
  buffer = []
  counter = 0
  while curr:
    segment = []
    while curr and counter < k:
      segment.insert(0, curr.value)
      counter += 1
      curr = curr.next
    buffer += segment
    counter = 0
  print(buffer)
  build_ll_from_list(buffer)

      






# reverseBlocks(head, 2) == "2 -> 1 -> 3"

tail = Node(6)
second = Node(5, tail)
third = Node(4, second)
fourth = Node(3, third)
fifth = Node(2, fourth)
head = Node(1, fifth)

reverseBlocks(head, 3)
