import io.trox667.aoc.Day10;
import org.junit.jupiter.api.Test;

import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay10 {
    @Test
    public void part1() {
        assertEquals(4, new Day10(Paths.get("../../input/sample10")).part1());
        assertEquals(8, new Day10(Paths.get("../../input/sample10_2")).part1());
        assertEquals(6773, new Day10(Paths.get("../../input/input10")).part1());
    }

    @Test
    public void part2() {
        assertEquals(4, new Day10(Paths.get("../../input/sample10_3")).part2());
//        assertEquals(0, new Day10(Paths.get("../../input/sample10_4")).part2());
//        assertEquals(0, new Day10(Paths.get("../../input/sample10_5")).part2());
//        assertEquals(0, new Day10(Paths.get("../../input/input10")).part2());
        // > 481
    }
}
