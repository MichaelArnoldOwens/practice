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
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

tail1 = Node(3)
second1 = Node(2, tail1)
head1 = Node(1, second1)

def create_ll_from_list(arr):
    print(arr)
    if len(arr) == 0:
        return None
    result = Node(arr[0])
    curr = result
    for i in range(1, len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next
    return result


def print_ll(head):
    while head:
        print(f'{head.val}, ', end='')
        head = head.next

def reverseBlocks(head, k):
    counter = 0
    curr = head
    arr = []
    block = []
    while curr:
        if counter == k:
            block.reverse()
            arr += block
            block = []
            counter = 0
        else:
            block.append(curr.val)
            curr = curr.next
            counter += 1
    block.reverse()
    arr += block
    return create_ll_from_list(arr)

# print_ll(reverseBlocks(head1, 2))
#
# tail = Node(6)
# fifth = Node(5, tail)
# fourth = Node(4, fifth)
# third = Node(3, fourth)
# second = Node(2, third)
# head = Node(1, second)
#
# print_ll(reverseBlocks(head, 3))


def toString(head: Node) -> None:
  if not head:
    return "<empty>"

  parts = []
  while head:
    parts.append(str(head.val))
    head = head.next

  return " -> ".join(parts)

print(toString(reverseBlocks(None, 1)) == "<empty>")

head = Node(1) # 1
print(toString(reverseBlocks(head, 1)) == "1")

head = Node(1) # 1
print(toString(reverseBlocks(head, 9)) == "1")

# 1 -> 2 -> 3
head = Node(1, Node(2, Node(3)))
print(toString(reverseBlocks(head, 1)) == "1 -> 2 -> 3")

# 1 -> 2 -> 3
head = Node(1, Node(2, Node(3)))
print(toString(reverseBlocks(head, 2)) == "2 -> 1 -> 3")

# 1 -> 2 -> 3 -> 4 -> 5 -> 6
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print(toString(reverseBlocks(head, 3)) == "3 -> 2 -> 1 -> 6 -> 5 -> 4")

# 5 -> 6 -> 9
head = Node(5, Node(6, Node(9)))
print(toString(reverseBlocks(head, 3)) == "9 -> 6 -> 5")

# 2 -> 2 -> 2
head = Node(2, Node(2, Node(2)))
print(toString(reverseBlocks(head, 2)) == "2 -> 2 -> 2")

# 1 -> 2 -> 3 -> 4 -> 5 -> 6
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print(toString(reverseBlocks(head, 2)) == "2 -> 1 -> 4 -> 3 -> 6 -> 5")

# 1 -> 2 -> 3 -> 4 -> 5 -> 6
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print(toString(reverseBlocks(head, 4)) == "4 -> 3 -> 2 -> 1 -> 6 -> 5")

# 1 -> 2 -> 3 -> 4 -> 5 -> 6
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print(toString(reverseBlocks(head, 5)) == "5 -> 4 -> 3 -> 2 -> 1 -> 6")

# 1 -> 2 -> 3 -> 4 -> 5 -> 6
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print(toString(reverseBlocks(head, 5)) == "5 -> 4 -> 3 -> 2 -> 1 -> 6")

# 1 -> 2 -> 3 -> 4 -> 5 -> 6
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print(toString(reverseBlocks(head, 6)) == "6 -> 5 -> 4 -> 3 -> 2 -> 1")

# 1 -> 2 -> 3 -> 4 -> 5 -> 6
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print(toString(reverseBlocks(head, 9)) == "6 -> 5 -> 4 -> 3 -> 2 -> 1")