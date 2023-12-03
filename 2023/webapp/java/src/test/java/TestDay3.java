import io.trox667.aoc.Day3;
import org.junit.jupiter.api.Test;

import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay3 {
    @Test
    public void part1() {
        assertEquals(4361, new Day3(Paths.get("../../input/sample03")).part1());
        assertEquals(536202, new Day3(Paths.get("../../input/input03")).part1());
    }

    @Test
    public void part2() {
        assertEquals(467835, new Day3(Paths.get("../../input/sample03")).part2());
        assertEquals(78272573, new Day3(Paths.get("../../input/input03")).part2());
    }
}
