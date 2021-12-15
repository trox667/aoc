//
// Created by trox667 on 15.12.21.
//

#include "day_15.hpp"
#include <map>
#include <limits>
#include <queue>

namespace day15 {
    using Point = std::pair<int, int>;
    using Grid = std::vector<std::vector<int>>;
    using Graph = std::map<int, std::vector<std::pair<int, int>>>;

    [[nodiscard]] int index(int x, int y, int width) {
        return y * width + x;
    }

    [[nodiscard]] std::vector<Point>
    get_neighbors(int x, int y, int width, int height) {
        auto n = std::vector<Point>{};
        if (x - 1 >= 0) n.emplace_back(x - 1, y);
        if (x + 1 < width) n.emplace_back(x + 1, y);
        if (y - 1 >= 0) n.emplace_back(x, y - 1);
        if (y + 1 < height) n.emplace_back(x, y + 1);
        return n;
    }

    [[nodiscard]] Grid build_grid(const std::vector<std::string> &lines) {
        auto grid = Grid{};
        auto x = 0;
        auto y = 0;
        for (const auto &line: lines) {
            std::vector<int> row{};
            for (const auto &c: line) {
                row.emplace_back(c - '0');
                x += 1;
            }
            grid.emplace_back(row);
            y += 1;
        }
        return grid;
    }

    [[nodiscard]] Grid build_grid2(const std::vector<std::string> &lines) {
        auto grid = Grid{};
        auto y = 0;
        for (const auto &line: lines) {
            std::vector<int> row{};
            auto x = 0;
            for (const auto &c: line) {
                row.emplace_back(c - '0');
                x += 1;
            }
            auto curr_row = row;
            for (auto i = 1; i < 5; ++i) {
                auto prev_row = curr_row;
                curr_row.clear();
                for (const auto& j: prev_row) {
                    auto value = j + 1 > 9 ? 1 : j + 1;
                    curr_row.emplace_back(value);
                    x += 1;
                }
                for (const auto &v: curr_row) row.emplace_back(v);
            }

            grid.emplace_back(row);
            y += 1;
        }

        auto height = grid.size();
        for (auto i = 1; i < 5; ++i) {
            auto s = (i - 1) * height;
            auto e = i * height;
            for(auto r = s; r < e; ++r) {
                auto row = grid[r];
                auto curr_row = std::vector<int>{};
                for (const auto& j: row) {
                    auto value = j + 1 > 9 ? 1 : j + 1;
                    curr_row.emplace_back(value);
                }
                grid.emplace_back(curr_row);
            }
        }

        return grid;
    }

    [[nodiscard]] Graph build_graph(const Grid &grid) {
        auto graph = Graph{};
        auto height = static_cast<int>(grid.size());
        auto width = static_cast<int>(grid[0].size());
        for (auto y = 0; y < height; ++y) {
            for (auto x = 0; x < width; ++x) {
                auto node_from = index(x, y, width);
                const auto neighbors = get_neighbors(x, y,
                                                     width, height);
                for (const auto &neighbor: neighbors) {
                    auto node_to = index(neighbor.first, neighbor.second,
                                         width);
                    auto value = grid[neighbor.second][neighbor.first];
                    graph[node_from].emplace_back(node_to, value);
                }
            }
        }
        return graph;
    }

    [[nodiscard]] int dijkstra(const int start, const int end, Graph &graph) {
        auto node_count = graph.size();
        auto distances = std::vector<int>(node_count,
                                          std::numeric_limits<int>::max());
        distances[start] = 0;
        auto visited = std::vector<int>(node_count, false);

        auto pq = std::priority_queue<std::pair<int, int>>{};
        pq.push(std::make_pair(0, start));

        while (!pq.empty()) {
            auto node = pq.top().second;
            pq.pop();

            if (visited[node]) continue;
            visited[node] = true;
            for (const auto &item: graph[node]) {
                const auto neighbor = item.first;
                const auto distance = item.second;
                const auto total_dist = distances[node] + distance;
                if (total_dist < distances[neighbor]) {
                    distances[neighbor] = total_dist;
                    // c++ priority_queue is max based, so use the negative value
                    pq.push(std::make_pair(-distances[neighbor], neighbor));
                }
            }
        }
        return distances[end];
    }

    [[nodiscard]] long part1(const std::vector<std::string> &lines) {
        auto test = std::vector<std::string>{
                "1163751742",
                "1381373672",
                "2136511328",
                "3694931569",
                "7463417111",
                "1319128137",
                "1359912421",
                "3125421639",
                "1293138521",
                "2311944581"
        };
        const auto grid = build_grid(lines);
        auto height = static_cast<int>(grid.size());
        auto width = static_cast<int>(grid[0].size());
        auto graph = build_graph(grid);
        return dijkstra(index(0, 0, width), index(width - 1, height - 1, width),
                        graph);
    }

    [[nodiscard]] long part2(const std::vector<std::string> &lines) {
        const auto grid = build_grid2(lines);
        auto height = static_cast<int>(grid.size());
        auto width = static_cast<int>(grid[0].size());
        auto graph = build_graph(grid);
        return dijkstra(index(0, 0, width), index(width - 1, height - 1, width),
                        graph);
    }
}