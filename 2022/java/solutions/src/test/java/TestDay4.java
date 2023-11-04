import io.trox667.aoc.day4.Day4;
import org.junit.jupiter.api.Test;

import java.nio.file.Path;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay4 {
    @Test
    public void part1() {
        var day4 = new Day4(Path.of("../../inputs/input4"));
        assertEquals(day4.part1().toString(), "464");
    }
    @Test
    public void part2() {
        var day4 = new Day4(Path.of("../../inputs/input4"));
        assertEquals(day4.part2().toString(), "770");
    }

}
