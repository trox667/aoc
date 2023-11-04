package io.trox667.aoc.day1;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Elf {
    private final List<Calories> calories;

    public Elf() {
        this.calories = new ArrayList<>();
    }

    public void addCalories(Calories calories) {
        this.calories.add(calories);
    }

    public int getCaloriesSum() {
        return this.calories.stream().map(Calories::value).reduce(0, Integer::sum);
    }
}

