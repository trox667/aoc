import io.trox667.aoc.algorithms.BinarySearch;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestBinarySearch {
    @Test
    public void testBinarySearch() {
        var input = new Integer[]{1, 2, 3, 4, 5, 6, 7, 8};
        assertEquals(6, BinarySearch.search(Arrays.asList(input), 7));
    }
}
