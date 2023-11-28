package io.trox667.aoc.algorithms;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Graph {
    // Each node name has a list of neighbors with their distance
    private HashMap<String, List<Node>> nodes;

    public Graph() {
        this.nodes = new HashMap<>();
    }

    /**
     * Insert a node to a given node name.
     *
     * @param toNode the name of the node
     * @param node the node to insert
     */
    public void insertNode(String toNode, Node node) {
        if (this.nodes.containsKey(toNode)) {
            // if the node already exists, add the new node to the list
            this.nodes.get(toNode).add(node);
        } else {
            // if the node does not exist yet, create a new list
            var list = new ArrayList<Node>();
            list.add(node);
            this.nodes.put(toNode, list);
        }
    }

    public List<Node> getNeighbors(String node) {
        return this.nodes.get(node);
    }

    public List<String> getNodeNames() {
        return new ArrayList<>(this.nodes.keySet());
    }
}
