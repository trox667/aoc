import io.trox667.aoc.Day12;
import org.junit.jupiter.api.Test;

import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay12 {
    @Test
    public void part1() {
        assertEquals( 21L, new Day12(Paths.get("../../input/sample12")).part1());
        assertEquals( 7204L, new Day12(Paths.get("../../input/input12")).part1());
    }

    @Test
    public void part2() {
        assertEquals(525152L, new Day12(Paths.get("../../input/sample12")).part2());
        assertEquals(1672318386674L, new Day12(Paths.get("../../input/input12")).part2());
    }
}
