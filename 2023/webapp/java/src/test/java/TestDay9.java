import io.trox667.aoc.Day9;
import org.junit.jupiter.api.Test;

import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay9 {
    @Test
    public void part1() {
        assertEquals((long) 114, new Day9(Paths.get("../../input/sample09")).part1());
        assertEquals((long) 1980437560, new Day9(Paths.get("../../input/input09")).part1());
    }

    @Test
    public void part2() {
        assertEquals((long) 2, new Day9(Paths.get("../../input/sample09")).part2());
        assertEquals((long) 977, new Day9(Paths.get("../../input/input09")).part2());
    }
}
