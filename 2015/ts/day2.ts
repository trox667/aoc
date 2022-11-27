import { readLines } from "./utils.ts";

export type BoxDimension = { length: number; width: number; height: number };

export function parse(lines: string[]): BoxDimension[] {
  return lines.map((line: string) => {
    return line.split("x").map((value) => parseInt(value));
  }).filter((values) => values.length === 3)
    .map((values) => {
      return { length: values[0], width: values[1], height: values[2] };
    });
}

export function boxSurfaceArea(boxDimension: BoxDimension): number {
  return 2 * boxDimension.length * boxDimension.width +
    2 * boxDimension.width * boxDimension.height +
    2 * boxDimension.height * boxDimension.length;
}

export function extraPaper(boxDimension: BoxDimension): number {
  return Math.min(
    boxDimension.length * boxDimension.width,
    boxDimension.width * boxDimension.height,
    boxDimension.height * boxDimension.length,
  );
}

export function ribbon(boxDimension: BoxDimension): number {
  return Math.min(
    2 * (boxDimension.length + boxDimension.width),
    2 * (boxDimension.width + boxDimension.height),
    2 * (boxDimension.height + boxDimension.length),
  );
}

export function bowRibbon(boxDimension: BoxDimension): number {
  return boxDimension.length * boxDimension.width * boxDimension.height;
}

export function part1(): number {
  return parse(readLines("../inputs/input02")).reduce(
    (acc, boxDimension) => {
      return acc + boxSurfaceArea(boxDimension) + extraPaper(boxDimension);
    },
    0,
  );
}

export function part2(): number {
  return parse(readLines("../inputs/input02")).reduce(
    (acc, boxDimension) => {
      return acc + ribbon(boxDimension) + bowRibbon(boxDimension);
    },
    0,
  );
}

console.log(`Part1: ${part1()}`);
console.log(`Part2: ${part2()}`);
