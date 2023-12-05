package io.trox667.aoc;

import org.junit.jupiter.api.Test;

import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDay5 {
    @Test
    public void part1() {
        assertEquals((long) 35, new Day5(Paths.get("../../input/sample05")).part1());
        assertEquals((long) 57075758, new Day5(Paths.get("../../input/input05")).part1());
    }

    @Test
    public void part2() {
        assertEquals((long) 46, new Day5(Paths.get("../../input/sample05")).part2());
        assertEquals(0, new Day5(Paths.get("../../input/input05")).part2());
    }
}
