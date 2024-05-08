/*
'''
Given an adjacency list of a directed graph, return "BINARY TREE" if it's a binary tree, "TREE" if it's any other type of tree, or "GRAPH" if it's neither.


EXAMPLE(S)
     1
   /   \
 2     3
/
4

input:
classify(
    {
        1: [2, 3],
        2: [4],
        3: [],
        4: []
    }

) -> BINARY TREE
There should be no cycles or loops
Node can't have more than one parent
No disconnected nodes
--------------

     1        5
   /   \
 2     3
/
4

input:
classify(
    {
        1: [2, 3],
        2: [4],
        3: [],
        4: [],
        5: [],
    }
) -> GRAPH

--------------

     1
   /   \
 2     3
   \  /
     4

input:
classify(
    {
        1: [2, 3],
        2: [4],
        3: [4],
        4: [],
    }
) -> GRAPH


FUNCTION SIGNATURE
function classify(adjList) {
def classify(adjList: dict[int, list[str]]) -> str:
'''
*/
function classify(adjList) {
  if (!Object.keys(adjList).length) {
    return 'BINARY TREE'
  }

  function isGraph(adj_graph) {
    const node_set = new Set()
    const vertex_set = new Set()
    for (const key of Object.keys(adj_graph)) {
      vertex_set.add(key)
      const children = adj_graph[key]
      children.forEach(val => {
        if (val in node_set) {
          return true
        }
        node_set.add(val)
        })
    }
    for (const key of node_set) {
      if (!adj_graph.hasOwnProperty(key)) {
        adj_graph[key] = []
      }
    }
    console.log(node_set)
    if (node_set.length !== Object.keys(adj_graph).length - 1) {
      return true
    }
    return false
  }

  function isBinaryTree(adj_list) {
    for (const key of Object.keys(adj_list)) {
      if (adj_list[key].length > 2) {
        return false;
      }
    }

    return true;
  }

  if (isBinaryTree(adjList)) {
    return 'BINARY TREE';
  }

  if (isGraph(adjList)) {
    return 'GRAPH';
  }

  return 'TREE';
}



const multiTree = {
    1: [2, 3],
    2: [4],
    3: [5, 6, 7],
  4: [],
}
console.log(classify(multiTree))

// const binaryTree = {
//     1: [2, 3],
//     2: [4],
//     3: [],
//     4: [],
// }
// console.log(classify(binaryTree) == 'BINARY TREE')

// const doubleRoot = {
//     1: [2, 3],
//     2: [4],
//     3: [],
//     4: [],
//     5: [],
// }
// console.log(classify(doubleRoot) == 'GRAPH')

// const sharedParent = {
//     1: [2, 3],
//     2: [4],
//     3: [4],
//     4: [],
// }
// console.log(classify(sharedParent) == 'GRAPH')

// const oneNode = {
//     1: [],
// }
// console.log(classify(oneNode) == 'BINARY TREE')

// const noNode = {}
// console.log(classify(noNode) == 'BINARY TREE')

// const oneNodeCycle = {
//     1: [1],
// }
// console.log(classify(oneNodeCycle) == 'GRAPH')

// const nestedCycle = {
//     1: [2, 3],
//     2: [],
//     3: [3, 4],
//     4: [],
// }
// console.log(classify(nestedCycle) == 'GRAPH')


function classify(adjList) {
  // The initial set of potential roots is all of the nodes
  // that have children, so the keys of the adjacency lists object.
  const potentialRoots = new Set(Object.keys(adjList).map(k => Number(k)));

  // Special case: if the graph is empty, then it can be any
  // type so make it the most restrictive.
  if (potentialRoots.size === 0) return "BINARY TREE";

  let maxChildren = 0;
  let maxParents = 0;
  const parentCounts = {};

  // Cull out potential roots that appear in child lists.
  // Also count the number of parents a child has.
  for (const node of Object.keys(adjList)) {
    maxChildren = Math.max(maxChildren, adjList[node].length);
    for (const child of adjList[node]) {
      // This node has a parent so it's not a root.
      potentialRoots.delete(child);

      // Add this to the parent count for this child node.
      if (parentCounts[child] === undefined) {
        parentCounts[child] = 0;
      }
      parentCounts[child]++;
      maxParents = Math.max(maxParents, parentCounts[child]);
    }
  } // O(N)

  // If any node has more than one parent, it's a graph.
  if (maxParents > 1) return "GRAPH";

  // If there is any number of potential roots OTHER than 1,
  // it's a graph.
  if (potentialRoots.size !== 1) return "GRAPH";

  // Helper function to detect cycles vs DFS
  function hasCycle(root) {
    const visited = new Set();
    const queue = [root];
    let position = 0;

    while (position < queue.length) {
      const node = queue[position++];
      visited.add(node);
      if (adjList[node] === undefined) continue;
      for (const child of adjList[node]) {
        if (visited.has(child)) {
          return true;
        }
        queue.push(child);
      }

    }
    return false;
  }

  // We know we have one root. Is there a cycle from this point?
  const [singleRoot] = potentialRoots;
  if (hasCycle(singleRoot)) return "GRAPH";

  // After eliminating other possibilities, it's a tree or binary tree
  // based on the max number of children.
  return maxChildren > 2 ? "TREE" : "BINARY TREE";
}
//Tc: o(v+e)