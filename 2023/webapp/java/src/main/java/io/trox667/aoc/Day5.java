package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Path;
import java.util.*;

public class Day5 extends Day {

    private static enum Maps {
        SOIL, FERTILIZER, WATER, LIGHT, TEMPERATURE, HUMIDITY, LOCATION
    }

    private static class Almanac {
        private List<Long> seeds;
        private List<SeedRange> seedRanges;
        private List<AnyToAnyMap> maps;

        public Almanac() {
            this.maps = new ArrayList<>();
            this.seedRanges = new ArrayList<>();
        }

        public static Almanac fromStrings(List<String> lines) {
            var almanac = new Almanac();
            var currMap = new AnyToAnyMap();
            var init = true;
            for (var line : lines) {
                if (line.startsWith("seeds: ")) {
                    almanac.seeds = Arrays.stream(line.split(": ")[1].split(" ")).map(Long::parseLong).toList();
                    for (var i = 0; i < almanac.seeds.size()-1; i+=2) {
                        almanac.seedRanges.add(new SeedRange(almanac.seeds.get(i), almanac.seeds.get(i+1)));
                    }

                } else if (!line.isEmpty() && !line.isBlank()) {
                    if (line.contains(":")) {
                        if (!init) {
                            almanac.maps.add(currMap);
                        } else {
                            init = false;
                        }
                        currMap = new AnyToAnyMap();
                    } else {
                        currMap.addLine(line);
                    }
                }
            }
            almanac.maps.add(currMap);
            return almanac;
        }

        public long getMinLocationForSeeds() {
            var minLocation = Long.MAX_VALUE;
            for (var seed : seeds) {
                minLocation = Math.min(minLocation, getLocationForSeed(seed));
            }
            return minLocation;
        }

        public long getMinLocationForSeedRanges() {
            var minLocation = Long.MAX_VALUE;
            for (var seedRange : seedRanges) {
                for (var seed = seedRange.source; seed < seedRange.source + seedRange.range; seed++) {
                    minLocation = Math.min(minLocation, getLocationForSeed(seed));
                }
            }
            return minLocation;
        }

        public long getLocationForSeed(long seed) {
            var curr_value = seed;
            for (var map : this.maps) {
                curr_value = map.getValue(curr_value);
            }
            return curr_value;
        }
    }

    private static record AnyRange(long destination, long source, long range) {
    }
    private static record SeedRange(long source, long range) {}

    private static class AnyToAnyMap {
        private List<AnyRange> ranges;

        public AnyToAnyMap() {
            this.ranges = new ArrayList<>();
        }

        public void addLine(String line) {
            var tokens = line.split(" ");
            var destinationStart = Long.parseLong(tokens[0]);
            var sourceStart = Long.parseLong(tokens[1]);
            var range = Long.parseLong(tokens[2]);
            this.ranges.add(new AnyRange(destinationStart, sourceStart, range));
        }

        public long getValue(Long source) {
            for (var range : this.ranges) {
                if (source >= range.source && source < range.source + range.range) {
                    return range.destination + (source - range.source);
                }
            }
            return source;
        }
    }

    public Day5(Path path) {
        super(path);
    }

    @Override
    public Object part1() {
        try {
            var lines = this.readInput();
            var almanac = Almanac.fromStrings(lines);
            return almanac.getMinLocationForSeeds() ;
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Object part2() { try {
        var lines = this.readInput();
        var almanac = Almanac.fromStrings(lines);
        return almanac.getMinLocationForSeedRanges();
    } catch (IOException e) {
        throw new RuntimeException(e);
    }
    }
}
