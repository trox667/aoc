import io.trox667.aoc.day5.Day5;
import org.junit.jupiter.api.Test;

import java.nio.file.Path;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay5 {
    @Test
    public void part1() {
//        var day5 = new Day5(Path.of("../../inputs/sample5"));
        var day5 = new Day5(Path.of("../../inputs/input5"));
        assertEquals(day5.part1().toString(), "BSDMQFLSP");
//        assertEquals(day5.part1().toString(), "CMZ");
    }

    @Test
    public void part2() {
//        var day5 = new Day5(Path.of("../../inputs/sample5"));
        var day5 = new Day5(Path.of("../../inputs/input5"));
        assertEquals(day5.part2().toString(), "PGSQBFLDP");
//        assertEquals(day5.part2().toString(), "MCD");
    }
}
