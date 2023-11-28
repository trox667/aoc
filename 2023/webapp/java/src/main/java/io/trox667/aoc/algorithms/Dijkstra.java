package io.trox667.aoc.algorithms;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Dijkstra {
    private List<Node> unvisited;
    private HashMap<String, Node> pathMap;
    private Graph graph;

    public Dijkstra(Graph graph) {
        this.graph = graph;
        this.reset();
    }

    public List<Node> findShortestPath(String start, String end) {
        this.run(start, end);
        var path = new ArrayList<Node>();
        var current = end;
        while (current != null) {
            if (this.pathMap.containsKey(current)) {
                path.add(0, this.pathMap.get(current));
                current = this.pathMap.get(current).name();
            } else {
                current = null;
            }
        }
        return path;
    }

    private void run(String start, String end) {
        for (var node : this.graph.getNodeNames()) {
            if (node.equals(start)) {
                this.unvisited.add(new Node(node, 0));
            } else {
                this.unvisited.add(new Node(node, Integer.MAX_VALUE));
            }
        }

        while (!this.unvisited.isEmpty()) {
            var current = getNextNode();
            if (current.name().equals(end)) {
                break;
            }

            var neighbors = this.graph.getNeighbors(current.name());
            if (neighbors != null) {
                for (var neighbor : neighbors) {
                    for (var unvisitedNode : this.unvisited) {
                        if (unvisitedNode.name().equals(neighbor.name())) {
                            var distance = current.distance() + neighbor.distance();
                            if (distance < unvisitedNode.distance()) {
                                unvisitedNode.setDistance(distance);
                                pathMap.put(neighbor.name(), current);
                            }
                            break;
                        }
                    }
                }
            }
        }
    }

    private Node getNextNode() {
        this.unvisited.sort((a, b) -> a.distance() - b.distance());
        return this.unvisited.removeFirst();
    }

    private void reset() {
        this.unvisited = new ArrayList<>();
        this.pathMap = new HashMap<>();
    }
}
