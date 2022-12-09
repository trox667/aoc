import { assert } from "./deps.ts";
import { readLines } from "./utils.ts";

type Instruction = [Coordinate, number];
type Coordinate = [number, number];

function coordinateToString(coordinate: Coordinate): string {
  return `${coordinate[0]}:${coordinate[1]}`;
}

function mapDirection(token: string): Coordinate {
  if (token === "U") return [0, 1];
  if (token === "L") return [-1, 0];
  if (token === "R") return [1, 0];
  if (token === "D") return [0, -1];
  return [0, 0];
}

export function parse(lines: string[]): Instruction[] {
  return lines.map((line) => {
    const tokens = line.split(" ");
    return [mapDirection(tokens[0]), parseInt(tokens[1])];
  });
}

function isTouching([hx, hy]: Coordinate, [tx, ty]: Coordinate): boolean {
  return new Set([hx - 1, hx, hx + 1]).has(tx) &&
    new Set([hy - 1, hy, hy + 1]).has(ty);
}

function move(head: Coordinate, tail: Coordinate): Coordinate {
  if (!isTouching(head, tail)) {
    if (head[0] === tail[0] || head[1] === tail[1]) {
      if (head[0] == tail[0]) {
        if (tail[1] > head[1]) {
          tail[1] -= 1;
        } else {
          tail[1] += 1;
        }
      } else {
        if (tail[0] > head[0]) {
          tail[0] -= 1;
        } else {
          tail[0] += 1;
        }
      }
    } else {
      if (head[0] > tail[0]) {
        tail[0] += 1;
      } else {
        tail[0] -= 1;
      }
      if (head[1] > tail[1]) {
        tail[1] += 1;
      } else {
        tail[1] -= 1;
      }
    }
  }
  return tail;
}

export function applyInstruction(
  head: Coordinate,
  tail: Coordinate,
  instruction: Instruction,
): [Coordinate, Coordinate, Set<string>] {
  const positions = new Set<string>();
  for (let i = 0; i < instruction[1]; ++i) {
    head[0] += instruction[0][0];
    head[1] += instruction[0][1];
    tail = move(head, tail);
    positions.add(coordinateToString(tail));
  }
  return [head, tail, positions];
}

export function run(instructions: Instruction[]): Set<string> {
  const positions = new Set<string>();
  let head: Coordinate = [0, 0];
  let tail: Coordinate = [0, 0];
  for (const instruction of instructions) {
    const [h, t, p] = applyInstruction(head, tail, instruction);
    head = h;
    tail = t;
    for (const ip of p) {
      positions.add(ip);
    }
  }
  return positions;
}

function part1() {
  const lines = readLines("../inputs/input9").filter((line) => line.length > 0);
  const instructions = parse(lines);
  const part1 = run(instructions).size;
  console.log(`Part 1: ${part1}`);
}

export function applyInstruction2(
  head: Coordinate,
  tails: Coordinate[],
  instruction: Instruction,
): [Coordinate, Coordinate[], Set<string>] {
  const positions = new Set<string>();
  for (let i = 0; i < instruction[1]; ++i) {
    head[0] += instruction[0][0];
    head[1] += instruction[0][1];

    let prev = head;
    for (let j = 0; j < tails.length; ++j) {
      tails[j] = move(prev, tails[j]);
      prev = tails[j];
      if (j == 8) {
        positions.add(coordinateToString(tails[j]));
      }
    }
  }
  return [head, tails, positions];
}

export function run2(instructions: Instruction[]): Set<string> {
  const positions = new Set<string>();
  let head: Coordinate = [0, 0];
  let tails: Coordinate[] = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
  ];
  for (const instruction of instructions) {
    const [h, t, p] = applyInstruction2(head, tails, instruction);
    head = h;
    tails = t;
    for (const ip of p) {
      positions.add(ip);
    }
  }
  return positions;
}

part1();

function part2() {
  const lines = readLines("../inputs/input9").filter((line) => line.length > 0);
  const instructions = parse(lines);
  const part2 = run2(instructions).size;
  console.log(`Part 2: ${part2}`);
}

part2();
