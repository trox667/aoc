package io.trox667.aoc.day8;

import io.trox667.aoc.Day;
import io.trox667.aoc.Result;

import java.io.IOException;
import java.nio.file.Path;
import java.util.Arrays;

public class Day8 extends Day {
    public Day8(Path path) {
        super(path);
    }

    @Override
    public Result part1() {
        try {
            var input = readInput().stream().filter(line -> !line.isBlank()).toList();
            var trees = input.stream().map(line -> Arrays.stream(line.split("")).map(Integer::parseInt).toList()).toList();
            var map = new Map(trees.size(), trees.get(0).size(), trees);
            var validator = new VisibilityValidator(map);
            return new Result(validator.countVisibleTrees());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Result part2() {
        try {
            var input = readInput();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return null;
    }
}
