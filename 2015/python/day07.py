import unittest
import ctypes
import copy


class Circuit:
    def __init__(self):
        self.signals = dict()
        self.deps = dict()
        self.ops = dict()


def parse(circuit, line):
    value, target = line.split(' -> ')
    if 'AND' in line:
        dep1, dep2 = value.split(' AND ')

        def op(x, y):
            return x & y

        circuit.deps[target] = [dep1, dep2]
        circuit.ops[target] = op
    elif 'OR' in line:
        dep1, dep2 = value.split(' OR ')

        def op(x, y):
            return x | y

        circuit.deps[target] = [dep1, dep2]
        circuit.ops[target] = op
    elif 'LSHIFT' in line:
        dep, count = value.split(' LSHIFT ')

        def op(x):
            return x << int(count)

        circuit.deps[target] = [dep]
        circuit.ops[target] = op
    elif 'RSHIFT' in line:
        dep, count = value.split(' RSHIFT ')

        def op(x):
            return x >> int(count)

        circuit.deps[target] = [dep]
        circuit.ops[target] = op
    elif 'NOT' in line:
        dep = value.lstrip('NOT ')

        def op(x):
            return ctypes.c_uint16(~x).value

        circuit.ops[target] = op
        circuit.deps[target] = [dep]
    else:
        try:
            circuit.signals[target] = int(value)
        except ValueError:
            circuit.deps[target] = [value]


def run(circuit):
    while len(circuit.deps) > 0:
        solved = False
        solved_key = ''
        for key in circuit.deps:
            deps = circuit.deps[key]
            if all(i != None for i in
                   [circuit.signals.get(d) for d in deps
                    if not d.isnumeric()]):
                signals = [
                    signal
                    for signal in [circuit.signals.get(d) for d in deps]
                    if signal != None
                ]
                for signal in [int(nc) for nc in deps if nc.isnumeric()]:
                    signals.append(signal)
                if len(signals) == 2:
                    circuit.signals[key] = circuit.ops[key](signals[0],
                                                            signals[1])
                elif len(signals) == 1:
                    op = circuit.ops.get(key)
                    if op != None:
                        circuit.signals[key] = op(signals[0])
                    else:
                        circuit.signals[key] = signals[0]
                elif len(signals) == 0:
                    circuit.signals[key] = circuit.ops[key]()
                solved = True
                solved_key = key
                break
        if solved:
            if solved_key in circuit.ops:
                del circuit.ops[solved_key]
            del circuit.deps[solved_key]
            solved_key = ''
            solved = False


def part1():
    circuit = Circuit()
    with open('../inputs/input07') as input:
        for i in input:
            parse(circuit, i.strip())
    run(circuit)
    print(circuit.signals['a'])


def run2():
    pass


def part2():
    circuit = Circuit()
    with open('../inputs/input07') as input:
        for i in input:
            parse(circuit, i.strip())
    circuit2 = copy.deepcopy(circuit)
    run(circuit)
    a = circuit.signals['a']
    circuit2.signals['b'] = a
    if 'b' in circuit2.ops:
        del circuit2.ops['b']
    if 'b' in circuit2.deps:
        del circuit2.deps['b']
    run(circuit2)
    print(circuit2.signals['a'])


def read_input():
    with open('input') as input:
        pass
    pass


class TestPart1(unittest.TestCase):
    def test_parse(self):
        circuit = Circuit()
        parse(circuit, '123 -> x')
        self.assertEqual(circuit.signals['x'], 123)
        parse(circuit, '456 -> y')
        self.assertEqual(circuit.signals['y'], 456)

        parse(circuit, 'x AND y -> d')
        self.assertIsNotNone(circuit.ops['d'])
        self.assertEqual(circuit.deps['d'], ['x', 'y'])

        parse(circuit, 'x OR y -> e')
        self.assertIsNotNone(circuit.ops['e'])
        self.assertEqual(circuit.deps['e'], ['x', 'y'])

        parse(circuit, 'x LSHIFT 2 -> f')
        self.assertIsNotNone(circuit.ops['f'])
        self.assertEqual(circuit.deps['f'], ['x'])

        parse(circuit, 'y RSHIFT 2 -> g')
        self.assertIsNotNone(circuit.ops['g'])
        self.assertEqual(circuit.deps['g'], ['y'])

        parse(circuit, 'NOT x -> h')
        self.assertIsNotNone(circuit.ops['h'])
        self.assertEqual(circuit.deps['h'], ['x'])

        parse(circuit, 'NOT y -> i')
        self.assertIsNotNone(circuit.ops['i'])
        self.assertEqual(circuit.deps['i'], ['y'])

    def test_run(self):
        circuit = Circuit()

        parse(circuit, '123 -> x')
        self.assertEqual(circuit.signals['x'], 123)

        parse(circuit, '456 -> y')
        self.assertEqual(circuit.signals['y'], 456)

        parse(circuit, 'x AND y -> d')
        parse(circuit, 'x OR y -> e')
        parse(circuit, 'x LSHIFT 2 -> f')
        parse(circuit, 'y RSHIFT 2 -> g')
        parse(circuit, 'NOT x -> h')
        parse(circuit, 'NOT y -> i')

        run(circuit)
        self.assertEqual(circuit.signals['d'], 72)
        self.assertEqual(circuit.signals['e'], 507)
        self.assertEqual(circuit.signals['f'], 492)
        self.assertEqual(circuit.signals['g'], 114)
        self.assertEqual(circuit.signals['h'], 65412)
        self.assertEqual(circuit.signals['i'], 65079)
        self.assertEqual(circuit.signals['x'], 123)
        self.assertEqual(circuit.signals['y'], 456)


class TestPart2(unittest.TestCase):
    def test_run2(self):
        pass


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
