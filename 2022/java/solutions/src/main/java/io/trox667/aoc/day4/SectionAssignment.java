package io.trox667.aoc.day4;

import java.util.Arrays;
import java.util.Objects;

public final class SectionAssignment {
    private final int min;
    private final int max;

    public SectionAssignment(int min, int max) {
        this.min = min;
        this.max = max;
    }

    public static SectionAssignment fromString(String token) throws IllegalArgumentException {
        var tokens = Arrays.stream(token.split("-")).map(Integer::parseInt).toList();
        if (tokens.size() < 2) {
            throw new IllegalArgumentException();
        }
        return new SectionAssignment(tokens.getFirst(), tokens.getLast());
    }

    public int min() {
        return min;
    }

    public int max() {
        return max;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == this) return true;
        if (obj == null || obj.getClass() != this.getClass()) return false;
        var that = (SectionAssignment) obj;
        return this.min == that.min &&
                this.max == that.max;
    }

    @Override
    public int hashCode() {
        return Objects.hash(min, max);
    }

    @Override
    public String toString() {
        return "SectionAssignment[" +
                "min=" + min + ", " +
                "max=" + max + ']';
    }

}
