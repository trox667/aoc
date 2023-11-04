package io.trox667.aoc.day6;

import io.trox667.aoc.Day;
import io.trox667.aoc.Result;

import java.io.IOException;
import java.nio.file.Path;

public class Day6 extends Day {

    public Day6(Path path) {
        super(path);
    }

    @Override
    public Result part1() {
        try {
            var input = readInput();
            var line = input.get(0);
            var startOfPacketMarker = new StartOfPacketMarker();
            char[] sequence = null;
            var index = -1;
            for (var i = 0; i < line.length() - 4; i++) {
                sequence = line.substring(i, i + 4).toCharArray();
                if (startOfPacketMarker.checkSequence(sequence)) {
                    index = i + 4;
                    break;
                }
            }
            return new Result(index);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Result part2() {
        try {
            var input = readInput();
            var line = input.get(0);
            var startOfPacketMarker = new StartOfPacketMarker();
            char[] sequence = null;
            var index = -1;
            for (var i = 0; i < line.length() - 14; i++) {
                sequence = line.substring(i, i + 14).toCharArray();
                if (startOfPacketMarker.checkSequence(sequence)) {
                    index = i + 14;
                    break;
                }
            }
            return new Result(index);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
