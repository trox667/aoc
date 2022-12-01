import { assert } from "./deps.ts";
import { readLines } from "./utils.ts";

export function parse(lines: string[]): number[] {
  let currentElve = 0;
  const elvesCalories = [];
  for (const line of lines) {
    if (line.length === 0) {
      elvesCalories.push(currentElve);
      currentElve = 0;
    } else {
      currentElve += parseInt(line);
    }
  }
  return elvesCalories;
}

export function mostCalories(elvesCalories: number[]): number {
  assert(elvesCalories.length >= 1, "elvesCalories does not contain any value");
  elvesCalories.sort((a, b) => b - a); // DESC
  return elvesCalories[0];
}

function part1() {
  console.log("Part 1:", mostCalories(parse(readLines("../inputs/input1"))));
}

part1();

export function topThree(elvesCalories: number[]): [number, number, number] {
  assert(
    elvesCalories.length >= 3,
    "elvesCalories does not contain a minimum of three values",
  );
  elvesCalories.sort((a, b) => b - a);
  return [elvesCalories[2], elvesCalories[1], elvesCalories[0]];
}

function part2() {
  console.log(
    "Part 2:",
    topThree(parse(readLines("../inputs/input1"))).reduce(
      (acc, value) => acc + value,
      0,
    ),
  );
}

part2();
