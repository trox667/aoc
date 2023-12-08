import io.trox667.aoc.Day8;
import org.junit.jupiter.api.Test;

import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay8 {
    @Test
    public void part1() {
        assertEquals((long)2, new Day8(Paths.get("../../input/sample08")).part1());
        assertEquals((long)6, new Day8(Paths.get("../../input/sample08_2")).part1());
        assertEquals((long)19637, new Day8(Paths.get("../../input/input08")).part1());
    }

    @Test
    public void part2() {
        assertEquals((long)6, new Day8(Paths.get("../../input/sample08_3")).part2());
        assertEquals((long)8811050362409L, new Day8(Paths.get("../../input/input08")).part2());
    }
}
