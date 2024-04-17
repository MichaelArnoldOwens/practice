# sum all elements in an array

def sum_all(arr):
    def helper(arr, i = 0, cumulator = 0):
        if i == len(arr):
            return cumulator
        cumulator += arr[i]
        return cumulator + helper(arr, i + 1) # tail recursion

    return helper(arr)


# print(sum_all([3,1,2,3,1]))

# check if a string is palindrome or not

def is_palindrome(s):

    def helper(s, right, left=0 ):
        if left > right:
            return True
        if s[left] != s[right]:
            return False
        return helper(s, right - 1, left + 1)
    return helper(s, len(s) - 1, 0)

# print(is_palindrome(('aba')))
# print(is_palindrome(('aab')))
# print(is_palindrome('abba'))
# print(is_palindrome('abaaba'))

# Time: 2^N - exponential - multi-path recursion
# Space: N - height of the tree - callstack space except when tail-recursion (O(1))
def fib(n):
    def helper(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return helper(n - 1) + helper(n - 2) # multi-path recursion
    return helper(n)

# print(fib(6))


# mock interview with Pengyu Victor Cheng

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
# frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# input: array of distinct ints(only positive) AND target int
# output: array of array of int

# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]] // [[2,3,2],[7]] is also valid
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:
# Input: candidates = [2], target = 1
# Output: []

'''
can have no output
not always sorted
2 -> all sets(2) -> sets(2, 2) => set(2,2, 3)


result = []
target_ = target
idx = 0 on candidates:
  target - candidates[idx] == 0? => append result [7]

7 - 2 = 5 - 3 = 2
7 - 2 = 5 - 2 = 3 -2
                3 - 3

5
7 - 3 = 4
7 - 6 = 1 -
7 - 7 = 0

feedback:
work on dry on
- use a tree structure to draw out
- dfs question
- leave some comment
'''


def get_all_combinations(arr, target):
    result = []

    def helper(arr, i=0, accumulator=[]):
        if sum(accumulator) == target:
            copy_accumulator = accumulator.copy()
            result.append(copy_accumulator)
            return
        if sum(accumulator) > target:  # 8
            return

        helper(arr, i, accumulator + [arr[i]])

        helper(arr, i + 1, accumulator + [arr[i]])

    helper(arr)
    return result


# print(get_all_combinations([2, 3, 6, 7], 7))

# Valid Ancestor group session

'''
Given a binary tree of numbers, and two numbers, A and B, determine if A is an ancestor of B.


EXAMPLE(S)
  3
1   2
A=3 and B=1 returns true
A=3 and B=2 returns true
A=2 and B=3 returns false

  3
1   2
   4 5
A=3 and B=5 returns true
A=2 and B=5 returns true
A=5 and B=2 returns false


FUNCTION SIGNATURE
function validAncestor(root, ancestor, descendent) {
def validAncestor(root: TreeNode, ancestor: int, descendent: int) -> bool:
'''
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
# this is actually find child
# def validAncestor(root, ancestor, descendent):
#     if not root:
#         return False
#     if root.value == ancestor:
#         if (root.left and descendent == root.left.value) or (root.right and descendent == root.right.value):
#             return True
#     return validAncestor(root.left, ancestor, descendent) or validAncestor(root.right, ancestor, descendent)


def validAncestor(root, ancestor, descendent):
    if ancestor == descendent:
        return False
    def findNode(root, target):
        if not root:
            return
        if root.value == target:
            return root
        return findNode(root.left, target) or findNode(root.right, target)
    a = findNode(root, ancestor)
    if not a:
        return False
    d = findNode(a, descendent)
    return bool(d)


# test = Node(3, Node(1), Node(2))
# print(validAncestor(test, 3, 1))
# print(validAncestor(test, 3, 2))
# print(validAncestor(test, 2, 3))

# test2 = Node(3, Node(1), Node(2, Node(4), Node(5)))
# print(validAncestor(test2, 3, 5))
# print(validAncestor(test2, 2, 5))
# print(validAncestor(test2, 5, 2))

'''
finding a path
    
findPath(root,B, list){

if (!root){
  return
}

list.push(root)
if(root.val==B){
    
  return
}

findPath(root.left, B, list)
findPath(root.right,B,list)
list.pop()

  }
'''



'''
We're going to build the data model for a text editor that supports the basic operations needed for typing. This data model will take the form of a class that has methods for:
- typing one character at a time (write)
- backspace and delete to remove text one character at a time (delete)
- moving the cursor (moveBack/moveStart/moveEnd/moveNext)

How can this class be designed so that the main operations are as efficient as possible?
 

EXAMPLE(S)
const editor = new TextEditor("Text").moveEnd();
console.log(editor.toString(), "Text");
editor.backspace();
console.log(editor.toString(), "Tex");
editor.addChar('t'). addChar(" ").addChar("E").addChar("d").addChar("i").addChar("t");
console.log(editor.toString(), "Text Edit");
editor.moveStart().delete().delete().delete().delete().delete();
console.log(editor.toString(), "Edit");

const e2 = new TextEditor("otter");
console.log(e2.toString(), "otter");
e2.backspace().backspace().backspace().backspace().backspace();
console.log(e2.toString() === "", true);
e2.addChar("a").moveBack().delete();
console.log(e2.toString() === "", true);
'''

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

#incomplete
class TextEditor:

    def __init__(self, initial_text=''):
        self.start = None # start and end should be sentinel nodes that point to the actual content instead of being references to the actual nodes
        self.end = None
        self.cursor = None
        prev = None
        for c in initial_text:
            new_node = Node(c)
            if not self.start:
                self.start = new_node
                self.cursor = new_node
            else:
                new_node.prev = prev
                prev.next = new_node
                prev = new_node
                self.end = new_node


        return self

    def add_char(self, c):
        new_node = Node(c, self.cursor.prev, self.cursor.next)
        self.cursor.next.prev = new_node
        self.cursor.next = new_node
        self.cursor = new_node
        return self

    def delete(self):
        if not self.cursor:
            return self
        prev = self.cursor.prev
        next = self.cursor.next
        new_end = True if self.cursor == self.end else False
        self.cursor.next = None
        self.cursor.prev = None
        prev.next = next
        next.prev = prev
        self.cursor = next
        if new_end:
            self.end = self.cursor
        return self

    def backspace(self):
        if not self.cursor:
            return self
        old_prev = self.cursor.prev
        old_prev.prev = None
        old_prev.next = None
        new_prev = self.cursor.prev.prev
        new_prev.next = self.cursor
        return self

    def move_back(self):
        if not self.cursor.prev:
            return self
        self.cursor = self.cursor.prev
        return self

    def move_next(self):
        if not self.cursor.next:
            return self
        self.cursor = self.cursor.next
        return self

    def move_start(self):
        self.cursor = self.start

    def move_end(self):
        self.cursor = self.end

    def to_string(self):
        curr = self.head
        result = ''
        while curr:
            result += curr.value
            curr = curr.next
        return result