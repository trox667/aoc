//
// Created by trox667 on 09.12.21.
//

#include "day_9.hpp"
#include <set>

namespace day9 {
    [[nodiscard]] std::vector<int>
    heightmap_from_file(const std::vector<std::string> &lines) {
        auto heightmap = std::vector<int>{};
        for (const auto &line: lines) {
            for (const auto &c: line) {
                heightmap.emplace_back(c - '0');
            }
        }
        return heightmap;
    }

    int index(int x, int y, int width) {
        return y * width + x;
    }

    std::pair<int, int> position(int idx, int width) {
        return std::make_pair(idx % width, idx / width);
    }

    [[nodiscard]] std::vector<int>
    get_neighbors(int x, int y, int width, int height) {
        auto n = std::vector<int>{};
        if (x - 1 >= 0) n.emplace_back(index(x - 1, y, width));
        if (x + 1 < width) n.emplace_back(index(x + 1, y, width));
        if (y - 1 >= 0) n.emplace_back(index(x, y - 1, width));
        if (y + 1 < height) n.emplace_back(index(x, y + 1, width));
        return n;
    }

    [[nodiscard]] std::set<int>
    get_low_points(const std::vector<int> &heightmap, const int width,
                   const int height) {
        auto low_points = std::set<int>();
        for (auto i = 0; i < heightmap.size(); ++i) {
            auto pos = position(i, width);
            auto x = std::get<0>(pos);
            auto y = std::get<1>(pos);
            auto curr_height = heightmap[i];
            if (curr_height == 9) continue;

            auto neighbors = get_neighbors(x, y, width, height);
            auto values = std::vector<int>(neighbors.size());
            std::transform(neighbors.begin(), neighbors.end(), values.begin(),
                           [heightmap](auto a) { return heightmap[a]; });
            auto min = std::min_element(values.begin(), values.end());
            if (curr_height < *min) low_points.insert(i);
        }
        return low_points;
    }

    void
    get_basin(const int idx, const std::vector<int> &heightmap, const int width,
              const int height, std::set<int> &basin, std::set<int> &visited) {
        visited.insert(idx);
        auto pos = position(idx, width);
        auto x = std::get<0>(pos);
        auto y = std::get<1>(pos);
        auto curr_height = heightmap[idx];
        if (curr_height == 9) return;

        basin.insert(idx);

        auto neighbors = get_neighbors(x, y, width, height);
        for (const auto &n: neighbors) {
            if (!visited.contains(n) && heightmap[n] != 9) {
                get_basin(n, heightmap, width, height, basin, visited);
            }
        }
    }

    [[nodiscard]] long part1(const std::vector<std::string> &lines) {
        auto width = lines[0].size();
        auto height = lines.size();
        const auto &heightmap = heightmap_from_file(lines);
        const auto &low_points = get_low_points(heightmap, width, height);
        auto sum = 0;
        for (const auto &low_point: low_points) {
            sum += heightmap[low_point] + 1;
        }
        return sum;
    }

    [[nodiscard]] long part2(const std::vector<std::string> &lines) {
        auto width = lines[0].size();
        auto height = lines.size();
        const auto &heightmap = heightmap_from_file(lines);
        const auto &low_points = get_low_points(heightmap, width, height);
        auto visited = std::set<int>{};
        auto results = std::vector<std::set<int>>{};
        for (const auto &low_point: low_points) {
            auto basin = std::set<int>{};
            get_basin(low_point, heightmap, width, height, basin, visited);
            results.emplace_back(basin);
        }
        std::sort(results.begin(), results.end(),
                  [](const std::set<int> &a, const std::set<int> &b) {
                      return a.size() < b.size();
                  });
        return results[results.size() - 1].size() *
               results[results.size() - 2].size() *
               results[results.size() - 3].size();
    }
}


