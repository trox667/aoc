package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

public class Day1 extends Day {
    private static Map<String, String> digits = Map.of("one", "1", "two", "2", "three", "3", "four", "4", "five", "5", "six", "6", "seven", "7", "eight", "8", "nine", "9");

    public Day1(Path path) {
        super(path);
    }


    private boolean isDigit(String input) {
        assert input.length() > 0;
        return Character.isDigit(input.charAt(0));
    }

    private String toDigit(String input) {
        return digits.get(input);
    }

    private String getDigits(String input) {
        return Arrays.stream(input.split("")).filter(this::isDigit).reduce("", String::concat);
    }

    private String getNamedDigits(String input) {
        var result = "";
        for (var start = 0; start < input.length(); start++) {
            // maximum word size is 5, so start + 6 for the substring
            for (var pos = start + 1; pos < start + 6 && pos < input.length() + 1; pos++) {
                var token = input.substring(start, pos);
                if (isDigit(token)) {
                    result += token;
                    break;
                } else if (toDigit(token) != null) {
                    result += toDigit(token);
                    break;
                }
            }
        }
        return result;
    }

    private int getCalibrationValues(String input) {
        List<String> digits = Arrays.asList(input.split(""));
        return Integer.parseInt(digits.getFirst() + digits.getLast());
    }

    @Override
    public Object part1() {
        var result = 0;
        try {
            var input = readInput();
            for (var line : input) {
                result += getCalibrationValues(getDigits(line));
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        return result;
    }

    @Override
    public Object part2() {
        var result = 0;
        try {
            var input = readInput();
            for (var line : input) {
                result += getCalibrationValues(getNamedDigits(line));
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        return result;
    }
}
