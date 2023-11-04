package io.trox667.aoc.day5;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Crates {
    private final List<Stack<String>> stacks;
    private static final int ELEMENT_SIZE = 3;

    public Crates() {
        this.stacks = new ArrayList<>();
    }

    public void addToStacksFromString(String line) {
        int i = 0;
        int stackIndex = 0;
        while (i < line.length()) {
            if (this.stacks.size() <= stackIndex) {
                this.stacks.add(new Stack<>());
            }
            var token = line.substring(i, i + ELEMENT_SIZE);
            if (!token.isBlank()) {
                token = String.valueOf(token.charAt(1));
                this.stacks.get(stackIndex).add(0, token);
            }
            i += ELEMENT_SIZE + 1;
            stackIndex++;
        }
    }

    public void move(Instruction instruction) {
        int count = instruction.getCount();
        int fromIndex = instruction.getFromIndex() - 1;
        int toIndex = instruction.getToIndex() - 1;
        for (var i = 0; i < count; ++i) {
            var value = this.stacks.get(fromIndex).pop();
            this.stacks.get(toIndex).add(value);
        }
    }

    public void moveMultiple(Instruction instruction) {
        int count = instruction.getCount();
        int fromIndex = instruction.getFromIndex() - 1;
        int toIndex = instruction.getToIndex() - 1;
        var movingItems = new ArrayList<String>();
        for (var i = 0; i < count; ++i) {
            var value = this.stacks.get(fromIndex).pop();
            movingItems.add(value);
        }
        for (var item : movingItems.reversed()) {
            this.stacks.get(toIndex).add(item);
        }
    }

    public String getFirstValueOfEachStack() {
        var builder = new StringBuilder();
        for (var stack : stacks) {
            builder.append(stack.lastElement());
        }
        return builder.toString();
    }
}
