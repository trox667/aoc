package io.trox667.aoc.day15;

import java.util.ArrayList;
import java.util.List;

public class Sensor {
    private final Coordinate position;
    private final Coordinate closestBeacon;

    public Sensor(Coordinate position, Coordinate closestBeacon) {
        this.position = position;
        this.closestBeacon = closestBeacon;
    }

    public Coordinate getPosition() {
        return position;
    }

    public Coordinate getClosestBeacon() {
        return closestBeacon;
    }

    public List<Range> getCoveredArea() {
        var manhattanDistance = this.getManhattanDistance(this.position, this.closestBeacon);
        var coveredArea = new ArrayList<Range>();

        var startY = this.position.y() - manhattanDistance;
        var endY = this.position.y();
        var countY = 0;
        for (int y = startY; y < endY; y++) {
            var rangeStart = this.position.x() - countY;
            var rangeEnd = this.position.x() + countY;
            coveredArea.add(new Range(rangeStart, rangeEnd, y));
            countY++;
        }
        for (int y = endY; y <= endY+manhattanDistance; y++) {
            var rangeStart = this.position.x() - countY;
            var rangeEnd = this.position.x() + countY;
            coveredArea.add(new Range(rangeStart, rangeEnd, y));
            countY--;
        }

        return coveredArea;
    }

    private int getManhattanDistance(Coordinate a, Coordinate b) {
        return Math.abs(a.x() - b.x()) + Math.abs(a.y() - b.y());
    }

    @Override
    public String toString() {
        return "Sensor{" +
                "position=" + position +
                ", closestBeacon=" + closestBeacon +
                '}';
    }
}
