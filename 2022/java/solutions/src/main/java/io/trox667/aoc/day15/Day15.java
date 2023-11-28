package io.trox667.aoc.day15;

import io.trox667.aoc.Day;
import io.trox667.aoc.Result;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Day15 extends Day {

    public Day15(Path path) {
        super(path);
    }

    @Override
    public Result part1() {
        try {
            var input = readInput().stream().filter(line -> !line.isBlank()).toList();
            var sensorReader = new SensorReader(input);
            var sensors = sensorReader.getSensors();
            var areaMap = new HashMap<Integer, List<Range>>();
            for (var sensor : sensors) {
                var ranges = sensor.getCoveredArea();
                for (var range : ranges) {
                    if (areaMap.containsKey(range.y())) {
                        var currentRanges = areaMap.get(range.y());
                        currentRanges.add(range);
                        areaMap.put(range.y(), currentRanges);
                    } else {
                        var currentRanges = new ArrayList<Range>();
                        currentRanges.add(range);
                        areaMap.put(range.y(), currentRanges);
                    }
                }
            }
            var blockedRangeFinder = new BlockedRangeFinder(new ArrayList<>(areaMap.values()));
//            return new Result("" + blockedRangeFinder.findBlockedCoordinates(10));
            return new Result("" + blockedRangeFinder.findBlockedCoordinates(2000000));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Result part2() {
        return null;
    }
}
