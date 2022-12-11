import { assert } from "./deps.ts";
import { lcm, readLines } from "./utils.ts";

interface Monkey {
  items: number[];
  op: (old: number) => number;
  div: number;
  testTrue: number;
  testFalse: number;
  handled: number;
}

function toMonkey(monkeyData: string): Monkey {
  const lines = monkeyData.split("\n");
  const items = lines[1].split(": ")[1].split(", ").map((t) => parseInt(t));
  const op = (old: number) => {
    return eval(lines[2].split(" = ")[1].replaceAll("old", `${old}`));
  };
  const div = parseInt(lines[3].split(" by ")[1]);
  const testTrue = parseInt(lines[4].split(" monkey ")[1]);
  const testFalse = parseInt(lines[5].split(" monkey ")[1]);
  const handled = 0;
  return { items, op, div, testTrue, testFalse, handled };
}

function run(monkeys: Monkey[], steps: number, part2 = false): number {
  let modulus = monkeys[0].div;
  for (let i = 1; i < monkeys.length; ++i) {
    modulus = lcm(modulus, monkeys[i].div);
  }
  for (let i = 0; i < steps; ++i) {
    for (const monkey of monkeys) {
      for (const item of monkey.items) {
        let worryLevel = item;
        if (part2) {
          worryLevel = monkey.op(worryLevel) % modulus;
        } else {
          worryLevel = Math.floor(monkey.op(worryLevel) / 3);
        }
        if (worryLevel % monkey.div === 0) {
          monkeys[monkey.testTrue].items.push(worryLevel);
        } else {
          monkeys[monkey.testFalse].items.push(worryLevel);
        }
        monkey.handled++;
        monkey.items = [];
      }
    }
  }
  monkeys.sort((a, b) => b.handled - a.handled);
  return monkeys[0].handled * monkeys[1].handled;
}

function part1() {
  const monkeys = readLines("../inputs/input11", "\n\n").map((chunk) =>
    toMonkey(chunk)
  );
  const part1 = run(monkeys, 20);
  console.log(`Part 1: ${part1}`);
}

part1();

function part2() {
  const monkeys = readLines("../inputs/input11", "\n\n").map((chunk) =>
    toMonkey(chunk)
  );
  const part2 = run(monkeys, 10000, true);
  console.log(`Part 2: ${part2}`);
}

part2();
