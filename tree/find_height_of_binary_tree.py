'''
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a binary tree, find the height of the tree.

Example:
• Given a binary tree:
                 1
                / \
               7   3
              / \
             4   5
// returns 2
'''
class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def tree_height(root: TreeNode) -> int:
    if not root:
        return 0
    pass


# Test Cases
print(tree_height(None), -1) # -1
print(tree_height(TreeNode(1, TreeNode(2), TreeNode(3))), 1) # 1
print(tree_height(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), 3) # 3
print(tree_height(TreeNode()), 0) # 0
