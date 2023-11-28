import io.trox667.aoc.day8.Day8;
import org.junit.jupiter.api.Test;

import java.nio.file.Path;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay8 {
    @Test
    public void part1() {
//        var day8 = new Day8(Path.of("../../inputs/sample8"));
//        assertEquals(day8.part1().toString(), "21");
        var day8 = new Day8(Path.of("../../inputs/input8"));
        assertEquals(day8.part1().toString(), "1676");
    }

    @Test
    public void part2() {
//        var day8 = new Day8(Path.of("../../inputs/sample8"));
//        assertEquals(day8.part2().toString(), "8");
        var day8 = new Day8(Path.of("../../inputs/input8"));
        assertEquals(day8.part2().toString(), "313200");
    }
}
