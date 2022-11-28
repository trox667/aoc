// 1000x1000 grid values [0;1]
// instructions changing values inclusive
// turn on x,y through x,y
// turn off x,y through x,y

import { readLines } from "./utils.ts";

// toggle x,y through x,y
const WIDTH = 1000;
const HEIGHT = 1000;

enum InstructionKind {
  ON,
  OFF,
  TOGGLE,
}

type Point = { x: number; y: number };

type Instruction = { kind: InstructionKind; from: Point; to: Point };

const grid = new Uint8Array(WIDTH * HEIGHT);

function dumpGrid() {
  for (let y = 0; y < HEIGHT; ++y) {
    const line = [];
    for (let x = 0; x < WIDTH; ++x) {
      const index = pointToIndex({ x, y });
      line.push(grid[index]);
    }
    console.log(line.join(""));
  }
}

function countLit(): number {
  let count = 0;
  for (let i = 0; i < grid.length; ++i) {
    if (grid[i] === 1) count++;
  }

  return count;
}

function countBrightness(): number {
  let count = 0;
  for (let i = 0; i < grid.length; ++i) {
    count += grid[i];
  }
  return count;
}

function pointToIndex(point: Point): number {
  return point.x + point.y * WIDTH;
}

function toInstruction(line: string): Instruction {
  const instructionKind = line.startsWith("turn on")
    ? InstructionKind.ON
    : line.startsWith("turn off")
    ? InstructionKind.OFF
    : InstructionKind.TOGGLE;
  const tokens = line.split(" ");
  let skip = 0;
  switch (instructionKind) {
    case InstructionKind.ON:
      skip = 2;
      break;
    case InstructionKind.OFF:
      skip = 2;
      break;
    case InstructionKind.TOGGLE:
      skip = 1;
      break;
  }

  const from = tokens[skip].split(",").map((value) => parseInt(value));
  const to = tokens[skip + 2].split(",").map((value) => parseInt(value));
  return {
    kind: instructionKind,
    from: { x: from[0], y: from[1] },
    to: { x: to[0], y: to[1] },
  };
}

function applyInstruction(instruction: Instruction) {
  const { kind, from, to } = instruction;
  for (let y = from.y; y <= to.y; ++y) {
    for (let x = from.x; x <= to.x; ++x) {
      const index = pointToIndex({ x, y });
      switch (kind) {
        case InstructionKind.ON:
          grid[index] = 1;
          break;
        case InstructionKind.OFF:
          grid[index] = 0;
          break;
        case InstructionKind.TOGGLE:
          grid[index] = grid[index] === 0 ? 1 : 0;
          break;
      }
    }
  }
}

function part1() {
  grid.fill(0, 0, WIDTH * HEIGHT);
  readLines("../inputs/input06").map((line) => toInstruction(line)).forEach(
    (instruction) => applyInstruction(instruction),
  );
  console.log(`Part 1: ${countLit()}`);
}

part1();

function applyInstruction2(instruction: Instruction) {
  const { kind, from, to } = instruction;
  for (let y = from.y; y <= to.y; ++y) {
    for (let x = from.x; x <= to.x; ++x) {
      const index = pointToIndex({ x, y });
      switch (kind) {
        case InstructionKind.ON:
          grid[index] += 1;
          break;
        case InstructionKind.OFF:
          grid[index] = Math.max(0, grid[index] - 1);
          break;
        case InstructionKind.TOGGLE:
          grid[index] += 2;
          break;
      }
    }
  }
}

function part2() {
  grid.fill(0, 0, WIDTH * HEIGHT);
  readLines("../inputs/input06").map((line) => toInstruction(line)).forEach(
    (instruction) => applyInstruction2(instruction),
  );
  console.log(`Part 2: ${countBrightness()}`);
}

part2();
