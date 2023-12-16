import io.trox667.aoc.Day16;
import org.junit.jupiter.api.Test;

import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay16 {
    @Test
    public void part1() {
        assertEquals( 46, new Day16(Paths.get("../../input/sample16")).part1());
        assertEquals( 6622, new Day16(Paths.get("../../input/input16")).part1());
    }

    @Test
    public void part2() {
        assertEquals(51, new Day16(Paths.get("../../input/sample16")).part2());
        assertEquals(7130, new Day16(Paths.get("../../input/input16")).part2());
    }
}
