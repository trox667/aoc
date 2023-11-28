package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public abstract class Day {
    protected Path path;

    public Day(Path path) {
        this.path = path;
    }

    public List<String> readInput() throws IOException {
        return Files.readAllLines(path);
    }

    public abstract <T> T part1();
    public abstract <T> T part2();
}
