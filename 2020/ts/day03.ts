import * as fs from "fs";

export function read_input(): Array<string> {
  return fs
    .readFileSync("../inputs/input03", "utf8")
    .split("\n")
    .map((line) => line);
}

function run(grid, dx = 3, dy = 1) {
  let y = 0;
  let x = 0;
  let hits = 0;

  while (y + dy < grid.length) {
    if (grid[y][x % grid[y].length] == "#") hits++;
    x += dx;
    y += dy;
  }
  return hits;
}

function part1() {
  console.log(run(read_input()));
}

function part2() {
  const grid = read_input();
  console.log(
    run(grid, 1, 1) *
      run(grid) *
      run(grid, 5, 1) *
      run(grid, 7, 1) *
      run(grid, 1, 2)
  );
}

part1();
part2();
