package io.trox667.aoc;

public class Result {
    private final Object value;

    public Result(int value) {
        this.value = value;
    }

    public Result(String value) {
        this.value = value;
    }

    @Override
    public String toString() {
        return switch (this.value) {
            case Integer i -> i.toString();
            case String s -> s;
            default -> "";
        };
    }
}
