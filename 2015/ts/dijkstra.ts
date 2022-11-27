type Node = { name: string; weight: number; prev: string };
type Neighbor = { name: string; weight: number };

const graph = {
  "S": [{ name: "A", weight: 7 }, { name: "B", weight: 2 }, {
    name: "C",
    weight: 3,
  }],
  "A": [{ name: "B", weight: 3 }, { name: "D", weight: 4 }],
  "B": [{ name: "A", weight: 3 }, { name: "D", weight: 4 }, {
    name: "H",
    weight: 1,
  }],
  "C": [{ name: "S", weight: 3 }, { name: "L", weight: 2 }],
  "D": [{ name: "A", weight: 4 }, { name: "B", weight: 4 }, {
    name: "F",
    weight: 5,
  }],
  "F": [{ name: "D", weight: 5 }, { name: "H", weight: 3 }],
  "H": [{ name: "B", weight: 1 }, { name: "F", weight: 3 }, {
    name: "G",
    weight: 2,
  }],
  "G": [{ name: "H", weight: 2 }, { name: "E", weight: 2 }],
  "L": [{ name: "C", weight: 2 }, { name: "I", weight: 4 }, {
    name: "J",
    weight: 4,
  }],
  "I": [{ name: "L", weight: 4 }, { name: "J", weight: 6 }, {
    name: "K",
    weight: 4,
  }],
  "J": [{ name: "L", weight: 4 }, { name: "I", weight: 6 }, {
    name: "K",
    weight: 4,
  }],
  "K": [{ name: "I", weight: 4 }, { name: "J", weight: 4 }, {
    name: "E",
    weight: 5,
  }],
  "E": [{ name: "G", weight: 2 }, { name: "K", weight: 5 }],
};
type Graphkey = keyof typeof graph;

// stack with visited notes
const visited: Node[] = [];

// priority queue with notes, sorted by the shortest distance
const queue: Node[] = [];
function enqueue(node: Node) {
  queue.push(node);
  updateQueue();
}

function updateQueue() {
  queue.sort((a, b) => {
    return a.weight - b.weight;
  });
}

// init all nodes with inifinity distance and an unknown previous node
function init() {
  for (const g in graph) {
    if (g === "S") {
      enqueue({ name: g, weight: 0, prev: "" });
    } else {
      enqueue({ name: g, weight: Infinity, prev: "" });
    }
  }
}

function getNodeFromVisited(nodeName: string): Node | undefined {
  for (const v of visited) {
    if (v.name === nodeName) {
      return v;
    }
  }
  return undefined;
}

function distance(nodeName: string) {
  const node = getNodeFromVisited(nodeName);
  if (node) {
    return node.weight;
  }
  return 0;
}

function path(endNode: string): string[] {
  const p = [];
  let node = getNodeFromVisited(endNode);
  if (node) {
    while (node) {
      p.push(node.name);
      node = getNodeFromVisited(node.prev);
    }
    return p.reverse();
  }
  return [];
}

init();

// loop over priority queue until end found or queue empty
while (queue.length > 0) {
  const node = queue.shift();
  if (node) {
    const neighbors = graph[node.name as Graphkey];
    for (const neighbor of neighbors) {
      // neighbor is still in queue, update distance
      for (const item of queue) {
        if (item.name === neighbor.name) {
          const newWeight = node.weight + neighbor.weight;
          if (newWeight < item.weight) {
            item.weight = newWeight;
            item.prev = node.name;
          }
          break;
        }
      }
    }
    updateQueue();
    visited.push(node);
  }
}
// console.log(visited);
console.log(path("E"));
console.log(distance("E"));
