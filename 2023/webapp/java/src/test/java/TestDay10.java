import io.trox667.aoc.Day10;
import org.junit.jupiter.api.Test;

import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay10 {
    @Test
    public void part1() {
        assertEquals((long) 0, new Day10(Paths.get("../../input/sample10")).part1());
        assertEquals((long) 0, new Day10(Paths.get("../../input/input10")).part1());
    }

    @Test
    public void part2() {
        assertEquals((long) 0, new Day10(Paths.get("../../input/sample10")).part2());
        assertEquals((long) 0, new Day10(Paths.get("../../input/input10")).part2());
    }
}
