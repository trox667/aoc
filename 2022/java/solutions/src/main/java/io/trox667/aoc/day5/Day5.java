package io.trox667.aoc.day5;

import io.trox667.aoc.Day;
import io.trox667.aoc.Result;

import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class Day5 extends Day {
    public Day5(Path path) {
        super(path);
    }

    private void applyInstructions(List<Instruction> instructions, Crates crates) {
        for (var instruction : instructions) {
            crates.move(instruction);
        }
    }

    private void applyInstructionsMoveMultiple(List<Instruction> instructions, Crates crates) {
        for (var instruction : instructions) {
            crates.moveMultiple(instruction);
        }
    }

    @Override
    public Result part1() {
        try {
            var input = readInput();
            var crates = new Crates();
            var instructions = new ArrayList<Instruction>();
            boolean isHeader = true;
            for (var line : input) {
                if (!line.contains("[")) {
                    isHeader = false;
                }
                if (isHeader) {
                    crates.addToStacksFromString(line);
                } else {
                    if (line.contains("move")) {
                        instructions.add(Instruction.fromString(line));
                    }
                }
            }

            applyInstructions(instructions, crates);
            return new Result(crates.getFirstValueOfEachStack());

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Result part2() {
        try {
            var input = readInput();
            var crates = new Crates();
            var instructions = new ArrayList<Instruction>();
            boolean isHeader = true;
            for (var line : input) {
                if (!line.contains("[")) {
                    isHeader = false;
                }
                if (isHeader) {
                    crates.addToStacksFromString(line);
                } else {
                    if (line.contains("move")) {
                        instructions.add(Instruction.fromString(line));
                    }
                }
            }

            applyInstructionsMoveMultiple(instructions, crates);
            return new Result(crates.getFirstValueOfEachStack());

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
