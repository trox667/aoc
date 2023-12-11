package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Path;
import java.util.*;
import java.util.stream.IntStream;

public class Day10 extends Day {

    private static final class Neighbours {
        public Optional<Coordinate> left;
        public Optional<Coordinate> right;
        public Optional<Coordinate> up;
        public Optional<Coordinate> down;

        private Neighbours(Optional<Coordinate> left, Optional<Coordinate> right, Optional<Coordinate> up, Optional<Coordinate> down) {
            this.left = left;
            this.right = right;
            this.up = up;
            this.down = down;
        }
    }

    private record Coordinate(int x, int y) {
    }

    private static class Maze {
        private final List<char[]> maze;
        private Coordinate start;
        private HashSet<Coordinate> path;
        private List<Coordinate> loop;

        private Maze() {
            maze = new ArrayList<>();
            this.path = new HashSet<>();
            this.loop = new ArrayList<>();
            start = null;
        }

        private void addRow(String row) {
            if (row.indexOf('S') != -1 && start == null) {
                start = new Coordinate(row.indexOf('S'), maze.size());
            }
            maze.add(row.toCharArray());
        }

        public static Maze fromStrings(List<String> lines) {
            var maze = new Maze();
            lines.stream().filter(line -> !line.isEmpty()).forEach(line -> maze.addRow(line));
            maze.findLoop();
            return maze;
        }

        public void print(List<Coordinate> loop) {
            for (var y = 0; y < maze.size(); y++) {
                for (var x = 0; x < maze.get(y).length; x++) {
                    if (path.contains(new Coordinate(x, y))) {
                        System.out.print(maze.get(y)[x]);
                    } else {
                        System.out.print('.');
                    }
                }
                System.out.print("\n");
            }
        }

        public void print(HashSet<Coordinate> encircled) {
            for (var y = 0; y < maze.size(); y++) {
                for (var x = 0; x < maze.get(y).length; x++) {
                    if (encircled.contains(new Coordinate(x, y))) {
                        System.out.print('I');
                    } else {
                        System.out.print('.');
                    }
                }
                System.out.print("\n");
            }
        }

        private List<Coordinate> findLoop() {
            var current = start;
            while (current != null) {
                loop.add(current);
                path.add(current);
                current = findNext(current, path);
            }
            return loop;
        }

        public int getDistance() {
            return loop.size() / 2;
        }

        public int countEncircled() {
            var possiblyEncircled = new HashSet<Coordinate>();
//            for (var i = 1; i < loop.size() - 1; i++) {
//                var coordinate = loop.get(i - 1);
//                var nextCoordinate = loop.get(i);
//
//            }

            for (var y = 0; y < maze.size(); y++) {
                for (var x = 0; x < maze.get(y).length; x++) {
                    var tile = maze.get(y)[x];
                    if ((x == 0 || y == 0 || x == maze.get(y).length-1 || y == maze.size()-1) && tile == '.') {
                        continue;
                    }
                    var coordinate = new Coordinate(x, y);
                    if (!path.contains(coordinate)) {
                        if (intersect(coordinate)) {
                            possiblyEncircled.add(coordinate);
                        }
                    }
                }
            }

            print(possiblyEncircled);
            return possiblyEncircled.size();
        }

        private boolean intersect(Coordinate coordinate) {
            var countIntersectionsX = 0;
            var countPipe = 0;
            for (var x = coordinate.x; x < maze.get(coordinate.y).length; x++) {
                if (path.contains(new Coordinate(x, coordinate.y))) {
                    var tile = maze.get(coordinate.y)[x];
                    if (tile == '-') {
                        countPipe++;
                    }
                    countIntersectionsX++;
                }
            }

            return (countIntersectionsX-countPipe) % 2 == 1;
        }

        private Coordinate findNext(Coordinate current, HashSet<Coordinate> path) {
            var pipe = maze.get(current.y)[current.x];
            var possibleNeighbours = possibleNeighbours(getNeighbours(current), pipe);
            if (possibleNeighbours.up.isPresent() && !path.contains(possibleNeighbours.up.get())) {
                return possibleNeighbours.up.get();
            } else if (possibleNeighbours.right.isPresent() && !path.contains(possibleNeighbours.right.get())) {
                return possibleNeighbours.right.get();
            } else if (possibleNeighbours.left.isPresent() && !path.contains(possibleNeighbours.left.get())) {
                return possibleNeighbours.left.get();
            } else if (possibleNeighbours.down.isPresent() && !path.contains(possibleNeighbours.down.get())) {
                return possibleNeighbours.down.get();
            }
            return null;
        }

        private Neighbours getNeighbours(Coordinate current) {
            var neighbours = new Neighbours(Optional.empty(), Optional.empty(), Optional.empty(), Optional.empty());
            if (current.x > 0) {
                if (maze.get(current.y)[current.x - 1] != '.') {
                    neighbours.left = Optional.of(new Coordinate(current.x - 1, current.y));
                }
            }
            if (current.x < maze.get(current.y).length - 1) {
                if (maze.get(current.y)[current.x + 1] != '.') {
                    neighbours.right = Optional.of(new Coordinate(current.x + 1, current.y));
                }
            }
            if (current.y > 0) {
                if (maze.get(current.y - 1)[current.x] != '.') {
                    neighbours.up = Optional.of(new Coordinate(current.x, current.y - 1));
                }
            }
            if (current.y < maze.size() - 1) {
                if (maze.get(current.y + 1)[current.x] != '.') {
                    neighbours.down = Optional.of(new Coordinate(current.x, current.y + 1));
                }
            }
            return neighbours;
        }

        private Neighbours possibleNeighbours(Neighbours neighbours, char pipe) {
            var possibleNeighbours = new Neighbours(Optional.empty(), Optional.empty(), Optional.empty(), Optional.empty());
            switch (pipe) {
                case 'S' -> {
                    if (neighbours.up.isPresent()) {
                        var value = maze.get(neighbours.up.get().y)[neighbours.up.get().x];
                        if (value != 'L' && value != '7') {
                            possibleNeighbours.up = neighbours.up;
                        }
                    }
                    if (neighbours.right.isPresent()) {
                        var value = maze.get(neighbours.right.get().y)[neighbours.right.get().x];
                        if (value != 'L' && value != 'F' && value != '|') {
                            possibleNeighbours.right = neighbours.right;
                        }
                    }
                    if (neighbours.down.isPresent()) {
                        var value = maze.get(neighbours.down.get().y)[neighbours.down.get().x];
                        if (value != '-' && value != '7' && value != 'F') {
                            possibleNeighbours.down = neighbours.down;
                        }
                    }
                    if (neighbours.left.isPresent()) {
                        var value = maze.get(neighbours.left.get().y)[neighbours.left.get().x];
                        if (value != 'J' && value != '7' && value != '|') {
                            possibleNeighbours.left = neighbours.left;
                        }
                    }
                }
                case '|' -> {
                    if (neighbours.up.isPresent()) {
                        possibleNeighbours.up = neighbours.up;
                    }
                    if (neighbours.down.isPresent()) {
                        possibleNeighbours.down = neighbours.down;
                    }
                }
                case '-' -> {
                    if (neighbours.left.isPresent()) {
                        possibleNeighbours.left = neighbours.left;
                    }
                    if (neighbours.right.isPresent()) {
                        possibleNeighbours.right = neighbours.right;
                    }
                }
                case 'L' -> {
                    if (neighbours.right.isPresent()) {
                        possibleNeighbours.right = neighbours.right;
                    }
                    if (neighbours.up.isPresent()) {
                        possibleNeighbours.up = neighbours.up;
                    }
                }
                case 'J' -> {
                    if (neighbours.left.isPresent()) {
                        possibleNeighbours.left = neighbours.left;
                    }
                    if (neighbours.up.isPresent()) {
                        possibleNeighbours.up = neighbours.up;
                    }
                }
                case '7' -> {
                    if (neighbours.left.isPresent()) {
                        possibleNeighbours.left = neighbours.left;
                    }
                    if (neighbours.down.isPresent()) {
                        possibleNeighbours.down = neighbours.down;
                    }
                }
                case 'F' -> {
                    if (neighbours.right.isPresent()) {
                        possibleNeighbours.right = neighbours.right;
                    }
                    if (neighbours.down.isPresent()) {
                        possibleNeighbours.down = neighbours.down;
                    }
                }
            }
            return possibleNeighbours;
        }
    }

    public Day10(Path path) {
        super(path);
    }

    @Override
    public Object part1() {
        try {
            var maze = Maze.fromStrings(this.readInput());
            return maze.getDistance();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Object part2() {
        try {
            var maze = Maze.fromStrings(this.readInput());
            return maze.countEncircled();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
