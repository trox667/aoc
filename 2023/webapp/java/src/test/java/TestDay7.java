import io.trox667.aoc.Day7;
import org.junit.jupiter.api.Test;

import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay7 {
    @Test
    public void part1() {
        assertEquals((long)6440, new Day7(Paths.get("../../input/sample07")).part1());
        assertEquals((long)250946742, new Day7(Paths.get("../../input/input07")).part1());
    }

    @Test
    public void part2() {
        assertEquals((long)5905, new Day7(Paths.get("../../input/sample07")).part2());
        assertEquals((long)251824095, new Day7(Paths.get("../../input/input07")).part2());
    }
}
