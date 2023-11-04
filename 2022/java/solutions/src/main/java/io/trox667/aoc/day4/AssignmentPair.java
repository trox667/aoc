package io.trox667.aoc.day4;

import java.util.Arrays;
import java.util.Objects;

public final class AssignmentPair {
    private final SectionAssignment a;
    private final SectionAssignment b;

    public AssignmentPair(SectionAssignment a, SectionAssignment b) {
        this.a = a;
        this.b = b;
    }

    public static AssignmentPair fromString(String line) throws IllegalArgumentException {
        var sectionAssignments = Arrays.stream(line.split(",")).map(SectionAssignment::fromString).toList();
        if (sectionAssignments.size() < 2) {
            throw new IllegalArgumentException();
        }
        return new AssignmentPair(sectionAssignments.getFirst(), sectionAssignments.getLast());
    }

    public boolean fullyContains() {
        // a.min >= b.min && a.max <= b.max = true
        // b.min >= a.min && b.max <= a.max = true
        return (a.min() >= b.min() && a.max() <= b.max()) || (b.min() >= a.min() && b.max() <= a.max());
    }

    public boolean overlap() {
       /* 5-7,7-9 overlaps in a single section, 7.
          2-8,3-7 overlaps all of the sections 3 through 7.
          6-6,4-6 overlaps in a single section, 6.
          2-6,4-8 overlaps in sections 4, 5, and 6.*/

        return (a.min() <= b.max() && a.max() >= b.min());
    }

    public SectionAssignment a() {
        return a;
    }

    public SectionAssignment b() {
        return b;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == this) return true;
        if (obj == null || obj.getClass() != this.getClass()) return false;
        var that = (AssignmentPair) obj;
        return Objects.equals(this.a, that.a) &&
                Objects.equals(this.b, that.b);
    }

    @Override
    public int hashCode() {
        return Objects.hash(a, b);
    }

    @Override
    public String toString() {
        return "AssignmentPair[" +
                "a=" + a + ", " +
                "b=" + b + ']';
    }

}
