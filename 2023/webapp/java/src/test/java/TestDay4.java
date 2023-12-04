import io.trox667.aoc.Day4;
import org.junit.jupiter.api.Test;

import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay4 {
    @Test
    public void part1() {
        assertEquals(13, new Day4(Paths.get("../../input/sample04")).part1());
        assertEquals(22897, new Day4(Paths.get("../../input/input04")).part1());
    }

    @Test
    public void part2() {
        assertEquals(30, new Day4(Paths.get("../../input/sample04")).part2());
        assertEquals(5095824, new Day4(Paths.get("../../input/input04")).part2());
    }
}
