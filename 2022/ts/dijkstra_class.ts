type Node = { name: string; weight: number; prev: string };
type Neighbor = { name: string; weight: number };
type GraphNode = { name: string; weight: number };
type Graph = Map<string, GraphNode[]>;

class Djikstra {
  private queue: Node[] = [];
  private visited: Node[] = [];

  constructor(
    private graph: Graph,
    private start: string,
    private end: string,
  ) {
    this.init();
    this.run();
  }

  updateQueue() {
    this.queue.sort((a, b) => a.weight - b.weight);
  }

  enqueue(node: Node) {
    this.queue.push(node);
    this.updateQueue();
  }

  init() {
    for (const g of this.graph.keys()) {
      if (g === this.start) {
        this.enqueue({ name: g, weight: 0, prev: "" });
      } else {
        this.enqueue({ name: g, weight: Infinity, prev: "" });
      }
    }
  }

  run() {
    while (this.queue.length > 0) {
      const node = this.queue.shift();
      if (node) {
        const neighbors = this.graph.get(node.name) ?? [];
        for (const neighbor of neighbors) {
          for (const item of this.queue) {
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
        this.updateQueue();
        this.visited.push(node);
      }
    }
  }

  getNodeFromVisited(nodeName: string): Node | undefined {
    for (const v of this.visited) {
      if (v.name === nodeName) {
        return v;
      }
    }
    return undefined;
  }

  distance(): number {
    const node = this.getNodeFromVisited(this.end);
    if (node) {
      return node.weight;
    }
    return 0;
  }
}

const sample = new Map<string, GraphNode[]>();
sample.set("London", [{ name: "Dublin", weight: 464 }, {
  name: "Belfast",
  weight: 518,
}]);
sample.set("Dublin", [{ name: "Belfast", weight: 141 }, {
  name: "London",
  weight: 464,
}]);
sample.set("Belfast", [{ name: "London", weight: 518 }, {
  name: "Dublin",
  weight: 141,
}]);

const d = new Djikstra(sample, "London", "Belfast");
console.log(d.distance());
