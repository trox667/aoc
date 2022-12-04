import { assert } from "./deps.ts";
import { readLines } from "./utils.ts";

type Item = { start: number; end: number };
type Pair = [Item, Item];

function parseItem(token: string): Item {
  const [start, end] = token.split("-");
  return { start: parseInt(start), end: parseInt(end) };
}

export function parse(line: string): Pair {
  const tokens = line.split(",");
  assert(tokens.length >= 2);
  assert(tokens[0].length >= 2);
  assert(tokens[1].length >= 2);
  return [
    parseItem(tokens[0]),
    parseItem(tokens[1]),
  ];
}

export function contains(pair: Pair): boolean {
  const [item1, item2] = pair;
  return (item1.start >= item2.start && item1.end <= item2.end) ||
    (item2.start >= item1.start && item2.end <= item1.end);
}

export function run1(lines: string[]): number {
  return lines.filter((line) => line.length > 0).map((
    line,
  ) => contains(parse(line))).filter((contained) => contained).length;
}

function part1() {
  const part1 = run1(readLines("../inputs/input4"));
  console.log(`Part 1: ${part1}`);
}

part1();

export function overlap(pair: Pair): boolean {
  const [item1, item2] = pair;
  return (item1.start >= item2.start && item1.start <= item2.end ||
    item1.end >= item2.start && item1.end <= item2.end) ||
    (item2.start >= item1.start && item2.start <= item1.end ||
      item2.end >= item1.start && item2.end <= item1.end);
}

export function run2(lines: string[]): number {
  return lines.filter((line) => line.length > 0).map((
    line,
  ) => overlap(parse(line))).filter((contained) => contained).length;
}

function part2() {
  const part2 = run2(readLines("../inputs/input4"));
  console.log(`Part 2: ${part2}`);
}

part2();
