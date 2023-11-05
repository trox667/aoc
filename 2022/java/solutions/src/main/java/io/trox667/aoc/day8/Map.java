package io.trox667.aoc.day8;

import java.util.ArrayList;
import java.util.List;

public class Map {
    private final int width;
    private final int height;

    private final List<List<Integer>> trees;

    public Map(int width, int height, List<List<Integer>> trees) {
        this.width = width;
        this.height = height;
        this.trees = trees;
    }

    public int getTree(int rowIndex, int columnIndex) throws IllegalArgumentException {
        if (rowIndex >= 0 && rowIndex < height) {
            var row = trees.get(rowIndex);
            if (columnIndex >= 0 && columnIndex < width) {
                return row.get(columnIndex);
            } else {
                throw new IllegalArgumentException("Column index out of bounds");
            }
        } else {
            throw new IllegalArgumentException("Row index out of bounds");
        }
    }

    public List<Integer> getRowSlice(int rowIndex, int columnStart, int columnEnd) {
        if (rowIndex > 0 && rowIndex < height) {
            var row = trees.get(rowIndex);
            if (columnStart >= 0 && columnEnd <= width) {
                return row.subList(columnStart, columnEnd);
            } else {
                return new ArrayList<>();
            }
        } else {
            return new ArrayList<>();
        }
    }

    public List<Integer> getColumnSlice(int columnIndex, int rowStart, int rowEnd) {
        if (rowStart < 0 || rowEnd > height) {
            return new ArrayList<>();
        }
        if (columnIndex < 0 || trees.get(rowStart).size() < columnIndex) {
            return new ArrayList<>();
        }
        var column = new ArrayList<Integer>();
        for (int row = rowStart; row < rowEnd; row++) {
            column.add(trees.get(row).get(columnIndex));
        }
        return column;
    }

    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }
}
