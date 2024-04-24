'''
Question :

Given the root of a binary tree, collect a tree's nodes by level from the leaves up. Return an array of arrays representing the values of the leaves at each iteration.

The result will have the leaves of the tree (no matter the depth from the root) in the first array (index zero), and then the root will be in the last by itself. See the examples below.

The complexity analysis of this one is interesting and might be worth discussing if there is time. What is the best case complexity? Worst case?
'''
from typing import List
# def findLeaves(root: TreeNode) -> List[List[int]]:
#     result = []
#     def helper(curr, level_list=[], level=0, visited={}):

#         if not curr.left and not curr.right and not doesExist(visited, curr): # add doesExist()
#             level_list.append(curr)
#             return
#         if curr.left in visited[curr.left.value] and curr.right in visited[curr.right.value]:
#             level_list.append(curr.value)


#         if curr.value in visited:
#             visited[curr.value].append(curr)
#         else:
#             visited[curr.value] = [curr]

#         if curr.left:
#             helper(curr.left, level_list, level + 1, visited)
#         if curr.right:
#             helper(curr.right, level_list, level + 1, visited)
#         result.append(level_list)

#     helper(root.left)
#     helper(root.right) # need to merge them back
#     return result
'''
deletion approach : 

  while root: 
     helper(root, level_list)
     go through level_list and add it to result 
     mark nodes in level_list
     eventually after visiting root, mark it as null to avoid further loop iterations 

'''


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# def find_height(node, height_map):
#     if not node:
#         return 0
#
#     left_height = find_height(node.left)
#     right_height = find_height(node.right)
#
#     height = 1 + max(left_height, right_height) # needed
#     if left_height in height_map:
#         height_map[height].append(node.val)
#     else:
#         height_map[height] = [node.val]
#
#     if right_height in height_map:
#         height_map[height].append(node.val)
#     else:
#         height_map[height] = [node.val]
#
#     return height
#
#
# def findLeavesV1(root: TreeNode) -> List[List[int]]:
#     if not root:
#         return [[]]
#
#     height_map = {}
#     find_height(root, height_map)
#
#     ans = []
#     for k in sorted(height_map.keys()):
#         ans.append(height_map[k])
#
#     return ans

class TreeNode:
  def __init__(self, val, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right

def findLeaves(root: TreeNode) -> List[List[int]]:
        res = []

        # recursive helper
        def dfs(node):
            if not node:
                return None
            if not node.left and not node.right:
                res[-1].append(node.val)
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node

        # iterative
        while root:
            res.append([])
            root = dfs(root)
        return res


# TODO: https://leetcode.com/problems/distribute-coins-in-binary-tree/description/
