import io.trox667.aoc.Day17Dijkstra;
import org.junit.jupiter.api.Test;

import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay17 {
    @Test
    public void part1() {
        assertEquals( 0, new Day17Dijkstra(Paths.get("../../input/sample17")).part1());
//        assertEquals( 0, new Day17(Paths.get("../../input/input17")).part1());
    }

    @Test
    public void part2() {
        assertEquals(0, new Day17Dijkstra(Paths.get("../../input/sample17")).part2());
//        assertEquals(0, new Day17(Paths.get("../../input/input17")).part2());
    }
}
