package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.LongStream;

public class Day6 extends Day {

    private static class RaceDocument {
        private List<Long> times;
        private List<Long> distances;

        public RaceDocument() {
            times = new ArrayList<>();
            distances = new ArrayList<>();
        }

        public static RaceDocument fromStrings(List<String> lines) {
            assert lines.size() >= 2;
            var raceDocument = new RaceDocument();
            var times = Arrays.stream(lines.get(0).split(": ")[1].trim().split(" ")).filter(s -> !s.isEmpty()).map(Long::parseLong).toList();
            var distances = Arrays.stream(lines.get(1).split(": ")[1].trim().split(" ")).filter(s -> !s.isEmpty()).map(Long::parseLong).toList();
            raceDocument.times = times;
            raceDocument.distances = distances;
            return raceDocument;
        }

        public static RaceDocument fromStringsOneRace(List<String> lines) {
            assert lines.size() >= 2;
            var raceDocument = new RaceDocument();
            var time = Long.parseLong(lines.get(0).split(": ")[1].trim().replaceAll(" ", ""));
            var distance = Long.parseLong(lines.get(1).split(": ")[1].trim().replaceAll(" ", ""));
            raceDocument.times.add(time);
            raceDocument.distances.add(distance);
            return raceDocument;
        }

        public long solve() {
            assert times.size() == distances.size();
            var result = 1L;
            for (var i = 0; i < times.size(); i++) {
                // x * (time - x) > distance
                // x^2 - time * x > distance
                var b = times.get(i) / 2.0;
                var d = Math.sqrt(b * b - distances.get(i));
                result *= (Math.ceil(b + d - 1L) - Math.floor(b - d + 1L) + 1L);
            }
            return result;
        }

        public long getMultipliedNumberOfWaysToBeatTheRecords() {
            assert times.size() == distances.size();
            var result = 1L;
            for (var i = 0; i < times.size(); i++) {
                var time = times.get(i);
                var distance = distances.get(i);
                result *= LongStream.range(1, time).map(speed -> (time - speed) * speed).filter(pd -> pd > distance).count();
            }
            return result;
        }
    }

    public Day6(Path path) {
        super(path);
    }

    @Override
    public Object part1() {
        try {
            var raceDocument = RaceDocument.fromStrings(readInput());
            return raceDocument.solve();
//            return raceDocument.getMultipliedNumberOfWaysToBeatTheRecords();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Object part2() {
        try {
            var raceDocument = RaceDocument.fromStringsOneRace(readInput());
            return raceDocument.solve();
//            return raceDocument.getMultipliedNumberOfWaysToBeatTheRecords();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
