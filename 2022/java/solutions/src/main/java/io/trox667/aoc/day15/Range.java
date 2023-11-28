package io.trox667.aoc.day15;

import java.util.Objects;

public final class Range {
    private final int start;
    private final int end;
    private final int y;

    public Range(int start, int end, int y) {
        this.start = start;
        this.end = end;
        this.y = y;
    }

    public int start() {
        return start;
    }

    public int end() {
        return end;
    }

    public int y() {
        return y;
    }

    public int getSize() {
        if (start < 0 && end < 0) {
            return Math.abs(start + end);
        } else if (start < 0) {
            return Math.abs(start) + end;
        } else {
            return end - start;
        }
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == this) return true;
        if (obj == null || obj.getClass() != this.getClass()) return false;
        var that = (Range) obj;
        return this.start == that.start &&
                this.end == that.end &&
                this.y == that.y;
    }

    @Override
    public int hashCode() {
        return Objects.hash(start, end, y);
    }

    @Override
    public String toString() {
        return "Range[" +
                "start=" + start + ", " +
                "end=" + end + ", " +
                "y=" + y + ']';
    }

}
