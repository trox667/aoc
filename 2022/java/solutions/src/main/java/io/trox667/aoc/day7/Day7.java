package io.trox667.aoc.day7;

import io.trox667.aoc.Day;
import io.trox667.aoc.Result;

import java.io.IOException;
import java.nio.file.Path;

public class Day7 extends Day {

    public Day7(Path path) {
        super(path);
    }

    @Override
    public Result part1() {
        try {
            var input = readInput();
            var outputParser = new OutputParser(input);
            while (outputParser.hasNext()) {
                outputParser.next();
            }
            var fs = new FileSystem(outputParser.getRootDirectory());
            return new Result(fs.getDirectoriesSize());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Result part2() {
        try {
            var input = readInput();
            var outputParser = new OutputParser(input);
            while (outputParser.hasNext()) {
                outputParser.next();
            }
            var fs = new FileSystem(outputParser.getRootDirectory());
            return new Result(fs.getDirectoryToDelete(30_000_000));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
