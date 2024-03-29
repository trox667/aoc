import io.trox667.aoc.Day2;
import org.junit.jupiter.api.Test;

import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay2 {
    @Test
    public void part1() {
        assertEquals(8, new Day2(Paths.get("../../input/sample02")).part1());
        assertEquals(2317, new Day2(Paths.get("../../input/input02")).part1());
    }

    @Test
    public void part2() {
        assertEquals(2286, new Day2(Paths.get("../../input/sample02")).part2());
        assertEquals(74804, new Day2(Paths.get("../../input/input02")).part2());
    }
}
