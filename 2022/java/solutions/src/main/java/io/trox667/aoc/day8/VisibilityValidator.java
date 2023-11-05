package io.trox667.aoc.day8;

import java.util.List;

public class VisibilityValidator {
    private final Map map;
    public VisibilityValidator(Map map) {
        this.map = map;
    }

    public int countVisibleTrees() {
        var count = 0;
        for (int rowIndex = 0; rowIndex < map.getHeight(); rowIndex++) {
            for (int columnIndex = 0; columnIndex < map.getWidth(); columnIndex++) {
                if (isVisible(rowIndex, columnIndex)) {
                    count++;
                }
            }
        }
        return count;
    }

    public boolean isVisible(int rowIndex, int columnIndex) {
        var tree = map.getTree(rowIndex, columnIndex);
        if (columnIndex == 0 || columnIndex == map.getWidth()-1)
            return true;
        if (rowIndex == 0 || rowIndex == map.getHeight()-1)
            return true;
        var rowLeft = map.getRowSlice(rowIndex, 0, columnIndex);
        var rowRight = map.getRowSlice(rowIndex, columnIndex+1, map.getWidth());
        var columnTop = map.getColumnSlice(columnIndex, 0, rowIndex);
        var columnBottom = map.getColumnSlice(columnIndex, rowIndex+1, map.getHeight());
        return isTreeVisible(rowLeft, tree) || isTreeVisible(rowRight, tree) || isTreeVisible(columnTop, tree) || isTreeVisible(columnBottom, tree);
    }

    private boolean isTreeVisible(List<Integer> trees, int tree) {
        if (trees.isEmpty()) return true;
        return trees.stream().allMatch(treeHeight -> treeHeight < tree);
    }
}
