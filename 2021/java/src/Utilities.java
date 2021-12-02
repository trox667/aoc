import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

public class Utilities {
    public static class Tuple<T> {
        public final T a;
        public final T b;

        public Tuple(T a, T b) {
            this.a = a;
            this.b = b;
        }
    }

    public static List<String> read_lines(Path path) throws IOException {
        return Files.readAllLines(path);
    }

    public static Stream<Tuple<String>> zip(List<String> a, List<String> b) throws Exception {
        if (a.size() != b.size()) throw new Exception("Could not zip lists, different size");
        List<Tuple<String>> c = new ArrayList<>();
        for (var i = 0; i < a.size(); ++i) {
            c.add(new Tuple<String>(a.get(i), b.get(i)));
        }
        return c.stream();
    }
}
