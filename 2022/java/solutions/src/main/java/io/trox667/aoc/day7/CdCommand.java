package io.trox667.aoc.day7;

public class CdCommand {
    private final String value;
    public CdCommand(String value) {
        this.value = value;
    }

    public String getTarget() {
        return value.replaceAll("cd ", "");
    }
}
