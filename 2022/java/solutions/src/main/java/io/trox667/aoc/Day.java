package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public abstract class Day {
    private final Path path;

    public Day(Path path) {
        this.path = path;
    }

    protected List<String> readInput() throws IOException {
        return Files.readAllLines(path);
    }

    public abstract Result part1();

    public abstract Result part2();
}
