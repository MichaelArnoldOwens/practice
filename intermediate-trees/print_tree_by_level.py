'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a binary tree, print level order traversal so that nodes of all levels are printed in several lines

Examples:
• Given a binary tree:
1
/ \
    2   3
// returns [[1], [2, 3]]

• Given a binary tree:
1
/ \
    2   3
/ \
    4   5

// returns [[1], [2, 3], [4, 5]]
'''


class Test:
    def __init__(self, test_name=""):
        self.total_count = 0
        self.problem_count = 0
        self.total_score = 0
        self.problem_score = 0
        self.current_problem = ""
        self.failed_problems = []
        print(f"Beginning Test: {test_name}")

    # Test Helpers
    def test(self, expected_outcome, outcome, case_num=0):
        if expected_outcome == outcome:
            return self.passed(case_num)
        return self.failed(case_num)

    def testMultipleCases(self, possible_outcomes, outcome, case_num=0):
        for possible_outcome in possible_outcomes:
            if possible_outcome == outcome:
                return self.passed(case_num)
        return self.failed(case_num)

    def testMatchAny(self, expected_outcome, outcome, case_num=0):
        if self.isEqual(expected_outcome, outcome):
            return self.passed(case_num)
        return self.failed(case_num)

    def isEqual(self, array1, array2) -> bool:
        for a1 in array1:
            a1.sort()
        sortedArray1 = sorted(array1)
        for a2 in array2:
            a2.sort()
        sortedArray2 = sorted(array2)
        return sortedArray1 == sortedArray2

        # Test Logistics

    def startProblem(self, problemName):
        self.current_problem = problemName
        self.problem_score = 0
        self.problem_count = 0
        self.failed_problems = []

    def passed(self, case_num):
        self.total_score += 1
        self.problem_score += 1
        self.problem_count += 1
        self.total_count += 1

    def failed(self, case_num):
        self.problem_count += 1
        self.total_count += 1
        self.failed_problems.append(case_num)

    def endProblem(self):
        print(f"\n   {self.current_problem} Score: {self.problem_score} / {self.problem_count}")
        if len(self.failed_problems) > 0:
            print(f"   ** Failed Test Cases: {self.failed_problems}")

    def printFinal(self):
        print(f"\nTotal Score: {self.total_score} / {self.total_count}")


test = Test("")


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def arrayify(head) -> list[int]:
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def arrayifyTree(root: TreeNode):
    if root is None:
        return []
    queue = []
    array = []
    queue.append(root)
    while (len(queue) != 0):
        node = queue.pop(0)
        array.append(node.value)
        if (node.left):
            queue.append(node.left)
        if (node.right):
            queue.append(node.right)
    return array


from typing import List
from collections import deque

def printTree(root: TreeNode) -> [[int]]:
    if not root:
        return []
    q = deque([[root]])
    result = []
    while q:
        curr_level = q.popleft()
        curr_level_values = []
        next_level_nodes = []
        for node in curr_level:
            curr_level_values.append(node.value)
            if node.left:
                next_level_nodes.append(node.left)
            if node.right:
                next_level_nodes.append(node.right)
        if len(curr_level_values) > 0:
            result.append(curr_level_values)

        if len(next_level_nodes) > 0:
            q.append(next_level_nodes)

    return result

# Test Cases
test.startProblem("Print Tree by Level")
test.test([[1], [2, 3]], printTree(TreeNode(1, TreeNode(2), TreeNode(3))), 1)
test.test([[2], [29, 4], [26, 2], [9]], printTree(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), 2)
test.test([[1], [2, 3], [4, 5]], printTree(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))), 3)
test.test([[-3]], printTree(TreeNode(-3)), 4)
test.endProblem()