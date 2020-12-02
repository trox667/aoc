import * as fs from "fs";

export function parse(line: string): [string, string, number, number] {
  const pattern = /(\d+)-(\d+) ([A-z]): ([A-z]+)/g;
  const matches = pattern.exec(line);
  return [matches[4], matches[3], parseInt(matches[1]), parseInt(matches[2])];
}

export function char_count(password: string, letter: string): number {
  return password.split("").filter((c) => c == letter).length;
}

function part1() {
  const input = fs.readFileSync("../inputs/input02", "utf8");
  const inputs = input.split("\n");
  let result = 0;
  for (const input of inputs) {
    if (input.trim().length == 0) continue;

    const entry = parse(input);
    const count = char_count(entry[0], entry[1]);
    if (entry[2] <= count && count <= entry[3]) result++;
  }
  console.log(result);
}

export function char_position(
  password: string,
  letter: string,
  position: number
): boolean {
  return password.charAt(position - 1) == letter;
}

function part2() {
  const input = fs.readFileSync("../inputs/input02", "utf8");
  const inputs = input.split("\n");
  let result = 0;
  for (const input of inputs) {
    if (input.trim().length == 0) continue;

    const entry = parse(input);
    const a = char_position(entry[0], entry[1], entry[2]);
    const b = char_position(entry[0], entry[1], entry[3]);
    if ((a && !b) || (!a && b)) result++;
  }
  console.log(result);
}

part1();
part2();
