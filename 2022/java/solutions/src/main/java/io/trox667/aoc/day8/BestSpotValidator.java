package io.trox667.aoc.day8;

import java.util.List;

public class BestSpotValidator {

    private Map map;

    public BestSpotValidator(Map map) {
        this.map = map;
    }

    public int getHighstScenicScore() {
        var maxScenicScore = 0;
        for (int rowIndex = 0; rowIndex < map.getHeight(); rowIndex++) {
            for (int columnIndex = 0; columnIndex < map.getWidth(); columnIndex++) {
                maxScenicScore = Math.max(maxScenicScore, calculateTreeScenicScore(rowIndex, columnIndex));
            }
        }
        return maxScenicScore;
    }

    public int calculateTreeScenicScore(int rowIndex, int columnIndex) {
        var tree = map.getTree(rowIndex, columnIndex);
        if (columnIndex == 0 || columnIndex == map.getWidth()-1)
            return 0;
        if (rowIndex == 0 || rowIndex == map.getHeight()-1)
            return 0;
        var rowLeft = map.getRowSlice(rowIndex, 0, columnIndex).reversed();
        var rowRight = map.getRowSlice(rowIndex, columnIndex+1, map.getWidth());
        var columnTop = map.getColumnSlice(columnIndex, 0, rowIndex).reversed();
        var columnBottom = map.getColumnSlice(columnIndex, rowIndex+1, map.getHeight());
        return calculateViewDistance(rowLeft, tree) * calculateViewDistance(rowRight, tree) * calculateViewDistance(columnTop, tree) * calculateViewDistance(columnBottom, tree);
    }

    private int calculateViewDistance(List<Integer> trees, int tree) {
        if (trees.isEmpty()) return 0;
        var count = 0;
        for (var treeHeight : trees) {
            if (treeHeight < tree) {
                count++;
            } else {
                count++;
                break;
            }
        }
        return count;
    }
}
