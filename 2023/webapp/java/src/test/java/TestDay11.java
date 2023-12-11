import io.trox667.aoc.Day11;
import org.junit.jupiter.api.Test;

import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay11 {
    @Test
    public void part1() {
//        assertEquals( 374L, new Day11(Paths.get("../../input/sample11")).part1());
        assertEquals( 9723824L, new Day11(Paths.get("../../input/input11")).part1());
    }

    @Test
    public void part2() {
//        assertEquals(8410L, new Day11(Paths.get("../../input/sample11")).part2());
        assertEquals(731244261352L, new Day11(Paths.get("../../input/input11")).part2());
    }
}
