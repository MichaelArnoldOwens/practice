'''▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
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
'''

class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def tree_max(root):
    # Write your code here. 
    def helper(curr, max_val=float('-inf')):
        if not curr:
            return max_val
        return max(helper(curr.left, max(max_val, curr.value)), helper(curr.right, max(max_val, curr.value)))
        
    return helper(root)

# Test Cases
# print(tree_max(None), float("-inf"))
test1 = TreeNode(1, TreeNode(2), TreeNode(3))
print(tree_max(test1), 3) # 3
# print(tree_max(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), 29)
# print(tree_max(TreeNode(1)), 1)
