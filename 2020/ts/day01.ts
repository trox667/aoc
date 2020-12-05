import * as fs from "fs";

export function read_input() {
  return fs
    .readFileSync("../inputs/input01", "utf8")
    .split("\n")
    .map((line) => parseInt(line));
}

function part1() {
  const items = read_input();
  for (let i of items) {
    for (let j of items) {
      if (j == i) continue;
      if (i + j == 2020) {
        console.log(i * j);
        return;
      }
    }
  }
}

function part2() {
  const items = read_input();
  for (let i of items) {
    for (let j of items) {
      for (let k of items) {
        if (j == i || i == k || j == k) continue;
        if (i + j + k == 2020) {
          console.log(i * j * k);
          return;
        }
      }
    }
  }
}

part1();
part2();
