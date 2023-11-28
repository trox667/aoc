import io.trox667.aoc.algorithms.Dijkstra;
import io.trox667.aoc.algorithms.Graph;
import io.trox667.aoc.algorithms.Node;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDijkstra {
    // Start: A
    // Neighbors: B (W 14), C (W 9), D (W 7)
    // B:
    // Neighbors: A (W 14), C (W 2), E (W 9)
    // C:
    // Neighbors: A (W 9), B (W 2), D (W 10), F (W 11)
    // D:
    // Neighbors: A (W 7), C (W 10), F (W 15)
    // E:
    // Neighbors: B (W 9), F (W 6)
    // F:
    // Neighbors: C (W 11), D (W 15), E (W 6)
    private Graph graph;

    @BeforeEach
    void buildGraph() {
        this.graph = new Graph();
        graph.insertNode("A", new Node("B", 14));
        graph.insertNode("A", new Node("C", 9));
        graph.insertNode("A", new Node("D", 7));

        graph.insertNode("B", new Node("A", 14));
        graph.insertNode("B", new Node("C", 2));
        graph.insertNode("B", new Node("E", 9));

        graph.insertNode("C", new Node("A", 9));
        graph.insertNode("C", new Node("B", 2));
        graph.insertNode("C", new Node("D", 10));
        graph.insertNode("C", new Node("F", 11));

        graph.insertNode("D", new Node("A", 7));
        graph.insertNode("D", new Node("C", 10));
        graph.insertNode("D", new Node("F", 15));

        graph.insertNode("E", new Node("B", 9));
        graph.insertNode("E", new Node("F", 6));

        graph.insertNode("F", new Node("C", 11));
        graph.insertNode("F", new Node("D", 15));
        graph.insertNode("F", new Node("E", 6));
    }

    @Test
    void testGraph() {
        var reference = new ArrayList<>();
        reference.add(new Node("B", 9));
        reference.add(new Node("F", 6));
        assertEquals(reference, graph.getNeighbors("E"));
    }

    // A -> B -> C -> D -> E
    @Test
    void testAtoE() {
        var dijkstra = new Dijkstra(this.graph);
        var path = dijkstra.findShortestPath("A", "E");
        System.out.println(path);
    }
}
