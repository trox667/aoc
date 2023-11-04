import io.trox667.aoc.day1.Day1;
import org.junit.jupiter.api.Test;

import java.nio.file.Path;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay1 {
    @Test
    public void part1() {
        var day1 = new Day1(Path.of("../../inputs/input1"));
        assertEquals(day1.part1().toString(), "66616");
    }

    @Test
    public void part2() {
        var day1 = new Day1(Path.of("../../inputs/input1"));
        assertEquals(day1.part2().toString(), "199172");
    }
}
