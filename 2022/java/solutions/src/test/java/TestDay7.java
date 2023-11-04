import io.trox667.aoc.day7.Day7;
import org.junit.jupiter.api.Test;

import java.nio.file.Path;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay7 {
    @Test
    public void part1() {
//        var day7 = new Day7(Path.of("../../inputs/sample7"));
//        assertEquals(day7.part1().toString(), "95437");
        var day7 = new Day7(Path.of("../../inputs/input7"));
        assertEquals(day7.part1().toString(), "1844187");
    }

    @Test
    public void part2() {
//        var day7 = new Day7(Path.of("../../inputs/sample7"));
//        assertEquals(day7.part2().toString(), "24933642");
        var day7 = new Day7(Path.of("../../inputs/input7"));
        assertEquals(day7.part2().toString(), "4978279");
    }
}
