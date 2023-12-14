import io.trox667.aoc.Day14;
import org.junit.jupiter.api.Test;

import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay14 {
    @Test
    public void part1() {
        assertEquals( 136L, new Day14(Paths.get("../../input/sample14")).part1());
        assertEquals( 113486L, new Day14(Paths.get("../../input/input14")).part1());
    }

    @Test
    public void part2() {
        assertEquals(64L, new Day14(Paths.get("../../input/sample14")).part2());
        assertEquals(104409L, new Day14(Paths.get("../../input/input14")).part2());
    }
}
