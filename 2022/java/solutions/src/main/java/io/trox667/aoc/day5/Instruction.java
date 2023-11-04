package io.trox667.aoc.day5;

public class Instruction {
    private final int count;
    private final int fromIndex;
    private final int toIndex;

    private Instruction(int count, int fromIndex, int toIndex) {
        this.count = count;
        this.fromIndex = fromIndex;
        this.toIndex = toIndex;
    }

    @Override
    public String toString() {
        return "Instruction{" +
                "count=" + count +
                ", fromIndex=" + fromIndex +
                ", toIndex=" + toIndex +
                '}';
    }

    public int getCount() {
        return count;
    }

    public int getFromIndex() {
        return fromIndex;
    }

    public int getToIndex() {
        return toIndex;
    }

    public static Instruction fromString(String line) throws IllegalArgumentException {
        // move 1 from 2 to 1
        var tokens = line.split(" ");
        if (tokens.length != 6) {
            throw new IllegalArgumentException("Instruction line does not contain valid arguments: " + line);
        }
        return new Instruction(Integer.parseInt(tokens[1]), Integer.parseInt(tokens[3]), Integer.parseInt(tokens[5]));
    }
}
