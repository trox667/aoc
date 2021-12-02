//
// Created by trox667 on 01.12.21.
//

#include <vector>
#include <string>

namespace day1 {
    int part1(const std::vector<std::string> &lines) {
        std::vector<int> depths(lines.size());
        std::transform(lines.cbegin(), lines.cend(), depths.begin(),
                       [](const std::string &line) {
                           return std::stoi(line);
                       });
        int count = 0;
        for(auto i = 1; i < depths.size(); ++i) {
            if (depths[i-1] < depths[i]) count++;
        }
        return count;
    }

    int part2(const std::vector<std::string> &lines) {
        std::vector<int> depths(lines.size());
        std::transform(lines.cbegin(), lines.cend(), depths.begin(),
                       [](const std::string &line) {
                           return std::stoi(line);
                       });
        int count = 0;
        for(auto i = 3; i < depths.size(); ++i) {
            if (depths[i-3] < depths[i]) count++;
        }
        return count;
    }
}