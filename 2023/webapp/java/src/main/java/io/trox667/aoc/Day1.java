package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;

public class Day1 extends Day {
    public Day1(Path path) {
        super(path);
    }

    private String findDigits(String input) {
        var result = input.replaceAll("[a-zA-Z]", "");
        return result;
    }

    private boolean isDigit(String input) {
        try {
            Integer.parseInt(String.valueOf(input));
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    private String toDigit(String input) {
        if (input.equals("one")) {
            return "1";
        } else if (input.equals("two")) {
            return "2";
        } else if (input.equals("three")) {
            return "3";
        } else if (input.equals("four")) {
            return "4";
        } else if (input.equals("five")) {
            return "5";
        } else if (input.equals("six")) {
            return "6";
        } else if (input.equals("seven")) {
            return "7";
        } else if (input.equals("eight")) {
            return "8";
        } else if (input.equals("nine")) {
            return "9";
        } else {
            return null;
        }
    }

    private String findNamedDigits(String input) {
        var result = "";
        for (var start = 0; start < input.length(); start++) {
            for (var pos = start + 1; pos < start + 7 && pos < input.length()+1; pos++) {
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

    private int getFirstAndLastDigit(String input) {
        List<String> digits = Arrays.asList(input.split(""));
        return Integer.parseInt(digits.getFirst() + digits.getLast());
    }

    @Override
    public <T> T part1() {
        var result = 0;
        try {
            var input = readInput();
            for (var line : input) {
                result += getFirstAndLastDigit(findDigits(line));
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        return (T) (Integer) result;
    }

    @Override
    public <T> T part2() {
        var result = 0;
        try {
            var input = readInput();
            for (var line : input) {
                var tmp = getFirstAndLastDigit(findNamedDigits(line));
                result += tmp;
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        return (T) (Integer) result;
    }
}
