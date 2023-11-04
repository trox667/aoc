package io.trox667.aoc.day1;

import io.trox667.aoc.Day;
import io.trox667.aoc.Result;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Day1 extends Day {
    public Day1(Path path) {
        super(path);
    }

    private List<Elf> parseElves(List<String> input) {
        List<Elf> elves = new ArrayList<>();
        Elf currentElf = new Elf();
        for (var line : input) {
            if (line.isEmpty()) {
                elves.add(currentElf);
                currentElf = new Elf();
            } else {
                currentElf.addCalories(Calories.fromString(line));
            }
        }
        elves.add(currentElf);
        return elves;
    }

    private List<Integer> getElvesCalories(List<Elf> elves) {
        var calories = new ArrayList<>(elves.stream().map(Elf::getCaloriesSum).toList());
        Collections.sort(calories);
        return calories;
    }

    private int getHighestCalories(List<Integer> calories) {
        return calories.getLast();
    }

    @Override
    public Result part1() {
        try {
            var input = this.readInput();
            var elves = parseElves(input);
            var calories = getElvesCalories(elves);
            return new Result(getHighestCalories(calories));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private int getTopThreeCaloriesAsSum(List<Integer> calories) throws IllegalArgumentException {
        var size = calories.size();
        if (size < 3) {
            throw new IllegalArgumentException("calories must contain at least 3 items.");
        }
        return calories.get(size - 1) + calories.get(size - 2) + calories.get(size - 3);
    }

    @Override
    public Result part2() {
        try {
            var input = this.readInput();
            var elves = parseElves(input);
            var calories = getElvesCalories(elves);
            return new Result(getTopThreeCaloriesAsSum(calories));
        } catch (IOException | IllegalArgumentException e) {
            throw new RuntimeException(e);
        }
    }
}
