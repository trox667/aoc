package io.trox667.aoc;

import io.trox667.aoc.algorithms.MathUtils;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Day11 extends Day {

    private record Coordinate(Long x, Long y) {
    }

    private record Galaxy(Long index, Coordinate position) {
    }

    private record GalaxyPair(Galaxy a, Galaxy b) {
        public Long distance() {
            return MathUtils.manhattanDistance(a.position.x, a.position.y, b.position.x, b.position.y);
        }
    }

    private static class Image {
        private final List<Galaxy> galaxies;

        private Image() {
            galaxies = new ArrayList<>();
        }

        public static Image fromStrings(List<String> lines, long expand) {
            var image = new Image();
            var rows = lines.stream().filter(line -> !line.isEmpty()).toList();
            var emptyLinesHorizontally = new ArrayList<Integer>();
            var emptyLinesVertically = new ArrayList<Integer>();
            // expand space horizontally
            for (var i = 0; i < rows.size(); i++) {
                if (!rows.get(i).contains("#")) {
                    emptyLinesHorizontally.add(i);
                }
            }
            // expand space vertically
            for (var x = 0; x < rows.get(0).length(); x++) {
                var columnHasNoGalaxy = true;
                for (var y = 0; y < rows.size(); y++) {
                    if (rows.get(y).charAt(x) == '#') {
                        columnHasNoGalaxy = false;
                        break;
                    }
                }
                if (columnHasNoGalaxy) {
                    emptyLinesVertically.add(x);
                }
            }

            var index = 1L;
            for (var y = 0; y < rows.size(); y++) {
                for (var x = 0; x < rows.get(y).length(); x++) {
                    if (rows.get(y).charAt(x) == '#') {
                        var countSpaceBefore = 0L;
                        var countSpaceAbove = 0L;
                        for (var i = 0; i < emptyLinesHorizontally.size(); i++) {
                            if (emptyLinesHorizontally.get(i) < y) {
                                countSpaceAbove++;
                            }
                        }
                        for (var i = 0; i < emptyLinesVertically.size(); i++) {
                            if (emptyLinesVertically.get(i) < x) {
                                countSpaceBefore++;
                            }
                        }
                        var xInSpace = x + countSpaceBefore * expand - countSpaceBefore;
                        var yInSpace = y + countSpaceAbove * expand - countSpaceAbove;
                        image.galaxies.add(new Galaxy(index++, new Coordinate((long)xInSpace, (long)yInSpace)));
                    }
                }
            }

            return image;
        }

        private List<GalaxyPair> getPairs() {
            var pairs = new ArrayList<GalaxyPair>();
            for (var i = 0; i < galaxies.size(); i++) {
                for (var j = i + 1; j < galaxies.size(); j++) {
                    pairs.add(new GalaxyPair(galaxies.get(i), galaxies.get(j)));
                }
            }
            return pairs;
        }

        public Long sumOfShortestPaths() {
            return getPairs().stream().map(GalaxyPair::distance).reduce(0L, Long::sum);
        }
    }

    public Day11(Path path) {
        super(path);
    }

    @Override
    public Object part1() {
        try {
            var image = Image.fromStrings(this.readInput(), 2);
            return image.sumOfShortestPaths();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Object part2() {
        try {
            var image = Image.fromStrings(this.readInput(), 1000000);
            return image.sumOfShortestPaths();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
