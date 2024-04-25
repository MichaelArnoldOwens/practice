'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a binary tree, count the number of elements in the tree.

Example:
• Given a binary tree:
                 1
                / \
               7   3
              / \
             4   5
// returns 5
'''


class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
def count_tree(root: TreeNode) -> int:
    if not root:
      return 0
    counter = 0
    q = [root]
    while len(q) > 0:
      counter += 1
      curr = q.pop()
      if curr.left:
        q.append(curr.left)
      if curr.right:
        q.append(curr.right)
    return counter


# Test Cases
print(count_tree(None), 0)
print(count_tree(TreeNode(1, TreeNode(2), TreeNode(3))), 3)
print(count_tree(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), 6)
print(count_tree(TreeNode()), 1)
