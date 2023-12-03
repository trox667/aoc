package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Path;
import java.util.*;

public class Day3 extends Day {

    private record Coordinate(int x, int y) {}

    private static class Engine {
        private List<char[]> map;

        public Engine() {
            map = new ArrayList<>();
        }

        public void addRowToMap(String row) {
            map.add(row.toCharArray());
        }

        public char getValue(int x, int y) {
            if (y < 0 || y >= map.size()) {
                return '.';
            }
            if (x < 0 || x >= map.get(y).length) {
                return '.';
            }
            return map.get(y)[x];
        }

        public int getHeight() {
            return map.size();
        }

        public int getRowWidth(int row) {
            return map.get(row).length;
        }

        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder();
            for (char[] row : map) {
                sb.append(Arrays.toString(row)).append("\n");
            }
            return sb.toString();
        }
    }

    private static class EngineScanner {
        private final Engine engine;
        private int x = 0;
        private int y = 0;
        private List<Character> currentValue;

        public EngineScanner(final Engine engine) {
            this.engine = engine;
            this.currentValue = new ArrayList<>();
        }

        public List<Integer> scan() {
            var result = new ArrayList<Integer>();
            var hasSymbol = false;
            for (y = 0; y < engine.getHeight(); y++) {
                for (x = 0; x < engine.getRowWidth(y); x++) {
                    if (isFieldDigit()) {
                        currentValue.add(engine.getValue(x, y));
                        if (hasSymbolAsNeighbour()) {
                            hasSymbol = true;
                        }
                    } else {
                        if (hasSymbol && !currentValue.isEmpty()) {
                            result.add(Integer.parseInt(currentValue.stream().map(c -> c.toString()).reduce((a, b) -> a + b).get()));
                        }
                        currentValue = new ArrayList<>();
                        hasSymbol = false;
                    }
                }
            }
            return result;
        }

        public List<Integer> scanGears() {
            var result = new ArrayList<Integer>();

            var gearMap = new HashMap<Coordinate, List<Integer>>();
            Coordinate gearPosition = null;
            for (y = 0; y < engine.getHeight(); y++) {
                for (x = 0; x < engine.getRowWidth(y); x++) {
                    if (isFieldDigit()) {
                        currentValue.add(engine.getValue(x, y));
                        var potentialGearPosition = hasGearAsNeighbour();
                        if (potentialGearPosition.isPresent()) {
                            gearPosition = potentialGearPosition.get();
                        }
                    } else {
                        if (gearPosition != null && !currentValue.isEmpty()) {
                            var list = gearMap.get(gearPosition);
                            if (list == null) {
                                list = new ArrayList<>();
                            }
                            list.add(Integer.parseInt(currentValue.stream().map(c -> c.toString()).reduce((a, b) -> a + b).get()));
                            gearMap.put(gearPosition, list);
                            gearPosition = null;
                        }
                        currentValue = new ArrayList<>();
                    }
                }
            }
            gearMap.values().stream().filter(list -> list.size() == 2).map(list -> list.stream().reduce(1, (a,b) -> a * b)).forEach(result::add);
            return result;
        }

        private boolean isFieldDigit() {
            var value = engine.getValue(x, y);
            return value != '.' && Character.isDigit(value);
        }

        private boolean isFieldGear(int x, int y) {
            var value = engine.getValue(x, y);
            return value == '*';
        }

        private boolean hasSymbolAsNeighbour() {
            for (var cy = y - 1; cy <= y + 1; cy++) {
                for (var cx = x - 1; cx <= x + 1; cx++) {
                    // skip self
                    if (cx == 0 && cy == 0) {
                        continue;
                    }
                    var neighbour = engine.getValue(cx, cy);
                    if (neighbour != '.' && !Character.isDigit(neighbour)) {
                        return true;
                    }
                }
            }
            return false;
        }

        private Optional<Coordinate> hasGearAsNeighbour() {
            for (var cy = y - 1; cy <= y + 1; cy++) {
                for (var cx = x - 1; cx <= x + 1; cx++) {
                    // skip self
                    if (cx == 0 && cy == 0) {
                        continue;
                    }
                    var neighbour = engine.getValue(cx, cy);
                    if (isFieldGear(cx, cy)) {
                        return Optional.of(new Coordinate(cx, cy));
                    }
                }
            }
            return Optional.empty();
        }
    }

    public Day3(Path path) {
        super(path);
    }

    @Override
    public Object part1() {
        try {
            var engine = new Engine();
            this.readInput().stream().forEach(engine::addRowToMap);
            var engineScanner = new EngineScanner(engine);
            var results = engineScanner.scan();
            return results.stream().reduce(0, Integer::sum);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Object part2() {
        try {
            var engine = new Engine();
            this.readInput().stream().forEach(engine::addRowToMap);
            var engineScanner = new EngineScanner(engine);
            var results = engineScanner.scanGears();
            return results.stream().reduce(0, Integer::sum);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
