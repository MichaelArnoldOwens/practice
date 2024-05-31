// # Graphs

// ## Calibration

// - Vertexes and edges
// - Directed and undirected
// - Prim's, Dijkstra's
// - Real World Data Structure (now on MTV)
// - Any kind of relational data (almost) -- way to hedge
// - Start node end node
//   - "cycles and all that" she says very casually

// ### Terms

// Here's a list of graph terms. Put your initial next to any you haven't heard before or aren't totally sure about:

// - Vertex / node:
// - Edge:
// - Degree (directed vs. undirected):
// - Source and sink: ap, nk
// - Directed vs. Undirected:
// - Path (directed vs. undirected):
//   - Walk: nk no restrictions except follow edges
//   - Trail: ap, mo, nk - no duplicate edges traversed
//   - Path: no duplicate vertices traversed - allows discovering cycle easily
// - Cycle:
//   - A trail that starts and ends at the same vertex
// - Connected (vs. disconnected):
//   - For any two vertexes v and w, there's a path starting at v and ending at w


function dfsFromNode(graph, node, callback, visited = new Set()) {
  if (!node) return;
  if (visited.has(node)) return;

  visited.add(node)

  // pre-order
  callback(node);

  for (const neighbor of graph[node]) {
    dfsFromNode(graph, neighbor, callback, visited);
  }

  // post-order
  // callback(node);
}

function treeDFS(root, callback) {
  if (!root) return;

  // callback(root);
  // dfs(root.left);
  // dfs(root.right);
}


function dfs(graph, callback) {
  let visited = new Set();

  for (let node of Object.keys(graph)) {
    dfsFromNode(graph, node, callback, visited);
  }
}

function bfsFromNode(graph, startNode, callback, visited = new Set()) {
  let bagOfNodes = [startNode];

  while (bagOfNodes.length > 0) {
    let node = bagOfNodes.shift();

    if (visited.has(node)) {
      continue;
    }

    visited.add(node);

    callback(node);

    for (let neighbor of graph[node]) {
      bagOfNodes.push(neighbor);
    }
  }
}

function shorestPathFromNode(graph, startNode) {
  let distances = new Map();

  for (let node of Object.keys(graph)) {
    if (node === startNode) {
      distances.set(node, 0);
    } else {
      distances.set(node, Infinity);
    }
  }

  bfsFromNode(graph, startNode, currentNode => {
    for (let neighbor of graph[currentNode]) {
      let currentDistance = distances.get(neighbor);
      distances.set(neighbor, Math.min(currentDistance, distances.get(currentNode) + 1));
    }
  });

  return distances;
}

let graph = {
  'A': ['B', 'C'],
  'B': [],
  'C': ['D'],
  'D': ['B', 'E'],
  'E': ['A'],
  'F': ['C'],
}

// dfsFromNode(graph, 'A', node => console.log(node), new Set())

console.log(shorestPathFromNode(graph, 'A'));
