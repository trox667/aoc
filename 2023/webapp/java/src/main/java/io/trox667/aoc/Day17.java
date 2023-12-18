package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Day17 extends Day {

    private record WalkInput(int px, int py, int x, int y, int sx, int sy) {}

    private static class IslandMap {
        private List<List<Long>> map;
        private HashMap<WalkInput, Long> memo;

        private IslandMap() {
            this.map = new ArrayList<>();
            this.memo = new HashMap<>();
        }

        public static IslandMap fromStrings(List<String> lines) {
            var islandMap = new IslandMap();
            for (var line : lines) {
                List<Long> row = new ArrayList<>();
                for (var c : line.toCharArray()) {
                    row.add((long)Character.digit(c, 10));
                }
                islandMap.map.add(row);
            }
            return islandMap;
        }

        public long walk(int px, int py, int x, int y, int sx, int sy) {
            if (y < 0 || y > this.map.size()-1) {
                return -1;
            }
            if (x < 0 || x > this.map.get(y).size()-1) {
                return -1;
            }

            if (sx > 3 || sy > 3) {
                return -1;
            }
            var input = new WalkInput(px, py, x, y, sx, sy);
            if (memo.containsKey(input)) {
                return memo.get(input);
            }

            var heatLoss = this.map.get(y).get(x);

            if (y == this.map.size()-1 && x == this.map.get(y).size()-1) {
                System.out.println("Found a path!");
                return 0;
            }

            if (x-1 != px) {
                var count = walk(x, y, x - 1, y, sx + 1, 0);
                if (count > 0) {
                    heatLoss += count;
                }
            }
            if (x+1 != px) {
                var count = walk(x, y, x + 1, y, sx + 1, 0);
                if (count > 0) {
                    heatLoss += count;
                }
            }
            if (y+1 != py) {
                var count = walk(x, y, x, y + 1, 0, sy + 1);
                if (count > 0) {
                    heatLoss += count;
                }
            }
            this.memo.put(input, heatLoss);
            return heatLoss;
        }
    }

    public Day17(Path path) {
        super(path);
    }

    @Override
    public Object part1() {
        try {
            var islandMap = IslandMap.fromStrings(this.readInput());
            islandMap.walk(0,0,0, 0, 0, 0);
            return null;
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Object part2() {
        return null;
    }
}
