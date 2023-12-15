package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;

public class Day15 extends Day {
    private static class HASHAlgorithm {

        public static long getHash(String input) {
            var hash = 0L;
            for (var c : input.toCharArray()) {
                var code = (int) c;
                hash += code;
                hash *= 17;
                hash %= 256;
            }
            return hash;
        }
    }

    private static class InitializationSequence {
        public static long fromStrings(List<String> lines) {
            var initializationSequence = new InitializationSequence();
            var result = 0L;
            for (var line : lines) {
                result += Arrays.stream(line.split(",")).map(HASHAlgorithm::getHash).reduce(0L, Long::sum);
            }


            return result;
        }
    }

    public Day15(Path path) {
        super(path);
    }

    @Override
    public Object part1() {
        try {
            return InitializationSequence.fromStrings(this.readInput());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Object part2() {
        
        return null;
    }
}
