package io.trox667.aoc.day1;

public record Calories(int value) {
    public static Calories fromString(String line) throws NumberFormatException {
        return new Calories(Integer.parseInt(line));
    }
}
