import io.trox667.aoc.day6.Day6;

import java.nio.file.Path;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay6 {
    @Test
    public void part1() {
//        var day6 = new Day6(Path.of("../../inputs/sample6"));
//        assertEquals(day6.part1().toString(), "7");
        var day6 = new Day6(Path.of("../../inputs/input6"));
        assertEquals(day6.part1().toString(), "1723");
    }

    @Test
    public void part2() {
//        var day6 = new Day6(Path.of("../../inputs/sample6"));
//        assertEquals(day6.part2().toString(), "19");
        var day6 = new Day6(Path.of("../../inputs/input6"));
        assertEquals(day6.part2().toString(), "3708");
    }
}
