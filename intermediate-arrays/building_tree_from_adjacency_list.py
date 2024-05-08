# /*
# '''
# Putting Up The Tree
#
# Just like putting up an artificial holiday tree, in this problem, we'll build a tree from a box of parts. In our case, the box of parts will be a list of lists (nested arrays) that represent the edges between nodes.
#
# * The index into the outer array identifies a node of the tree
# * The inner array lists the nodes that are children of the current one
# * The value at each node should be it's index in the original array
# * The value at each index should be the children of that node
# * For starters, you may assume that the tree will be a binary tree, the first index in the list is the left child, the second is the right.
# * A null or None indicates a missing child
#
# For example:
#
# [
#   0: [1, 2],
#   1: [null, null], // or [None, None] for Python folks
#   2: [] // assume null if missing
# ]
#
# This describes a tree that is shaped like this:
# 
#    0
#  /  \
# 1    2
#
# As a follow up, extend this code to support N-ary trees, that is, a tree that allows an arbitrary number of children. How does this change the time complexity?
#
#
# EXAMPLE(S)
#      0
#    /   \
#   1     2
#  /
# 3
#
# input:
# buildTree(
#     [
#         [1, 2],
#         [3],
#         [],
#         []
#     ]
# ) -> returns a pointer to the node with the value 0.
#
# -------------------------
#
#      2
#    /   \
#   0     3
#  /
# 1
#
# input:
# buildTree(
#     [
#         [1], // 0
#         [], // 1
#         [0, 3], // 2
#         [],   // 3
#     ]
#   // build a tree
#   {node: pointer_of the node}
#   node set([1-len(list)])
#   iterate the list
#     create the parent
#     check if map has the child
#       remove children from nodeSet
#       use that ptr to link the parent and child
#       else
#       create the children -> store ptr into dictionary
#     link the parent and children together
#     store the parent into the dictionary [value of the node]: ptr to the node
#
#   if nodeSet.size() > 1 return null
#   return nodeSet.values().next().value
#
#   // find root
#   //   {1, 0, 3} => 2
#   //   total of number of nodes = len(list)
#   //  set([1- len(list)])
#   //  traverse adj list => remove the node we're visting from the set
#   //  and the leftover node in the set at the end of the bfs traversal will be the root
# ) -> returns a pointer to the node with the value 2.
#
# Explore:
# Will the root always be node 0?
#
# Assumptions:
#  - valid tree (single parent for each node)
#  - the tree will be connected
#  - the root will no parents
#
# Brainstorm:
# Find the root node
# Generate the tree
# Return the root node
#
#
# plan
#
# function buildTree(adjLists) {
#   if adjLists.length === 0 return null
#   const nodeSet = new Set(Array(adjLists.length).map((val,idx) => idx + 1))
#   for children in adjLists:
#     children.forEach(val => nodeSet.remove(val))
#   if nodeSet.size() > 1 return null
#   return nodeSet.values().next().value
# }
#
#
# FUNCTION SIGNATURE
# def buildTree(adj_lists) -> Node:
# '''
# */
#
# /*
#   // build a tree
#   {node: pointer_of the node}
#   node set([1-len(list)])
#   iterate the list
#     create the parent
#     check if map has the child
#       remove children from nodeSet
#       use that ptr to link the parent and child
#       else
#       create the children -> store ptr into dictionary
#     link the parent and children together
#     store the parent into the dictionary [value of the node]: ptr to the node
#
#   if nodeSet.size() > 1 return null
#   return nodeSet.values().next().value
# */
#
# class Node {
#   constructor(value, left = null, right = null) {
#     this.left = left;
#     this.right = right;
#     this.value = value;
#   }
# }
#
# const buildTree = adjList => {
#   if (adjList.length === 0) return null;
#   const nodeSet = new Set(Array(adjList.length).fill(0).map((x, i) => i));
#   const nodeMap = {};
#
#   for (let i = 0; i < adjList.length; i++) {
#     const [left, right] = adjList[i];
#     nodeSet.delete(left);
#     nodeSet.delete(right);
#
#     const curr = nodeMap[i] ? nodeMap[i] : new Node(i)  // {value: 0, left: null, right: null}
#     nodeMap[i] = curr;
#     /*
#        { 0: { value: 0, left: {1, left: null, right: null}, right: null },
#         1: {1, left: null, right: null}
#         }
#     */
#
#     if (left !== undefined) {
#       if (nodeMap[left]) {
#         curr.left = nodeMap[left]
#       } else {
#         const left_node = new Node(left) // {1, left: null, right: null}
#         nodeMap[left] = left_node
#         curr.left = nodeMap[left]
#       }
#     }
#     if (right !== undefined) {
#       if (nodeMap[right]) {
#         curr.right = nodeMap[right]
#       } else {
#         const right_node = new Node(right)
#         nodeMap[right] = right_node
#         curr.right = right_node
#       }
#     }
#   }
#
#   if (nodeSet.size > 1) return null;
#
#   const rootValue = [...nodeSet.values()][0]
#
#   return nodeMap[rootValue];
# }
#
# // Tests
# const list0 = [[]]
# const list1 = [[1, 2], [], []]
# const list2 = [[1, 2], [3], [], []]
#
# console.log(buildTree(list0));
# console.log(buildTree(list1));
# console.log(buildTree(list2));
#
# console.log(buildTree([
#   [1], // 0
#   [], // 1
#   [0, 3], // 2
#   [],   // 3
# ]))