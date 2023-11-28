import io.trox667.aoc.day15.BlockedRangeFinder;
import io.trox667.aoc.day15.Day15;
import io.trox667.aoc.day15.Range;
import org.junit.jupiter.api.Test;

import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;


public class TestDay15 {
    @Test
    public void merge() {
        var ranges = new ArrayList<Range>();
        ranges.add(new Range(-2, 2, 0));
        ranges.add(new Range(1, 2, 0));
        ranges.add(new Range(2, 5, 0));
        ranges.add(new Range(3, 5, 0));
        ranges.add(new Range(6, 6, 0));

        var result = new ArrayList<Range>();
        result.add(new Range(-2, 5, 0));
        result.add(new Range(6, 6, 0));

        var allRanges = new ArrayList<List<Range>>();
        allRanges.add(ranges);
        var blockedRangeFinder = new BlockedRangeFinder(allRanges);
        assertEquals(result, blockedRangeFinder.getRanges());
    }

    @Test
    public void part1() {
//        var day15 = new Day15(Path.of("../../inputs/sample15"));
//        assertEquals("26", day15.part1().toString());
        var day15 = new Day15(Path.of("../../inputs/input15"));
        assertEquals("5073496", day15.part1().toString());
    }

    @Test
    public void part2() {
        var day15 = new Day15(Path.of("../../inputs/input15"));
    }
}
