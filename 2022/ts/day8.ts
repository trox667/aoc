import { assert } from "./deps.ts";
import { readLines } from "./utils.ts";

export function run(lines: string[]): number {
  let result = 0;

  const treeGrid = lines.map((line) =>
    line.split("").map((token) => parseInt(token))
  );

  const visibleGrid: boolean[][] = [];
  for (let y = 0; y < treeGrid.length; ++y) {
    const row = [];
    for (let x = 0; x < treeGrid[y].length; ++x) {
      row.push(false);
    }
    visibleGrid.push(row);
  }

  const mark = (x: number, y: number, max: number): number => {
    const tree = treeGrid[y][x];
    const visible = visibleGrid[y][x];
    if (tree > max) {
      max = tree;
      if (!visible) {
        visibleGrid[y][x] = true;
      }
    }
    return max;
  };

  for (let y = 0; y < treeGrid.length; ++y) {
    let currMax = -1;
    for (let x = 0; x < treeGrid[y].length; ++x) {
      currMax = mark(x, y, currMax);
    }
    currMax = -1;
    for (let x = treeGrid[y].length - 1; x >= 0; --x) {
      currMax = mark(x, y, currMax);
    }
  }

  for (let x = 0; x < treeGrid[0].length; ++x) {
    let currMax = -1;
    for (let y = 0; y < treeGrid.length; ++y) {
      currMax = mark(x, y, currMax);
    }
    currMax = -1;
    for (let y = treeGrid.length - 1; y >= 0; --y) {
      currMax = mark(x, y, currMax);
    }
  }

  for (let y = 0; y < visibleGrid.length; ++y) {
    for (let x = 0; x < visibleGrid[y].length; ++x) {
      if (visibleGrid[y][x]) {
        result++;
      }
    }
  }

  return result;
}

function part1() {
  const part1 = run(
    readLines("../inputs/input8").filter((line) => line.length > 0),
  );
  console.log(`Part 1: ${part1}`);
}

part1();

export function run2(lines: string[]): number {
  let result = 0;

  const treeGrid = lines.map((line) =>
    line.split("").map((token) => parseInt(token))
  );

  for (let y = 0; y < treeGrid.length; ++y) {
    for (let x = 0; x < treeGrid[y].length; ++x) {
      const tree = treeGrid[y][x];

      let countUp = 0;
      for (let ys = y - 1; ys >= 0; --ys) {
        const currTree = treeGrid[ys][x];
        if (currTree < tree) {
          countUp++;
        } else {
          countUp++;
          break;
        }
      }

      let countBottom = 0;
      for (let ys = y + 1; ys < treeGrid.length; ++ys) {
        const currTree = treeGrid[ys][x];
        if (currTree < tree) {
          countBottom++;
        } else {
          countBottom++;
          break;
        }
      }

      let countLeft = 0;
      for (let xs = x - 1; xs >= 0; --xs) {
        const currTree = treeGrid[y][xs];
        if (currTree < tree) {
          countLeft++;
        } else {
          countLeft++;
          break;
        }
      }

      let countRight = 0;
      for (let xs = x + 1; xs < treeGrid[y].length; ++xs) {
        const currTree = treeGrid[y][xs];
        if (currTree < tree) {
          countRight++;
        } else {
          countRight++;
          break;
        }
      }
      const score = countUp * countLeft * countRight * countBottom;
      result = Math.max(result, score);
    }
  }

  return result;
}

function part2() {
  const part2 = run2(
    readLines("../inputs/input8").filter((line) => line.length > 0),
  );
  console.log(`Part 2: ${part2}`);
}

part2();
