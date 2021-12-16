def load_file():
    with open('../inputs/input16') as file:
        return file.read().strip()


def bin_repr(value, base=2):
    return '{:04b}'.format(int(value, base))


def to_binary(data):
    out = ''
    for c in data:
        out += bin_repr(c, 16).zfill(4)
    out = out
    return out


class Packet:
    def __init__(self):
        self.literals = []
        self.version = 0
        self.type_id = 0
        self.packets = []


def read(data):
    packet = Packet()
    packet.version, data = int(data[:3], 2), data[3:]
    packet.type_id, data = int(data[:3], 2), data[3:]
    if packet.type_id == 4:
        literal = ''
        while data[0] != '0':
            literal, data = literal + bin_repr(data[1:5]), data[5:]
        packet.literals.append(int(literal + bin_repr(data[1:5]), 2))
        data = data[5:]
    else:
        length_type_id, data = data[0], data[1:]
        if length_type_id == '0':
            total_length_in_bits, data = int(data[:15], 2), data[15:]
            bit_count = len(data)
            while bit_count - len(data) < total_length_in_bits:
                subpacket, data = read(data)
                packet.packets.append(subpacket)
        else:
            number_of_packets, data = int(data[:11], 2), data[11:]
            for _ in range(number_of_packets):
                subpacket, data = read(data)
                packet.packets.append(subpacket)
        if packet.type_id == 0:
            s = 0
            for p in packet.packets:
                s += sum(p.literals)
            packet.literals.append(s)
        elif packet.type_id == 1:
            s = 1
            for p in packet.packets:
                for literal in p.literals:
                    s *= literal
            packet.literals.append(s)
        elif packet.type_id == 2:
            literals = []
            for p in packet.packets:
                literals.extend(p.literals)
            packet.literals.append(min(literals))
        elif packet.type_id == 3:
            literals = []
            for p in packet.packets:
                literals.extend(p.literals)
            packet.literals.append(max(literals))
        elif packet.type_id == 5:
            assert len(packet.packets) == 2
            a = packet.packets[0].literals[0]
            b = packet.packets[1].literals[0]
            packet.literals.append(int(a > b))
        elif packet.type_id == 6:
            assert len(packet.packets) == 2
            a = packet.packets[0].literals[0]
            b = packet.packets[1].literals[0]
            packet.literals.append(int(a < b))
        elif packet.type_id == 7:
            assert len(packet.packets) == 2
            a = packet.packets[0].literals[0]
            b = packet.packets[1].literals[0]
            packet.literals.append(int(a == b))
    return packet, data


def sum_versions(packet):
    s = packet.version
    for p in packet.packets:
        s += sum_versions(p)
    return s


def part1():
    data = to_binary(load_file())
    packet, _ = read(data)

    sum_version_numbers = packet.version
    for p in packet.packets:
        sum_version_numbers += sum_versions(p)
    return sum_version_numbers


def part2():
    data = to_binary(load_file())
    data = to_binary("9C0141080250320F1802104A08")
    packet, _ = read(data)
    return packet.literals[0]


print(part1())
print(part2())
