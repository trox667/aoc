import io.trox667.aoc.Day1;
import org.junit.jupiter.api.Test;

import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay1 {
    @Test
    public void testPart1() {
        assertEquals((Integer)142, new Day1(Paths.get("../../input/sample01")).part1());
        assertEquals((Integer)54338, new Day1(Paths.get("../../input/input01")).part1());
    }

    @Test
    public void testPart2() {
        assertEquals((Integer)281, new Day1(Paths.get("../../input/sample01_2")).part2());
        assertEquals((Integer)53389, new Day1(Paths.get("../../input/input01")).part2());
    }
}
