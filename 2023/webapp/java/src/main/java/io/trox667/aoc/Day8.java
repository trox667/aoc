package io.trox667.aoc;

import io.trox667.aoc.algorithms.Graph;
import io.trox667.aoc.algorithms.MathUtils;
import io.trox667.aoc.algorithms.Node;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Day8 extends Day {

    private static class Network {
        private Graph graph;
        private String currentNode;
        private String instructions;

        public Network() {
            this.graph = new Graph();
            this.instructions = "";
        }

        public static Network fromString(List<String> lines) {
            var network = new Network();
            network.instructions = lines.removeFirst();
            network.graph = graphFromStrings(lines);
            return network;
        }

        private long navigateFromTo(String from, String to) {
            String currentNode = from;
            char[] instructions = this.instructions.toCharArray();
            long steps = 0;
            while (true) {
                for (var instruction : instructions) {
                    if (instruction == 'L') {
                        currentNode = graph.getNeighbors(currentNode).get(0).name();
                    } else {
                        currentNode = graph.getNeighbors(currentNode).get(1).name();
                    }
                    steps++;
                }
                if (currentNode.endsWith(to)) {
                    break;
                }
            }
            return steps;
        }

        public long navigateToZZZ() {
            return navigateFromTo("AAA", "ZZZ");
        }

        public long navigateToZ() {
            List<String> nodeNames = graph.getNodeNames();
            List<Long> results = new ArrayList<>();
            var currentNodes = nodeNames.stream().filter(name -> name.endsWith("A")).toList();
            for (var currentNode : currentNodes) {
                results.add(navigateFromTo(currentNode, "Z"));
            }

            long steps = results.removeFirst();
            for (var result : results) {
                steps = MathUtils.lcm(steps, result);
            }

            return steps;
        }
    }

    private static Graph graphFromStrings(List<String> lines) {
        var graph = new Graph();
        var nodeMap = new HashMap<String, Node>();
        for (var line : lines) {
            if (!line.isEmpty()) {
                var tokens = line.split(" = ");
                var fromNode = new Node(tokens[0]);
                nodeMap.put(fromNode.name(), fromNode);
                var neighborTokens = tokens[1].replaceAll("\\(", "").replaceAll("\\)", "").split(", ");
                for (var neighborToken : neighborTokens) {
                    if (!nodeMap.containsKey(neighborToken)) {
                        nodeMap.put(neighborToken, new Node(neighborToken));
                    }
                    graph.insertNode(fromNode.name(), nodeMap.get(neighborToken));

                }
            }
        }
        return graph;
    }

    public Day8(Path path) {
        super(path);
    }

    @Override
    public Object part1() {
        try {
            var network = Network.fromString(this.readInput());
            return network.navigateToZZZ();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Object part2() {
        try {
            var network = Network.fromString(this.readInput());
            return network.navigateToZ();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
