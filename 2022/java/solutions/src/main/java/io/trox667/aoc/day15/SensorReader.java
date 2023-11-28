package io.trox667.aoc.day15;

import java.util.List;
import java.util.ArrayList;

public class SensorReader {
    private final List<Sensor> sensors;

    public SensorReader(List<String> lines) throws RuntimeException {
        this.sensors = new ArrayList<Sensor>();
        lines.forEach(this::parseLine);
    }

    private void parseLine(String line) throws RuntimeException {
        String[] tokens = line.split(" ");
        if (tokens.length != 10) {
            throw new RuntimeException("Invalid input line: " + line);
        }
        var sensorX = Integer.parseInt(tokens[2].replaceAll("x=", "").replaceAll(",", ""));
        var sensorY = Integer.parseInt(tokens[3].replaceAll("y=", "").replaceAll(":", ""));
        var beaconX = Integer.parseInt(tokens[8].replaceAll("x=", "").replaceAll(",", ""));
        var beaconY = Integer.parseInt(tokens[9].replaceAll("y=", "").replaceAll(",", ""));
        this.sensors.add(new Sensor(new Coordinate(sensorX, sensorY), new Coordinate(beaconX, beaconY)));
    }

    public List<Sensor> getSensors() {
        return sensors;
    }
}
