package io.trox667.aoc.algorithms;

import java.util.List;

public class BinarySearch {
    public static int search(List<Integer> values, int target) {
        var left = 0;
        var right = values.size() - 1;
        while (left <= right) {
            var mid = (int)Math.floor((left + right) / 2);
            if (values.get(mid) < target) {
                left = mid + 1;
            } else if (values.get(mid) > target) {
                right = mid - 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
}
