import { assert } from "./deps.ts";
import { readLines } from "./utils.ts";

function run(step: number): number {
  const lines = readLines("../inputs/input6").filter((line) => line.length > 0);
  assert(lines.length > 0);
  const line = lines[0];

  for (let i = step; i < line.length; ++i) {
    const uniqueCharacters = new Set(line.substring(i - step, i).split(""));
    if (uniqueCharacters.size === step) {
      return i;
    }
  }
  return 0;
}

function part1() {
  console.log(`Part 1: ${run(4)}`);
}

part1();

function part2() {
  console.log(`Part 2: ${run(14)}`);
}

part2();
