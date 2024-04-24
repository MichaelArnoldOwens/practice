'''
❓ PROMPT
Given a binary tree, find all nodes that have only one child. Return an array of node values representing each single-child parent in any order.

Example(s)
           1
       2       3
     _   4   _   _

should return [2]

           12
       3       4
    1    _   6   _

should return [3, 4]

           12
       3       4
    1    _   6   _
  9  _      _ _

should return [3, 1, 4]
'''
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def find_single_children_parents(root):
    result = []
    def helper(node):
        if not node:
            return
        if node.left and not node.right:
            result.append(node.value)
        if node.right and not node.left:
            result.append(node.value)

        helper(node.left)
        helper(node.right)
    helper(root)
    return result

test1 = Node(1, Node(2, None, Node(4)), Node(3))
print(find_single_children_parents(test1))

test2 = Node(12, Node(3, Node(1)),Node(4,Node(6)))
print(find_single_children_parents(test2))

test3 = Node(12, Node(3, Node(1, Node(9))),Node(4,Node(6)))
print(find_single_children_parents(test3))

hasSingleChildren = find_single_children_parents
#   1
# 2
root = Node(1,
            Node(2))
print(set(hasSingleChildren(root)) == set([1]))

#   1
# 2   3
root = Node(1,
            Node(2),
            Node(3))
print(hasSingleChildren(root) == [])

#     1
#  2     3
# _ 4   _ _
root = Node(1,
            Node(2,
                 None,
                 Node(4)),
            Node(3))
print(set(hasSingleChildren(root)) == set([2]))

#     12
#  3     4
# 1 _   6 _
root = Node(12,
            Node(3,
                 Node(1)),
            Node(4,
                 Node(6)))
print(set(hasSingleChildren(root)) == set([3,4]))

#     12
#   3     4
#  1 _   6  _
# 9 _   _ _
root.left.left.left = Node(9)
print(set(hasSingleChildren(root)) == set([3,1,4]))
