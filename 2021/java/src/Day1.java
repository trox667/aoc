import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;

public class Day1 implements Day {
    public static final String INPUT = "../inputs/input01";

    @Override
    public int part1() {
        var count = 0;
        try {
            var lines = Utilities.read_lines(Path.of(INPUT));
            var depths = lines.stream().map(Integer::parseInt).toList();
            for (var i = 1; i < depths.size(); ++i) {
                if (depths.get(i) > depths.get(i - 1)) count++;
            }
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }
        return count;
    }

    @Override
    public int part2() {
        var count = 0;
        try {
            var lines = Utilities.read_lines(Path.of(INPUT));
            var depths = lines.stream().map(Integer::parseInt).toList();
            for (var i = 3; i < depths.size(); ++i) {
                if (depths.get(i) > depths.get(i - 3)) count++;
            }
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }
        return count;
    }
}
