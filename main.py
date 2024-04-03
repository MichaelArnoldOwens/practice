'''
❓ PROMPT
You will be implementing a function called stringify which will take in a Javascript Object and return the JSON representation of the object as a string. This function is actually built into Javascript as `JSON.stringify(object)` but you have to write yours from scratch!

You may want to take a moment to review the rules for [JSON syntax](https://www.w3schools.com/js/js_json_syntax.asp).

Example(s)
anObj = {"x": 5, "y": "Oliver"}
stringify(anObj)
Output: '{"x": 5, "y": "Oliver"}'

aList = [1, "hello", "null", {"x": 5, "y": "Oliver"}]
stringify(aList)
Output: '[1, "hello", "null", {"x": 5, "y": "Oliver"}]'

A brief note about the input and output. They look very similar, but the input is an object and the output is a string enclosed in single ticks. This means that the double quotes inside that string are characters in the string and are important.


🔎 EXPLORE
List your assumptions & discoveries:


Insightful & revealing test cases:


🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()


📆 PLAN
Outline of algorithm #:


🛠️ IMPLEMENT
function stringify(obj) {


🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def stringify(obj):
    result = ''
    if type(obj) == list:
        result += '['
        for i, val in enumerate(obj):
            if type(val) == str:
                if i == 0:
                    result += f'"{str}",'
                else:
                    result += f' "{str}",'
            if type(val) == dict:
                result += ' {'
                for key in val:
                    obj_val = val[key]
                    # value_string = obj_val if type(obj_val) is int or type(obj_val) is float else
                    result += f'"{key}": '




anObj = {"x": 5, "y": "Oliver"}
stringify(anObj)

aList = [1, "hello", "null", {"x": 5, "y": "Oliver"}]
stringify(aList)
"""
Given a string with nested parentheses, return the substring between the parentheses at the specified depth.

Input: "ab(c(def)gh)i", depth=1
Output: "c(def)gh"
Input: "ab(c(def)gh)i", depth=2
Output: "def"
The string is guaranteed to have balanced parentheses, i.e. every ( character has a corresponding ) character, and every level has at most 1 parenthesis nesting, i.e. (()()) will not occur.

If the depth is greater than the maximum parentheses depth in the string, return an empty string.
pass dictionary
keys = depths
values are list of characters
left to right
    increment depth if hitting (
    decrement depth if hitting )
    add characters between ()
ex
{
    0: ab -> abi
    1: c -> cgh
    2: def


"""

'''
Given a string with nested parentheses, return the substring between the parentheses at the specified depth.

Input: "ab(c(def)gh)i", depth=1
Output: "c(def)gh"
Input: "ab(c(def)gh)i", depth=2
Output: "def"
The string is guaranteed to have balanced parentheses, i.e. every ( character has a corresponding ) character, and every level has at most 1 parenthesis nesting, i.e. (()()) will not occur.

If the depth is greater than the maximum parentheses depth in the string, return an empty string.

 d (e(a b c) f) 
            ^

curr_depth
0
'''


# def solution(parenString, depth):
#     print('parenString:', parenString)
#     if depth == 0:
#         return parenString
#
#     def walk(i=0, curr_depth=0, start=0):
#
#         if i >= len(parenString):
#             return ""
#
#         if parenString[i] == '(':
#             new_depth = curr_depth + 1
#             if new_depth == depth:
#                 start = i + 1
#             return walk(i + 1, new_depth, start)
#         elif parenString[i] == ')':
#             if curr_depth - 1 < depth:
#                 return (parenString[start:i])
#             return walk(i + 1, curr_depth - 1, start)
#
#         else:
#             return walk(i + 1, curr_depth, start)
#
#     return walk()


# parenString= "def(abc)g"
# depth= 1
# print(solution(parenString, depth))

parenString2 = "ab(c(def)gh)i"
depth2 = 1
print(solution(parenString2, depth2))

# parenString2 = "ab(c(def)gh)i"
# depth2 = 2
# print(solution(parenString2, depth2))


# def solution(parenString, depth):
#     print('parenString:', parenString)
#
#     def walk(i=0, curr_depth=0, start=0):
#         print('i =', i)
#         if depth == 0:
#             return parenString
#         if i >= len(parenString):
#             return ""
#
#         print('char = ', parenString[i])
#         print('start = ', start)
#         print('curr_depth:', curr_depth, 'curr_depth == depth: ', curr_depth == depth)
#         if parenString[i] == '(':
#             start += 1
#             return walk(i + 1, curr_depth + 1, start)
#         elif parenString[i] == ')':
#             print('hitting )')
#             if curr_depth == depth:
#                 print(parenString[start:i])
#                 return parenString[start:i]
#             return walk(i + 1, curr_depth - 1, start)
#         else:
#             return walk(i + 1, curr_depth, start)
#
#     return walk()
# parenString= "def(abc)g"
# depth= 1
# print(solution(parenString, depth))


# def stringify(obj):
#
#
#
# anObj = {"x": 5, "y": "Oliver"}
# stringify(anObj)
# # Output: '{"x": 5, "y": "Oliver"}'
#
# aList = [1, "hello", "null", {"x": 5, "y": "Oliver"}]
# stringify(aList)
# # Output: '[1, "hello", "null", {"x": 5, "y": "Oliver"}]'
#


'''
❓ PROMPT
You will be implementing a function called stringify which will take in a Javascript Object and return the JSON representation of the object as a string. This function is actually built into Javascript as `JSON.stringify(object)` but you have to write yours from scratch!

You may want to take a moment to review the rules for [JSON syntax](https://www.w3schools.com/js/js_json_syntax.asp).

Example(s)
anObj = {"x": 5, "y": "Oliver"}
stringify(anObj)
Output: '{"x": 5, "y": "Oliver"}'

aList = [1, "hello", "null", {"x": 5, "y": "Oliver"}]
stringify(aList)
Output: '[1, "hello", "null", {"x": 5, "y": "Oliver"}]'

A brief note about the input and output. They look very similar, but the input is an object and the output is a string enclosed in single ticks. This means that the double quotes inside that string are characters in the string and are important.


🔎 EXPLORE
List your assumptions & discoveries:


Insightful & revealing test cases:


🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()


📆 PLAN
Outline of algorithm #:


🛠️ IMPLEMENT
function stringify(obj) {


🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
# class TreeNode:
#     def __init__(self, value = 0, left = None, right = None):
#         self.value = value
#         self.left = left
#         self.right = right
#
# def walk(curr, max_val = [float('-inf')]):
#     if not curr:
#         return max_val[0]
#     max_val[0] = max(max_val[0], curr.value)
#     walk(curr.left, max_val)
#     walk(curr.right, max_val)
#     return max_val[0]
# def tree_max(root: TreeNode):
#     # Write your code here.
#     return walk(root, [float('-inf')])
#
# # Test Cases
# print(tree_max(None), float("-inf"))
# print(tree_max(TreeNode(1, TreeNode(2), TreeNode(3))), 3) # 3
# print(tree_max(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), 29)
# print(tree_max(TreeNode(1)), 1)
'''▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a binary tree, find the element with the largest value.

Example:
• Given a binary tree:
                 1
                / \
               7   3
              / \
             4   5
// returns 7

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def tree_max(root: TreeNode):
    # Write your code here.
    return -1

# Test Cases
print(tree_max(None), float("-inf"))
print(tree_max(TreeNode(1, TreeNode(2), TreeNode(3))), 3) # 3
print(tree_max(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), 29)
print(tree_max(TreeNode(1)), 1)

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟨 Javascript
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
class TreeNode {
    constructor(value = 0, leftChild = null, rightChild = null) {
        this.value = value
        this.left = leftChild
        this.right = rightChild
    }
}

function findTreeMax(root) {
    // Write your code here.
    return -1
}

// Test Cases
console.log(findTreeMax(null)) // null
console.log(findTreeMax(new TreeNode(1, new TreeNode(2), new TreeNode(3)))) // 3
console.log(findTreeMax(new TreeNode(2, new TreeNode(29, new TreeNode(26)), new TreeNode(4, null, new TreeNode(2, new TreeNode(9)))))) // 29
console.log(findTreeMax(new TreeNode(1))) // 1
'''
# def printAllPairs(arr):
#     slow, fast = 0, 1
#     while slow < fast and slow < len(arr):
#         while fast < len(arr):
#             print((arr[slow], arr[fast]))
#             fast += 1
#         slow += 1
#         fast = slow + 1
# printAllPairs([1,2,3,4])
# printAllPairs([1,2,3])
'''
❓ PROMPT
Finding all pairs is one of the basic patterns that frequently comes up, especially in _brute force_ algorithms. Understanding and proficiently applying this pattern will often jump-start progress on other problems, even if in the end there may be a way to do something more efficiently.

To illustrate this pattern, write a function that takes an array and prints out all of the pairs of elements from the array.

Example(s)
printAllPairs([1,2,3])
(1, 2)
(1, 3)
(2, 3)

printAllPairs([1,2,3,4])
(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)


🔎 EXPLORE
List your assumptions & discoveries:


Insightful & revealing test cases:


🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()


📆 PLAN
Outline of algorithm #: 


🛠️ IMPLEMENT
function printAllPairs(array) {
def printAllPairs(array: list[int]) -> None:


🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
# actions = [
#     ("add_operator", "A"),         # Add operator A
#     ("add_operator", "B"),         # Add operator B
#     ("receive_call", "1"),         # Receive call 1, connect it to operator A (first available)
#     ("receive_call", "2"),         # Receive call 2, connect it to operator B (next available)
#     ("release_operator", "A"),     # Release operator A from call 1
#     ("receive_call", "3"),         # Receive call 3, connect it to operator A (first available after release)
#     ("release_operator", "B"),     # Release operator B from call 2
#     ("receive_call", "4"),         # Receive call 4, connect it to operator B (first available after release)
# ]
#
# def process_actions(input):
#     result = []
#     op_q = []
#     active_op_q = set()
#     for (action, id) in actions:
#         if action == 'add_operator':
#             op_q.append(id)
#         elif action == 'release_operator':
#             active_op_q.remove(id)
#             op_q.append(id)
#         elif action == 'receive_call':
#             op = op_q.pop(0)
#             result.append((id, op))
#             active_op_q.add(op)
#     return result
#
# print(process_actions(actions))
'''
❓ PROMPT
Design a simplified call center system that connects incoming calls to available operators.

The system should provide the following features:

* Add or release operators.
* Accept incoming calls.
* Assign calls to operators in the order they were received.
* If no operators are available, the calls should be queued and connected to an operator once one becomes available.

Implement a function that takes a list of actions and processes them. Each action is a tuple containing two strings.

The first string represents the action type ("add_operator", "receive_call", or "release_operator"), and the second string represents the ID of the operator or call.

Example(s)
actions = [
    ("add_operator", "A"),         # Add operator A
    ("add_operator", "B"),         # Add operator B
    ("receive_call", "1"),         # Receive call 1, connect it to operator A (first available)
    ("receive_call", "2"),         # Receive call 2, connect it to operator B (next available)
    ("release_operator", "A"),     # Release operator A from call 1
    ("receive_call", "3"),         # Receive call 3, connect it to operator A (first available after release)
    ("release_operator", "B"),     # Release operator B from call 2
    ("receive_call", "4"),         # Receive call 4, connect it to operator B (first available after release)
]

Output: [('1', 'A'), ('2', 'B'), ('3', 'A'), ('4', 'B')]



🔎 EXPLORE
List your assumptions & discoveries:


Insightful & revealing test cases:


🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()


📆 PLAN
Outline of algorithm #: 


🛠️ IMPLEMENT
function processCallCenterActions(actions) {) // returns list
def process_call_center_actions(actions: list[tuple]) -> list:


🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
'''
❓ PROMPT
We have a number of bunnies, each with two big floppy ears. We want to compute the total number of ears across all the bunnies recursively, without loops or multiplication.

Example(s)
bunnyEars(3) == 6
bunnyEars(5) == 10


🔎 EXPLORE
List your assumptions & discoveries:


Insightful & revealing test cases:


🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()


📆 PLAN
Outline of algorithm #:


🛠️ IMPLEMENT
function bunnyEars(bunnies) {
def bunnyEars(bunnies: int) -> int:


🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

# def bunnyEars(count):
#     if count == 0:
#         return 0
#     return 2 + bunnyEars(count - 1)
#
# print(bunnyEars(3) == 6)
# print(bunnyEars(5) == 10)


# class listnode:
#     def __init__(self, value=0, next=none):
#         self.value = value
#         self.next = next
#
#
# def count(node: listnode) -> int:
#     if not node:
#         return 0
#     return 1 + count(node.next)
#
#
# # test cases
# ll1 = listnode(1, listnode(4, listnode(5)))
# print(count(none))  # 0
# print(count(ll1))  # 3
# print(count(ListNode()))  # 1

# def dutch(arr):
#     l, m, r = 0, 1, len(arr) - 1
#
# print(dutch([1, 0, 2, 0, 1, 2]))


# def reverse_words(s):
#     """
#     Args:
#      s(str)
#     Returns:
#      str
#     """
#     # Write your code here.
#     result = s.split()
#     result.reverse()
#     print(' '.join(result))
#     print(result)
#
#     # return ' '.join(s.split().reverse())
#
# reverse_words('a b c')
# # def build_dict(_list):
# #     result = {}
# #     for num in _list:
# #         if num in result:
# #             result[num] += 1
# #         else:
# #             result[num] = 1
# #     return result
# #
# #
# # def get_intersection_with_maintained_frequency(a, b):
# #     """
# #     Args:
# #      a(list_int32)
# #      b(list_int32)
# #     Returns:
# #      list_int32
# #     """
# #     # Write your code here.
# #
# #     mapA = build_dict(a)
# #     mapB = build_dict(b)
# #     print(mapA)
#
#     # for num in a:
#     #     if num in mapA:
#     #         mapA[num] += 1
#     #     else:
#     #         mapA[num] = 1
#     # for num in b:
#     #     if num in mapB:
#     #         mapB[num] += 1
#     #     else:
#     #         mapB[num] = 1
#
#     # aSet = set(list(mapA.keys()))
#     # bSet = set(list(mapB.keys()))
#     # result = []
#     # for key in aSet.intersection(bSet):
#     #     for i in range(min(mapA[key], mapB[key])):
#     #         result.append(key)
#
#     # return result
#
#
# # 12/4/23
#
#
#
# # grand staircase
# # def solution(n):
# #     m = [[0 for i in range(n + 1)] for j in range(n + 1)]
# #     m[0][0] = 1  # base case
# #     for stair in range(1, n + 1):
# #         for left in range(0, n + 1):
# #             m[stair][left] = m[stair - 1][left]
# #             if left >= stair:
# #                 m[stair][left] += m[stair - 1][left - stair]
# #
# #     return m[n][n] - 1
# #
# #
# # print(solution(5))
# #
#
# # sorting version numbers
#
# # def str_to_list(str):
# #     return str.split('.')
# #
# # def get_major(ver_arr):
# #     return ver_arr[0]
# #
# # def solution(l):
# #     l.sort(key=lambda val: [int(section) for section in val.split(".")])
# #     return l
#     # def parse_version(version_str):
#     #     parts = version_str.split('.')
#     #     major = int(parts[0])
#     #     minor = int(parts[1]) if len(parts) > 1 else 0
#     #     revision = int(parts[2]) if len(parts) > 2 else 0
#     #     return major, minor, revision
#
#     # return sorted(l, key=lambda version_str: parse_version(version_str))
#
#
# #
# # sol = solution((["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
# # print(sol)
# # sol = solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
# # print(sol)
#
#
# # knight movement
#
# # def get_coords_from_number(num):
# #     x = num // 8
# #     y = num % 8
# #     return x, y
# #
# # def get_num_from_coords(coords):
# #     return 8 * coords[0] + coords[1]
# #
# # def is_legal_move(final_coords):
# #     x = final_coords[0]
# #     y = final_coords[1]
# #
# #     return 0 <= x <= 7 and 0 <= y <= 7
# #
# #
# # def get_possible_moves(start_coord, visited, depth):
# #     moves = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, -2)]
# #     result = []
# #     x, y, _ = start_coord
# #     for m in moves:
# #         dx, dy = m
# #         new_xyd = (dx + x, dy + y, depth)
# #         if is_legal_move(new_xyd) and not visited[new_xyd[0]][new_xyd[1]]:
# #             result.append(new_xyd)
# #     return result
# #
# #
# # def solution(src, dest):
# #     if not (0 <= src <= 63) or not (0 <= dest <= 63):
# #         return -1
# #
# #     starting_coords = get_coords_from_number(src)
# #     start_x, start_y = starting_coords
# #     q = [(start_x, start_y, 0)]
# #     visited = [[False for _ in range(8)] for _ in range(8)]
# #     while len(q) > 0:
# #         curr = q.pop(0)
# #         x, y, depth = curr
# #
# #         if get_num_from_coords(curr) == dest:
# #             # print('dest found:', depth)
# #             return depth
# #         if not visited[x][y]:
# #             visited[x][y] = True
# #             q = q + get_possible_moves(curr, visited, depth + 1)
# #     return - 1
# #
# #
# #
# # solution(19,36)
# # solution(0, 1)
# # solution(0, 0)
# # # solution(0, 54)
# # # solution(0, 42)
# # # solution(0,56)
# # solution(-1, 2)
#
#
# # Solar Doomsday
# # ==============
# # Who would've guessed? Doomsday devices take a LOT of power. Commander Lambda wants to supplement the LAMBCHOP's quantum antimatter reactor core with solar arrays, and you've been tasked with setting up the solar panels.
# # Due to the nature of the space station's outer paneling, all of its solar panels must be squares. Fortunately, you have one very large and flat area of solar material, a pair of industrial-strength scissors, and enough MegaCorp Solar Tape(TM) to piece together any excess panel material into more squares. For example, if you had a total area of 12 square yards of solar material, you would be able to make one 3x3 square panel (with a total area of 9). That would leave 3 square yards, so you can turn those into three 1x1 square solar panels.
# # Write a function test(solution(area) that takes as its input a single unit of measure representing the total area of solar panels you have (between 1 and 1000000 inclusive) and returns a list of the areas of the largest squares you could make out of) those panels, starting with the largest squares first. So, following the example above, test(solution(12) would return [9, 1, 1, 1].)
# # Test cases
# # ==========
# # Your code should pass the following test cases.
# # Note that it may also be run against hidden test cases not shown here.
# #
# # -- Python cases --
# # Input:
# # test(solution.test(solution(12))
# # Output:
# #     9,1,1,1
# #
# # Input:
# # test(solution.test(solution(15324))
# # Output:
# #     15129,169,25,1
#
# import random
# # import math
# #
# #
# # def max_square(upper_bound):
# #     sqrt = int(math.sqrt(upper_bound))
# #     return sqrt * sqrt
# #
# #
# # def solution(area):
# #     remaining_area = area
# #     result = []
# #     while remaining_area > 0:
# #         largest_square = max_square(remaining_area)
# #         result.append(largest_square)
# #         remaining_area -= largest_square
# #
# #     return result
# #
# # solution(12)
# # solution(15324)
#
# #
# # def test(sol, area):
# #     return sum(sol) == area
# #
# #
# # def test_kit():
# #     for i in range(100000):
# #         random_num = math.floor(random.random() * 1000000)
# #         sol = solution(random_num)
# #         the_test = test(sol, random_num)
# #         if not the_test:
# #             print('random_num', random_num)
# #             print('sol:', sol)
#
#
# # test_kit()
#
#
#
#
# # print(test(solution(107897), 107897))
# # print(test(solution(12), 12))
#
#
# # print(test(solution(15324), 15324))
# # print(test(solution(145)))
# # print(test(solution(150)))
# # print(test(solution(-10)))
# # print(test(solution(1)))
# # print(test(solution(222)))
#
# # def solution3(area):
# #     result = []
# #
# #     while area > 0:
# #         # Find the largest square that can be formed from the remaining area
# #         side = int(math.sqrt(area))
# #         square = side * side
# #
# #         # Add the square to the result list
# #         result.append(square)
# #
# #         # Reduce the remaining area by the square's area
# #         area -= square
# #
# #     return result
# #
# # print(solution3(12))
# # print(solution3(15324))
#
#
# # def solution2(area):
# #     res = []
# #     while area > 0:
# #         biggest_square_side = int(area ** 0.5)
# #         biggest_square_area = biggest_square_side ** 2
# #         area -= biggest_square_area
# #         res.append(biggest_square_area)
# #
# #     return res
#
# # import math
#
#
# #
# # def comp(array1, array2):
# #     dict = {}
# #     for n in array1:
# #         if n in dict:
# #             dict[n] += 1
# #         else:
# #             dict[n] = 1
# #     print(dict)
# #     for n in array2:
# #         sqrt = math.sqrt(n)
# #         print(sqrt in dict)
# #         if not sqrt.is_integer:
# #             return False
# #         if sqrt not in dict:
# #             return False
# #         elif dict[sqrt] == 1:
# #             del dict[sqrt]
# #         else:
# #             dict[sqrt] -= 1
# #     return not bool(dict)
# #
# # a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# # a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
# #
# #
# # print(comp(a1, a2))
# #
#
#
# # Example 1: Define a function that takes an argument. Call the function. Identify what code is the argument and what code is the parameter.
# #
# # Example 2: Call your function from Example 1 three times with different kinds of arguments: a value, a variable, and an expression. Identify which kind of argument is which.
# #
# # Example 3: Construct a function with a local variable. Show what happens when you try to use that variable outside the function. Explain the results.
# #
# # Example 4: Construct a function that takes an argument. Give the function parameter a unique name. Show what happens when you try to use that parameter name outside the function. Explain the results.
# #
# # Example 5: Show what happens when a variable defined outside a function has the same name as a local variable inside a function. Explain what happens to the value of each variable as the program runs.
#
#
# # #1
# # def title_case(str: str):
# #     return str.title()
# # #2
# # print(title_case("this is a class i didn't know i was registered for"))
# # print(title_case("it takes any string"))
# # print(title_case("and title cases it; makes every words first letter capitalized"))
#
# # 3
# # bar = 1
# # def foo(string: str):
# #     print(string)
#
# # foo(1)
