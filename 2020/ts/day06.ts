import * as fs from "fs";

export function read_input() {
  return fs
    .readFileSync("../inputs/input06", "utf8")
    .split("\n\n")
    .map((line) => line.split("\n"));
}

function part1() {
  console.log(
    read_input().reduce((acc, answers) => {
      const curr_keys = new Set();
      answers.forEach((answer) =>
        answer.split("").forEach((c) => curr_keys.add(c))
      );

      return (acc += curr_keys.size);
    }, 0)
  );
}

function part2() {
  console.log(
    read_input().reduce((acc, answers) => {
      acc += answers
        .map((answer) => answer.split(""))
        .filter((c) => c.length > 0)
        .reduce((a, b) => a.filter((c) => b.includes(c))).length;
      return acc;
    }, 0)
  );
}

part1();
part2();
