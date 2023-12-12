package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.regex.Pattern;

public class Day12 extends Day {

    private record CacheArgs(int remainingSprings, int index) {
    }

    private record ConditionRecord(String springs, List<Integer> groupsOfDamagedSprings,
                                   HashMap<CacheArgs, Long> cache) {

        private boolean validate(String currentSprings, String springs) {
            for (var i = 0; i < currentSprings.length(); i++) {
                if (springs.charAt(i) != '?' && currentSprings.charAt(i) != springs.charAt(i)) {
                    return false;
                }
            }
            return true;
        }

        public long generate() {
            var numSprings = this.springs.length();
            var numDamagedSprings = this.groupsOfDamagedSprings.stream().reduce(0, Integer::sum);
            var numGaps = this.groupsOfDamagedSprings.size() - 1;
            var numIntactSprings = numSprings - numDamagedSprings - numGaps;
            var result = generatePossibleCombinations(numIntactSprings, 0, "");
            return result;
        }

        private long generatePossibleCombinations(int numSprings, int index, String basePattern) {
            if (index == this.groupsOfDamagedSprings.size()) {
                var pattern = basePattern + ".".repeat(numSprings);
                if (validate(pattern, this.springs)) {
                    return 1;
                }
                return 0;
            }

            var isBorder = index == 0 || index == this.groupsOfDamagedSprings.size();

            var result = 0L;

            for (var numSpringsDistributed = numSprings; numSpringsDistributed >= 0; numSpringsDistributed--) {
                var pattern = basePattern;
                if (!isBorder) {
                    pattern += '.';
                }

                var remainingSprings = numSprings - numSpringsDistributed;
                pattern += ".".repeat(numSpringsDistributed);
                if (index < this.groupsOfDamagedSprings.size()) {
                    pattern += "#".repeat(this.groupsOfDamagedSprings.get(index));
                }
                if (validate(pattern, this.springs)) {
                    if (cache.containsKey(new CacheArgs(remainingSprings, index + 1))) {
                        result += cache.get(new CacheArgs(remainingSprings, index + 1));
                    } else {
                        var combinations = generatePossibleCombinations(remainingSprings, index + 1, pattern);
                        cache.put(new CacheArgs(remainingSprings, index + 1), combinations);
                        result += combinations;
                    }
                }
            }

            return result;
        }
    }

    private static class ConditionRecords {
        private List<ConditionRecord> records;

        ConditionRecords() {
            this.records = new ArrayList<>();
        }

        public static ConditionRecords fromStrings(List<String> lines) {
            var conditionRecords = new ConditionRecords();
            for (var line : lines) {
                var tokens = line.split(" ");
                var conditionRecord = new ConditionRecord(tokens[0], Arrays.stream(tokens[1].split(",")).map(Integer::parseInt).toList(), new HashMap<>());
                conditionRecords.records.add(conditionRecord);
            }
            return conditionRecords;
        }

        public static ConditionRecords fromStrings2(List<String> lines) {
            var conditionRecords = new ConditionRecords();
            for (var line : lines) {
                var tokens = line.split(" ");
                var springs = (tokens[0] + "?").repeat(5);
                springs = springs.substring(0, springs.length() - 1);
                var groups = Arrays.stream(tokens[1].split(",")).map(Integer::parseInt).toList();
                var manyGroups = new ArrayList<Integer>();
                for (var i = 0; i < 5; i++) {
                    manyGroups.addAll(groups);
                }
                var conditionRecord = new ConditionRecord(springs, manyGroups, new HashMap<>());
                conditionRecords.records.add(conditionRecord);
            }
            return conditionRecords;
        }

        public long getCombinations() {

            return this.records.stream().map(r -> r.generate()).reduce(0L, Long::sum);

            // MT is not that much faster
//            ExecutorService service = Executors.newVirtualThreadPerTaskExecutor();
//            List<Future<Long>> results = new ArrayList<>();
//            for (var record : this.records) {
//                var future = service.submit(() -> record.generate());
//                results.add(future);
//            }
//            return results.stream().map(f -> {
//                try {
//                    return f.get();
//                } catch (InterruptedException e) {
//                    throw new RuntimeException(e);
//                } catch (ExecutionException e) {
//                    throw new RuntimeException(e);
//                }
//            }).reduce(0L, Long::sum);
        }
    }

    public Day12(Path path) {
        super(path);
    }

    @Override
    public Object part1() {
        try {
            var conditionRecords = ConditionRecords.fromStrings(this.readInput());
            return conditionRecords.getCombinations();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Object part2() {
        try {
            var conditionRecords = ConditionRecords.fromStrings2(this.readInput());
            return conditionRecords.getCombinations();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
