import * as fs from "fs";

export function read_input(): Array<number> {
  return fs
    .readFileSync("../inputs/input09", "utf8")
    .split("\n")
    .map((line) => line.trim())
    .filter((line) => line.length > 0)
    .map((line) => parseInt(line));
}

function combinations(nums: Array<number>): Array<[number, number]> {
  let s = new Set<String>();

  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = 1; j < nums.length; j++) {
      if (!s.has(`${nums[j]}:${nums[i]}`)) s.add(`${nums[i]}:${nums[j]}`);
    }
  }

  const res = [];
  s.forEach((v) => {
    const tokens = v.split(":");
    res.push([parseInt(tokens[0]), parseInt(tokens[1])]);
  });
  return res;
}

export function is_valid(nums: Array<number>, target: number) {
  const combs = combinations(nums);
  for (let [i, j] of combs) {
    if (i + j == target) return true;
  }
  return false;
}

export function run(nums: Array<number>, preamble: number = 5): number {
  for (let i = 0; i < nums.length - preamble; i++) {
    const end = i + preamble;
    const n = nums.slice(i, end);
    const target = nums[end];
    if (!is_valid(n, target)) return target;
  }
  return 0;
}

function part1() {
  console.log(run(read_input(), 25));
}

function part2() {
  const nums = read_input();
  const target = 88311122;
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      const sum = nums.slice(i, j).reduce((acc, v) => acc + v, 0);
      if (sum == target) {
        console.log(
          Math.min.apply(Math, nums.slice(i, j)) +
            Math.max.apply(Math, nums.slice(i, j))
        );
        return;
      } else if (sum > target) break;
    }
  }
}

part1();
part2();
