import io.trox667.aoc.Day15;
import org.junit.jupiter.api.Test;

import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay15 {
    @Test
    public void part1() {
        assertEquals( 1320L, new Day15(Paths.get("../../input/sample15")).part1());
        assertEquals( 0L, new Day15(Paths.get("../../input/input15")).part1());
    }

    @Test
    public void part2() {
        assertEquals(0L, new Day15(Paths.get("../../input/sample15")).part2());
//        assertEquals(0L, new Day15(Paths.get("../../input/input15")).part2());
    }
}
