//
// Created by trox667 on 16.12.21.
//

#include "utils.hpp"
#include "day_16.hpp"
#include <bitset>
#include <limits>


namespace day16 {
    struct Packet {
        int version;
        int type_id;
        std::vector<long> literals;
        std::vector<Packet> subpackets;

        [[nodiscard]] long sum_literals() {
            auto s = 0L;
            for (const auto &sp: subpackets) {
                for (const auto &lit: sp.literals) {
                    s += lit;
                }
            }
            return s;
        }

        [[nodiscard]] long mul_literals() {
            auto s = 1L;
            for (const auto &sp: subpackets) {
                for (const auto &lit: sp.literals) {
                    s *= lit;
                }
            }
            return s;
        }

        [[nodiscard]] long min_literal() {
            auto m = std::numeric_limits<long>::max();
            for (const auto &sp: subpackets) {
                for (const auto &lit: sp.literals) {
                    if (lit < m) m = lit;
                }
            }
            return m;
        }

        [[nodiscard]] long max_literal() {
            auto m = std::numeric_limits<long>::min();
            for (const auto &sp: subpackets) {
                for (const auto &lit: sp.literals) {
                    if (lit > m) m = lit;
                }
            }
            return m;
        }

        [[nodiscard]] long greater() {
            return subpackets[0].literals[0] > subpackets[1].literals[0] ? 1L
                                                                         : 0L;
        }

        [[nodiscard]] long less() {
            return subpackets[0].literals[0] < subpackets[1].literals[0] ? 1L
                                                                         : 0L;
        }


        [[nodiscard]] long eq() {
            return subpackets[0].literals[0] == subpackets[1].literals[0] ? 1L
                                                                          : 0L;
        }
    };

    [[nodiscard]] std::string
    take_n(int &index, int size, const std::string &data) {
        auto s = data.substr(index, size);
        index += size;
        return s;
    }

    [[nodiscard]] Packet read(int &index, const std::string &data) {
        auto packet = Packet{};
        packet.version = static_cast<int>(utils::int_from_binary_str(
                take_n(index, 3, data)));
        packet.type_id = static_cast<int>(utils::int_from_binary_str(
                take_n(index, 3, data)));
        if (packet.type_id == 4) {
            auto literal = std::string{};
            while (data.at(index) != '0') {
                index++;
                literal += take_n(index, 4, data);
            }
            index++;
            literal += take_n(index, 4, data);
            packet.literals.emplace_back(utils::int_from_binary_str(literal));
        } else {
            auto length_type_id = utils::int_from_binary_str(
                    take_n(index, 1, data));
            if (length_type_id == 0) {
                auto total_length = utils::int_from_binary_str(
                        take_n(index, 15, data));
                auto bit_count = data.size() - index;
                while (bit_count - (data.size() - index) < total_length) {
                    auto subpacket = read(index, data);
                    packet.subpackets.push_back(subpacket);
                }
            } else {
                auto number_of_packets = utils::int_from_binary_str(
                        take_n(index, 11, data));
                for (auto i = 0; i < number_of_packets; ++i) {
                    auto subpacket = read(index, data);
                    packet.subpackets.push_back(subpacket);
                }
            }
            switch (packet.type_id) {
                case 0:
                    packet.literals.emplace_back(packet.sum_literals());
                    break;
                case 1:
                    packet.literals.emplace_back(packet.mul_literals());
                    break;
                case 2:
                    packet.literals.emplace_back(packet.min_literal());
                    break;
                case 3:
                    packet.literals.emplace_back(packet.max_literal());
                    break;
                case 5:
                    packet.literals.emplace_back(packet.greater());
                    break;
                case 6:
                    packet.literals.emplace_back(packet.less());
                    break;
                case 7:
                    packet.literals.emplace_back(packet.eq());
                    break;
            }
        }

        return packet;
    }

    [[nodiscard]] int sum_version(const Packet &packet) {
        auto sum = packet.version;
        for (const auto &p: packet.subpackets) {
            sum += sum_version(p);
        }
        return sum;
    }

    [[nodiscard]] long part1(const std::vector<std::string> &lines) {
        auto data = utils::to_binary(utils::trim(lines[0]));
        auto index = 0;
        auto packet = read(index, data);
        return sum_version(packet);
    }

    [[nodiscard]] long part2(const std::vector<std::string> &lines) {
        auto data = utils::to_binary(utils::trim(lines[0]));
        auto index = 0;
        auto packet = read(index, data);
        return !packet.literals.empty() ? packet.literals[0] : 0;
    }
}
