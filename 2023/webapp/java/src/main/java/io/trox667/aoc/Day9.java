package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.LongStream;

public class Day9 extends Day {

    private static class Values {
        private List<Long> values;

        public Values(List<Long> values) {
            this.values = values;
        }

        public Values differences() {
            var newValues = new ArrayList<Long>();

            for (var i = 0; i < values.size() - 1; i++) {
                var a = values.get(i + 1);
                var b = values.get(i);
                newValues.add(a - b);
            }

            return new Values(newValues);
        }

        public boolean isZero() {
            return values.stream().allMatch(v -> v == 0);
        }
    }

    private static class HistoryEntry {
        private Values history;

        private HistoryEntry() {
            this.history = null;
        }

        public static HistoryEntry fromString(String line) {
            var entry = new HistoryEntry();
            entry.history = new Values(Arrays.stream(line.split(" ")).map(Long::parseLong).toList());
            return entry;
        }

        public Values differences() {
            var newValues = new ArrayList<Long>();

            for (var i = 0; i < history.values.size() - 1; i++) {
                var a = history.values.get(i + 1);
                var b = history.values.get(i);
                newValues.add(a - b);
            }

            return new Values(newValues);
        }
    }

    private static class OASISReport {
        private List<HistoryEntry> historyEntries;

        private OASISReport() {
            this.historyEntries = new ArrayList<>();
        }

        public static OASISReport fromStrings(List<String> lines) {
            var report = new OASISReport();

            for (var line : lines) {
                if (line.isEmpty() || line.isBlank()) {
                    continue;
                }
                report.historyEntries.add(HistoryEntry.fromString(line));
            }

            return report;
        }

        private List<Values> getStepsToZero(HistoryEntry historyEntry) {
            List<Values> steps = new ArrayList<>();
            steps.add(historyEntry.history);
            steps.add(historyEntry.differences());
            while (!steps.getLast().isZero()) {
                steps.add(steps.getLast().differences());
            }
            return steps;
        }

        public long sumOfExtrapolatedValues() {
            var sum = 0L;
            for (var historyEntry : historyEntries) {
                List<Values> steps = getStepsToZero(historyEntry);
                steps.removeLast(); // remove the zero values
                var lastValue = 0L;
                for (var i = steps.size()-1; i >= 0; i--) {
                    var step = steps.get(i);
                    lastValue = step.values.getLast() + lastValue;
                }
                sum += lastValue;
            }
            return sum;
        }

        public long sumOfExtrapolatedValuesAtBackwards() {
            var sum = 0L;
            for (var historyEntry : historyEntries) {
                List<Values> steps = getStepsToZero(historyEntry);
                steps.removeLast(); // remove the zero values
                var firstValue = 0L;
                for (var i = steps.size()-1; i >= 0; i--) {
                    var step = steps.get(i);
                    firstValue = step.values.getFirst() - firstValue;
                }
                sum += firstValue;
            }
            return sum;
        }
    }

    public Day9(Path path) {
        super(path);
    }

    @Override
    public Object part1() {
        try {
            var report = OASISReport.fromStrings(this.readInput());
            return report.sumOfExtrapolatedValues();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Object part2() {
        try {
            var report = OASISReport.fromStrings(this.readInput());
            return report.sumOfExtrapolatedValuesAtBackwards();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
