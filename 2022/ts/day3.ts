import { assert } from "./deps.ts";
import { readLines } from "./utils.ts";

export function parse(line: string): string[] {
  assert(line.length % 2 === 0, "Compartments are not equally sized");

  const mid = line.length / 2;
  return [line.substring(0, mid), line.substring(mid)];
}

function score(token: string): number {
  const code = token.charCodeAt(0);
  if (code >= 97 && code <= 122) {
    return code - 96;
  } else if (code >= 65 && code <= 90) {
    return code - 38;
  }
  return 0;
}

function findItem(tokens: string[]): number {
  assert(tokens.length >= 2, "findItem got not enough items");
  const [first, second] = tokens;
  for (const token of first) {
    if (second.includes(token)) {
      return score(token);
    }
  }
  return 0;
}

export function run(lines: string[]): number[] {
  return lines.map((line) => findItem(parse(line)));
}

function part1() {
  const part1 = run(readLines("../inputs/input3")).reduce(
    (acc, value) => acc + value,
    0,
  );
  console.log(`Part 1: ${part1}`);
}

part1();

function findItemThreeTimes(tokens: string[]): number {
  assert(tokens.length >= 3, "findItemThreeItems got not enough items");
  const [first, second, third] = tokens;
  for (const token of first) {
    if (second.includes(token) && third.includes(token)) {
      return score(token);
    }
  }
  return 0;
}

export function run2(lines: string[]): number[] {
  const scores = [];
  for (let i = 0; i < lines.length; i += 3) {
    const score = findItemThreeTimes([lines[i], lines[i + 1], lines[i + 2]]);
    scores.push(score);
  }
  return scores;
}

function part2() {
  const part2 = run2(readLines("../inputs/input3")).reduce(
    (acc, value) => acc + value,
    0,
  );
  console.log(`Part 2: ${part2}`);
}

part2();
