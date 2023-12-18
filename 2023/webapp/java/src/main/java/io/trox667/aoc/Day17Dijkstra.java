package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Objects;

public class Day17Dijkstra extends Day {
    private record Coordinate(int x, int y) {
    }

    private static final class Node {
        private final Coordinate coordinate;
        private int heatLoss;

        private Node(Coordinate coordinate, int heatLoss) {
            this.coordinate = coordinate;
            this.heatLoss = heatLoss;
        }

        public Coordinate coordinate() {
            return coordinate;
        }

        public int heatLoss() {
            return heatLoss;
        }

        public void setHeatLoss(int heatLoss) {
            this.heatLoss = heatLoss;
        }

        @Override
        public boolean equals(Object obj) {
            if (obj == this) return true;
            if (obj == null || obj.getClass() != this.getClass()) return false;
            var that = (Node) obj;
            return Objects.equals(this.coordinate, that.coordinate) &&
                    this.heatLoss == that.heatLoss;
        }

        @Override
        public int hashCode() {
            return Objects.hash(coordinate, heatLoss);
        }

    }

    private static class Graph {
        private int width;
        private int height;

        public Graph(int width, int height) {
            this.width = width;
            this.height = height;
        }

        public List<Coordinate> getNeighbors(Coordinate current, Coordinate previous, int sx, int sy) {
            var coordinates = new ArrayList<Coordinate>();
            // cannot go reverse and not more than 3 blocks straight
            if (previous.x != current.x - 1) {
                coordinates.add(new Coordinate(current.x - 1, current.y));
            }
            if (previous.x != current.x + 1) {
                coordinates.add(new Coordinate(current.x + 1, current.y));

            }
            if (previous.y != current.y - 1) {
                coordinates.add(new Coordinate(current.x, current.y - 1));
            }
            if (previous.y != current.y + 1) {
                coordinates.add(new Coordinate(current.x, current.y + 1));
            }
            return coordinates;
        }

    }

    private static class Dijkstra {
        List<Node> unvisited;
        HashMap<Coordinate, Node> pathMap;
        private Graph graph;
        private IslandMap islandMap;

        public Dijkstra(IslandMap islandMap) {
            this.unvisited = new ArrayList<>();
            this.pathMap = new HashMap<>();
            this.islandMap = islandMap;
            this.graph = new Graph(islandMap.map.get(0).size(), islandMap.map.size());
        }

        public long findShortestPath() {
            this.run();
            var path = new ArrayList<Node>();
            var current = new Coordinate(this.graph.width - 1, this.graph.height - 1);
            while (current != null) {
                if (this.pathMap.containsKey(current)) {
                    path.add(0, this.pathMap.get(current));
                    current = this.pathMap.get(current).coordinate();
                } else {
                    current = null;
                }
            }
            return path.stream().map(Node::heatLoss).reduce(0, Integer::sum);
        }

        private Node getNextNode() {
            this.unvisited.sort((a, b) -> a.heatLoss() - b.heatLoss());
            return this.unvisited.removeFirst();
        }

        private void run() {
            var previous = new Coordinate(-1, -1);
            var sx = 0;
            var sy = 0;
            var start = new Coordinate(0, 0);
            var end = new Coordinate(this.graph.width - 1, this.graph.height - 1);
            for (var y = 0; y < this.graph.height; y++) {
                for (var x = 0; x < this.graph.width; x++) {
                    var c = new Coordinate(x, y);
                    if (start == c) {
                        this.unvisited.add(new Node(c, 0));
                    } else {
                        this.unvisited.add(new Node(c, Integer.MAX_VALUE));
                    }
                }
            }

            while (!this.unvisited.isEmpty()) {
                var current = getNextNode();
                if (current.coordinate().equals(end)) {
                    break;
                }

                var neighbors = this.graph.getNeighbors(current.coordinate, previous, sx, sy);
//                for (var neighbor : neighbors) {
//                    if (neighbor.x != previous.x) {
//                        sx++;
//                        break;
//                    }
//                }
//                for (var neighbor : neighbors) {
//                    if (neighbor.y != previous.y) {
//                        sy++;
//                        break;
//                    }
//                }
                for (var neighbor : neighbors) {
                    for (var unvisitedNode : this.unvisited) {
                        if (unvisitedNode.coordinate().equals(neighbor)) {
                            var heatLoss = current.heatLoss() + this.islandMap.map.get(neighbor.y).get(neighbor.x);
                            if (heatLoss < unvisitedNode.heatLoss()) {
                                unvisitedNode.setHeatLoss(heatLoss);
                                pathMap.put(neighbor, current);
                            }
                            break;
                        }
                    }
                }
                if (sx > 3) {
                    sx = 0;
                }
                if (sy > 3) {
                    sy = 0;
                }
            }
        }
    }

    private static class IslandMap {
        private List<List<Integer>> map;

        private IslandMap() {
            this.map = new ArrayList<>();
        }

        public static IslandMap fromStrings(List<String> lines) {
            var islandMap = new IslandMap();
            for (var line : lines) {
                List<Integer> row = new ArrayList<>();
                for (var c : line.toCharArray()) {
                    row.add(Character.digit(c, 10));
                }
                islandMap.map.add(row);
            }
            return islandMap;
        }

    }

    public Day17Dijkstra(Path path) {
        super(path);
    }

    @Override
    public Object part1() {
        try {
            var islandMap = IslandMap.fromStrings(this.readInput());
            var dijkstra = new Dijkstra(islandMap);
            return dijkstra.findShortestPath();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Object part2() {
        return null;
    }
}
