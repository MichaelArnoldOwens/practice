'''
❓ PROMPT
Convert a sorted array into a balanced binary search tree. Return the root of the created tree.

Example(s)
Input:  [1, 2, 3, 4, 5] =>

Output:
        3
   2        5
1        4

or
        3
    2       4
1              5

or
    3
1       5
   2  4

or
   3
1     4
   2     5



bst -> can take the first value to make it the root
curr = root
curr_q = [root]
then for each 2 values, a b:
  curr = q.pop()
  curr left = a 
  curr right = b
  if curr left
   q.append(left)
  if curr right
   q.append(right)

'''

class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
 
def sorted_arr_to_balanced_tree(arr):
   if not arr:
      return None
   root = TreeNode(arr[0])
   q = [root]
   i = 1
   while i < len(arr) - 1:
      print(i)
      curr = q.pop()
      left_child = TreeNode(arr[i])
      right_child = TreeNode(arr[i + 1])
      curr.left = left_child
      curr.right = right_child
      q.append(left_child)
      q.append(right_child)
      i += 2
   return root



def print_tree(root):
   if not root:
      return []
   result = []
   q = [root]
   while len(q) > 0:
      curr = q.pop(0)
      print(curr.value)
      result.append(curr.value)
      if curr.left:
         q.append(curr.left)
      if curr.right:
         q.append(curr.right)

   return result


print_tree(sorted_arr_to_balanced_tree([1,2,3,4,5]))
'''
def isCorrect(r): return b(r) and v(r)
def gH(r): 
  if r == None: return 0
  lH=gH(r.left)
  if lH==-1: return -1
  rH=gH(r.right)
  if rH==-1: return -1
  if abs(lH-rH)>1: return -1
  return max(lH,rH)+1
def b(r):return gH(r)!=-1
import sys
def v(r): return vx(r,~sys.maxsize,sys.maxsize)
def vx(r,m,M):
  if r==None: return True
  if r.val>=M or r.val<=m: return False
  return vx(r.left,m,r.val) and vx(r.right,r.val,M)

tests = [
  [1, 2, 3, 4, 5],
  [-10, -3, 0, 5, 9], 
  [],
  [1],
  [1,2],
  [1,2,3,4,5],
  [1,2,10,20,35,50,420,609],
  [-100,-50,-25,-20,-10,-1,0,1,2,10,20]
]

for params in tests:
    actual = sorted_arr_to_balanced_tree(params)
    if isCorrect(actual) != True:
        print(f"Test failed for {params}. Actual: {actual}")
    else:
        print(f"Works fine for {params}.")
'''
