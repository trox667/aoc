package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.LongStream;

public class Day9 extends Day {

    private record Values(List<Long> values) {
        public Values differences() {
            var newValues = new ArrayList<Long>();
            LongStream.range(0, values.size() - 1).forEach(i -> newValues.add(values.get((int) i + 1) - values.get((int) i)));
            return new Values(newValues);
        }

        public boolean isZero() {
            return values.stream().allMatch(v -> v == 0);
        }
    }

    private static class HistoryEntry {
        private Values history;

        public static HistoryEntry fromString(String line) {
            var entry = new HistoryEntry();
            entry.history = new Values(Arrays.stream(line.split(" ")).map(Long::parseLong).toList());
            return entry;
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
            steps.add(historyEntry.history.differences());
            while (!steps.getLast().isZero()) {
                steps.add(steps.getLast().differences());
            }
            steps.removeLast(); // remove the zero values
            return steps;
        }

        public long sumOfExtrapolatedValues(boolean beginning) {
            return historyEntries.stream().map(historyEntry -> {
                List<Values> steps = getStepsToZero(historyEntry);
                var currentValue = 0L;
                for (var i = steps.size() - 1; i >= 0; i--) {
                    var step = steps.get(i);
                    if (beginning) {
                        currentValue = step.values.getFirst() - currentValue;
                    } else {
                        currentValue = step.values.getLast() + currentValue;
                    }
                }
                return currentValue;
            }).reduce(0L, Long::sum);
        }
    }

    public Day9(Path path) {
        super(path);
    }

    @Override
    public Object part1() {
        try {
            var report = OASISReport.fromStrings(this.readInput());
            return report.sumOfExtrapolatedValues(false);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Object part2() {
        try {
            var report = OASISReport.fromStrings(this.readInput());
            return report.sumOfExtrapolatedValues(true);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
