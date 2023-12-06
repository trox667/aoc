import io.trox667.aoc.Day6;
import org.junit.jupiter.api.Test;

import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay6 {
    @Test
    public void part1() {
        assertEquals((long) 288, new Day6(Paths.get("../../input/sample06")).part1());
        assertEquals((long) 131376, new Day6(Paths.get("../../input/input06")).part1());
    }

    @Test
    public void part2() {
        assertEquals((long) 71503, new Day6(Paths.get("../../input/sample06")).part2());
        assertEquals((long) 34123437, new Day6(Paths.get("../../input/input06")).part2());
    }
}
