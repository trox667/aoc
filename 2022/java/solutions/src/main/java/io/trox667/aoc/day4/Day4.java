package io.trox667.aoc.day4;

import io.trox667.aoc.Day;
import io.trox667.aoc.Result;

import java.io.IOException;
import java.nio.file.Path;

public class Day4 extends Day {
    public Day4(Path path) {
        super(path);
    }

    @Override
    public Result part1() {
        try {
            var input = readInput();
            var assignmentPairs = input.stream().map(AssignmentPair::fromString).toList();
            var containingPairs = assignmentPairs.stream().filter(AssignmentPair::fullyContains).toList();
            return new Result(containingPairs.size());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Result part2() {
        try {
            var input = readInput();
            var assignmentPairs = input.stream().map(AssignmentPair::fromString).toList();
            var overlappingPairs = assignmentPairs.stream().filter(AssignmentPair::overlap).toList();
            return new Result(overlappingPairs.size());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
