package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Path;
import java.util.*;

public class Day14 extends Day {

    private static class Platform {
        private List<List<Character>> grid;

        public Platform() {
            grid = new ArrayList<>();
        }

        public void print() {
            for (var row : grid) {
                for (var c : row) {
                    System.out.print(c);
                }
                System.out.println();
            }
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Platform platform = (Platform) o;
            return Objects.equals(grid, platform.grid);
        }

        @Override
        public int hashCode() {
            return Objects.hash(grid);
        }

        public static Platform fromStrings(List<String> lines) {
            Platform platform = new Platform();
            for (String line : lines) {
                List<Character> row = new ArrayList<>();
                for (char c : line.toCharArray()) {
                    row.add(c);
                }
                platform.grid.add(row);
            }
            return platform;
        }

        // TODO: refactor these move methods to a rotate method
        public void moveNorth() {
            boolean move;
            do {
                move = false;
                for (var x = 0; x < grid.get(0).size(); x++) {
                    for (var y = 1; y < grid.size(); y++) {
                        if (grid.get(y - 1).get(x) == '.' && grid.get(y).get(x) == 'O') {
                            grid.get(y - 1).set(x, 'O');
                            grid.get(y).set(x, '.');
                            move = true;
                        }
                    }
                }
            } while (move);
        }

        public void moveWest() {
            boolean move;
            do {
                move = false;
                for (var y = 0; y < grid.size(); y++) {
                    for (var x = 1; x < grid.get(0).size(); x++) {
                        if (grid.get(y).get(x - 1) == '.' && grid.get(y).get(x) == 'O') {
                            grid.get(y).set(x - 1, 'O');
                            grid.get(y).set(x, '.');
                            move = true;
                        }
                    }
                }
            } while (move);
        }

        public void moveSouth() {
            boolean move;
            do {
                move = false;
                for (var x = 0; x < grid.get(0).size(); x++) {
                    for (var y = grid.size() - 2; y >= 0; y--) {
                        if (grid.get(y + 1).get(x) == '.' && grid.get(y).get(x) == 'O') {
                            grid.get(y + 1).set(x, 'O');
                            grid.get(y).set(x, '.');
                            move = true;
                        }
                    }
                }
            } while (move);
        }

        public void moveEast() {
            boolean move;
            do {
                move = false;
                for (var y = 0; y < grid.size(); y++) {
                    for (var x = grid.get(0).size() - 2; x >= 0; x--) {
                        if (grid.get(y).get(x + 1) == '.' && grid.get(y).get(x) == 'O') {
                            grid.get(y).set(x + 1, 'O');
                            grid.get(y).set(x, '.');
                            move = true;
                        }
                    }
                }
            } while (move);
        }

        public void cycle() {
            this.moveNorth();
            this.moveWest();
            this.moveSouth();
            this.moveEast();
        }

        public long getTotalLoad() {
            var result = 0L;
            for (var y = 0; y < grid.size(); y++) {
                var rowLoad = grid.size() - y;
                var rowCount = 0L;
                for (var x = 0; x < grid.get(0).size(); x++) {
                    if (grid.get(y).get(x) == 'O') {
                        rowCount++;
                    }
                }
                result += rowLoad * rowCount;
            }
            return result;
        }
    }

    public Day14(Path path) {
        super(path);
    }

    @Override
    public Object part1() {
        try {
            var platform = Platform.fromStrings(this.readInput());
            platform.moveNorth();
            return platform.getTotalLoad();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Object part2() {
        try {
            var platform = Platform.fromStrings(this.readInput());
            // history to detect cycles
            var history = new HashMap<Integer, Integer>();
            var historyValue = new HashMap<Integer, Long>();
            for (var i = 0; i < 1_000_000_000; i++) {
                platform.cycle();
                var hash = platform.hashCode();
                if (history.containsKey(hash)) {
                    // cycle detected
                    var idx = history.get(hash); // start of cycle
                    // calculate final index
                    // idx = 2
                    // cycle length = 7
                    var finalIdx = (idx + (1_000_000_000 - idx) % (history.size() - idx)) - 1;
                    return historyValue.get(finalIdx);
                } else {
                    history.put(hash, i);
                    historyValue.put(i, platform.getTotalLoad());
                }
            }
            return null;
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
