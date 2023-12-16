package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class Day16 extends Day {
    private enum Direction {
        UNKNOWN, UP, DOWN, LEFT, RIGHT
    }

    private record Coordinate(int x, int y) {
    }

    private record Tile(int x, int y) {
    }

    private record MemoKey(Coordinate c, Direction d) {
    }

    private static class Contraption {
        private List<String> layout;
        private HashSet<Tile> energizedTiles;
        private HashSet<MemoKey> memo;

        private Contraption() {
            layout = new ArrayList<>();
            energizedTiles = new HashSet<>();
            memo = new HashSet<>();
        }

        private Contraption(Contraption c) {
            this.layout = new ArrayList<>(c.layout);
            this.energizedTiles = new HashSet<>();
            memo = new HashSet<>();
        }

        public static Contraption fromStrings(List<String> lines) {
            Contraption contraption = new Contraption();
            contraption.layout = lines;
            return contraption;
        }

        public void walk(Coordinate p, Coordinate n) {
            if (n.y >= layout.size() || n.y < 0) {
                return;
            }
            if (n.x >= layout.get(n.y).length() || n.x < 0) {
                return;
            }
            energizedTiles.add(new Tile(n.x, n.y));

            var tile = layout.get(n.y).charAt(n.x);
            var direction = Direction.UNKNOWN;
            if (p.x < n.x) {
                direction = Direction.RIGHT;
            }
            if (p.x > n.x) {
                direction = Direction.LEFT;
            }
            if (p.y < n.y) {
                direction = Direction.DOWN;
            }
            if (p.y > n.y) {
                direction = Direction.UP;
            }
            if (p.x == 0 && p.x == p.y && p.x == n.x && p.x == n.y) {
                direction = Direction.RIGHT;
            }

            if (memo.contains(new MemoKey(n, direction))) {
                return;
            }

            var steps = nextSteps(tile, n, direction);
            memo.add(new MemoKey(n, direction));
            for (var step : steps) {
                walk(n, step);
            }
        }

        private List<Coordinate> nextSteps(char tile, Coordinate c, Direction d) {
            var steps = new ArrayList<Coordinate>();
            switch (tile) {
                case '.' -> {
                    switch (d) {
                        case UP -> steps.add(new Coordinate(c.x, c.y - 1));
                        case DOWN -> steps.add(new Coordinate(c.x, c.y + 1));
                        case LEFT -> steps.add(new Coordinate(c.x - 1, c.y));
                        case RIGHT -> steps.add(new Coordinate(c.x + 1, c.y));
                    }
                }
                case '|' -> {
                    switch (d) {
                        case UP -> steps.add(new Coordinate(c.x, c.y - 1));
                        case DOWN -> steps.add(new Coordinate(c.x, c.y + 1));
                        case LEFT, RIGHT -> {
                            steps.add(new Coordinate(c.x, c.y - 1));
                            steps.add(new Coordinate(c.x, c.y + 1));
                        }
                    }
                }
                case '-' -> {
                    switch (d) {
                        case UP, DOWN -> {
                            steps.add(new Coordinate(c.x - 1, c.y));
                            steps.add(new Coordinate(c.x + 1, c.y));
                        }
                        case LEFT -> steps.add(new Coordinate(c.x - 1, c.y));
                        case RIGHT -> steps.add(new Coordinate(c.x + 1, c.y));
                    }
                }
                case '\\' -> {
                    switch (d) {
                        case UP -> steps.add(new Coordinate(c.x - 1, c.y));
                        case DOWN -> steps.add(new Coordinate(c.x + 1, c.y));
                        case LEFT -> steps.add(new Coordinate(c.x, c.y - 1));
                        case RIGHT -> steps.add(new Coordinate(c.x, c.y + 1));
                    }
                }
                case '/' -> {
                    switch (d) {
                        case UP -> steps.add(new Coordinate(c.x + 1, c.y));
                        case DOWN -> steps.add(new Coordinate(c.x - 1, c.y));
                        case LEFT -> steps.add(new Coordinate(c.x, c.y + 1));
                        case RIGHT -> steps.add(new Coordinate(c.x, c.y - 1));
                    }
                }
            }

            return steps;
        }

        public void reset() {
            energizedTiles.clear();
            memo.clear();
        }

        public int countEnergizedTiles() {
            return energizedTiles.size();
        }

        public int findMostEnergizedStart() {
            var count = Integer.MIN_VALUE;
            // TOP to BOTTOM
            for (var x = 0; x < layout.get(0).length(); x++) {
                walk(new Coordinate(x, -1), new Coordinate(x, 0));
                count = Math.max(count, countEnergizedTiles());
//                printLayout();
                reset();

                walk(new Coordinate(x, layout.size()), new Coordinate(x, layout.size() - 1));
                count = Math.max(count, countEnergizedTiles());
                reset();
            }

            for (var y = 0; y < layout.size(); y++) {
                walk(new Coordinate(-1, y), new Coordinate(0, y));
                count = Math.max(count, countEnergizedTiles());
                reset();

                walk(new Coordinate(layout.get(0).length(), y), new Coordinate(layout.get(0).length() - 1, y));
                count = Math.max(count, countEnergizedTiles());
                reset();
            }
            return count;
        }

        private void printLayout() {
            for (var y = 0; y < layout.size(); y++) {
                for (var x = 0; x < layout.get(y).length(); x++) {
                    if (energizedTiles.contains(new Tile(x, y))) {
                        System.out.print("#");
                    } else {
                        System.out.print(layout.get(y).charAt(x));
                    }
                }
                System.out.println();
            }
        }
    }

    public Day16(Path path) {
        super(path);
    }

    private int findMostEnergizedStart(List<String> lines) {
        var contraption = Contraption.fromStrings(lines);
        var count = Integer.MIN_VALUE;
        ExecutorService service = Executors.newVirtualThreadPerTaskExecutor();
        List<Future<Integer>> futures = new ArrayList<>();
        // TOP to BOTTOM
        for (var x = 0; x < contraption.layout.get(0).length(); x++) {
            int finalX = x;
            futures.add(service.submit(() -> {
                var c = new Contraption(contraption);
                c.walk(new Coordinate(finalX, -1), new Coordinate(finalX, 0));
                return c.countEnergizedTiles();
            }));
            futures.add(service.submit(() -> {
                var c = new Contraption(contraption);
                c.walk(new Coordinate(finalX, c.layout.size()), new Coordinate(finalX, c.layout.size() - 1));
                return c.countEnergizedTiles();
            }));
        }
        for (var y = 0; y < contraption.layout.size(); y++) {
            int finalY = y;
            futures.add(service.submit(() -> {
                var c = new Contraption(contraption);
                c.walk(new Coordinate(-1, finalY), new Coordinate(0, finalY));
                return c.countEnergizedTiles();
            }));
            futures.add(service.submit(() -> {
                var c = new Contraption(contraption);
                c.walk(new Coordinate(c.layout.get(0).length(), finalY), new Coordinate(c.layout.get(0).length() - 1, finalY));
                return c.countEnergizedTiles();
            }));
        }

        for (var result : futures) {
            try {
                count = Math.max(result.get(), count);
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        }

        return count;
    }

    @Override
    public Object part1() {
        try {
            Contraption contraption = Contraption.fromStrings(this.readInput());
            contraption.walk(new Coordinate(-1, 0), new Coordinate(0, 0));
            return contraption.countEnergizedTiles();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Object part2() {
        try {
//            Contraption contraption = Contraption.fromStrings(this.readInput());
//            return contraption.findMostEnergizedStart();
            return findMostEnergizedStart(this.readInput());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
