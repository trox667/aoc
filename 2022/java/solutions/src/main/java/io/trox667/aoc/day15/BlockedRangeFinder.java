package io.trox667.aoc.day15;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class BlockedRangeFinder {
    private final List<Range> ranges;

    public BlockedRangeFinder(List<List<Range>> ranges) {
        this.ranges = ranges.stream().map(this::mergeRanges).reduce(new ArrayList<>(), (acc, list) -> {
            acc.addAll(list);
            return acc;
        });
    }

    private List<Range> mergeRanges(List<Range> ranges) {
        var mergedRanges = new ArrayList<Range>();
        ranges.sort(Comparator.comparingInt(Range::start));
        var currentStart = Integer.MIN_VALUE;
        var currentEnd = Integer.MIN_VALUE;
        var y = ranges.get(0).y();
        for (Range range : ranges) {
            var start = range.start();
            var end = range.end();
            if (start > currentEnd) {
                mergedRanges.add(new Range(start, end, y));
                currentStart = start;
                currentEnd = end;
            } else {
                mergedRanges.removeLast();
                mergedRanges.add(new Range(currentStart, end, y));
                currentEnd = Math.max(currentEnd, end);
            }
        }


        return mergedRanges;
    }

    public int findBlockedCoordinates(int y) {
        var blockedRanges = ranges.stream().filter(range -> range.y() == y).toList();
        return blockedRanges.stream().reduce(0, (acc, range) -> acc + range.getSize(), Integer::sum);
    }

    public List<Range> getRanges() {
        return ranges;
    }
}
