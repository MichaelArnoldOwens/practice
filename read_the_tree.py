'''
❓ PROMPT
In many but not all languages, humans read from top to bottom, left to right. This problem is convert a tree to a list of values in this reading order. Since computer scientists draw trees with the root at the top, the first node we read is that one, followed by the nodes at the first level down (only at most two nodes), then the third level, etc. For example:

      a
    /  \
   b     c
 /
d

We would read this as [a, b, c, d].

Write a function that generates a list of the values in a binary tree in this reading order.

Example(s)
treeToArray(new BTNode("a")) - returns ['a']
treeToArray(new BTNode("a", new BTNode("b"))) - only left child, returns ['a', 'b']
treeToArray(new BTNode("a", null, new BTNode("b"))) - only right child, returns ['a', 'b']
treeToArray(new BTNode("a", new BTNode("b"), new BTNode("c"))) - basic tree with both left and right children, , returns ['a', 'b', 'c']

 

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
function treeToArray(root)
function tree_to_array(root):
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
class BTNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def print_node(root):
    if not root:
        return
    print(root.val)
    print_node(root.left)
    print_node(root.right)


def treeToArray(root):
    q = [root]
    result = []
    while len(q):
        curr = q.pop(0)
        result.append(curr.val)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    return result

print(treeToArray(BTNode("a"))) # - returns ['a'])
print(treeToArray(BTNode("a", BTNode("b")))) # - only left child, returns ['a', 'b'])
print(treeToArray(BTNode("a", None, BTNode("b")))) # - only right child, returns ['a', 'b'])
print(treeToArray(BTNode("a", BTNode("b"), BTNode("c")))) # - basic tree with both left and right children, , returns ['a', 'b', 'c'])


