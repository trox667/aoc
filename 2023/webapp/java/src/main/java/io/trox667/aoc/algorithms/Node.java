package io.trox667.aoc.algorithms;

import java.util.Objects;

public final class Node {
    private String name;
    private int distance;

    public Node(String name, int distance) {
        this.name = name;
        this.distance = distance;
    }

    public Node(String name) {
        this.name = name;
        this.distance = 0;
    }

    public String name() {
        return name;
    }

    public int distance() {
        return distance;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setDistance(int distance) {
        this.distance = distance;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == this) return true;
        if (obj == null || obj.getClass() != this.getClass()) return false;
        var that = (Node) obj;
        return Objects.equals(this.name, that.name) &&
                this.distance == that.distance;
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, distance);
    }

    @Override
    public String toString() {
        return "Node[" +
                "name=" + name + ", " +
                "distance=" + distance + ']';
    }

}
