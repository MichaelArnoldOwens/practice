'''
Given a binary search tree and a target value, return the in-order successor.
 

EXAMPLE(S)
    5 <--- root
 2     8
1 4   6 9

inOrderSuccessor(root, 1) = 2
inOrderSuccessor(root, 2) = 4
inOrderSuccessor(root, 4) = 5
inOrderSuccessor(root, 5) = 6
inOrderSuccessor(root, 6) = 8
inOrderSuccessor(root, 8) = 9
inOrderSuccessor(root, 9) = null
 

FUNCTION SIGNATURE
function inOrderSuccessor(root, target) {
def inOrderSuccessor(root: Node, target: int, successor=None) -> Node:
'''

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

test1 = Node(5, Node(2, Node(1), Node(4)), Node(8, Node(6), Node(9)))

def inOrderSuccessor(root, target):
    successor = None
    curr = root

    while curr:
        if curr.value <= target:
            curr = curr.right
        elif curr.value > target:
            successor = curr
            curr = curr.left
    return successor




print(inOrderSuccessor(test1, 1).value)
# runtime O(logn) , space O(1) in a balanced bst


def inOrderSuccessorRecursive(root, target):
    def helper(curr, successor = None):
        nonlocal target
        if not curr:
            return successor
        if curr.value <= target:
            return helper(curr.right, successor)
        else:
            return helper(curr.left, curr)
    return helper(root)

print(inOrderSuccessorRecursive(test1, 1).value)

