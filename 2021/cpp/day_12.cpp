//
// Created by trox667 on 12.12.21.
//

#include "day_12.hpp"
#include <map>
#include <iostream>
#include "utils.hpp"

namespace day12 {

    struct Graph {
        Graph() : graph{}, visited{}, current_path{}, paths{} {};

        void add_edge(const std::string &a, const std::string &b) {
            if (!graph.contains(a)) {
                graph[a] = std::vector<std::string>();
            }
            if (!graph.contains(b)) {
                graph[b] = std::vector<std::string>();
            }
            graph[a].emplace_back(b);
            graph[b].emplace_back(a);
        }

        void dfs(const std::string &start, const std::string &end,
                 const bool allow_visit_twice) {
            // TODO: move into lambda parameter
            if (allow_visit_twice) {
                auto visited_twice = 0;
                for (const auto &item: visited) {
                    const auto &value = std::get<1>(item);
                    if (value >= 2) visited_twice++;
                }
                if ((visited_twice && visited[start] >= 1) or
                    ((start == "start" or start == "end") and
                     visited[start] >= 1)) {
                    return;
                }
            } else {
                if (visited.contains(start) && visited[start] == 1) {
                    return;
                }
            }

            if (utils::is_lower(start)) {
                visited[start]++;
            }
            current_path.emplace_back(start);
            if (start == end) {
                paths.emplace_back(current_path);
                visited[start]--;
                current_path.pop_back();
                return;
            }
            for (const auto &neighbor: graph[start]) {
                dfs(neighbor, end, allow_visit_twice);
            }
            current_path.pop_back();
            visited[start]--;
        }

        std::map<std::string, std::vector<std::string>> graph;
        std::map<std::string, int> visited;
        std::vector<std::string> current_path;
        std::vector<std::vector<std::string>> paths;
    };

    std::ostream &operator<<(std::ostream &os, const Graph &graph) {
        for (const auto &item: graph.graph) {
            os << std::get<0>(item);
            os << std::string(" -> ");
            const auto &values = std::get<1>(item);
            for (const auto &value: values) {
                os << value << std::string(", ");
            }
            os << std::string("\n");
        }
        os << std::string("\n");
        return os;
    }

    [[nodiscard]] Graph create_graph(const std::vector<std::string> &lines) {
        auto graph = Graph();
        for (const auto &line: lines) {
            const auto tokens = utils::split(line, '-');
            graph.add_edge(tokens[0], tokens[1]);
        }
        return graph;
    }

    [[nodiscard]] long part1(const std::vector<std::string> &lines) {
        auto graph = create_graph(lines);
        graph.dfs("start", "end", false);
        return static_cast<long>(graph.paths.size());
    }

    [[nodiscard]] long part2(const std::vector<std::string> &lines) {
        auto graph = create_graph(lines);
        graph.dfs("start", "end", true);
        return static_cast<long>(graph.paths.size());
    }
}