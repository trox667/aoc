import { assert } from "./deps.ts";
import { readLines } from "./utils.ts";

export class NoOp {}
export class AddOp {
  constructor(public value: number) {}
}
export type Op = NoOp | AddOp;

export function parse(lines: string[]): Op[] {
  const instructions = [];
  for (const line of lines) {
    if (line.startsWith("noop")) {
      instructions.push(new NoOp());
    } else if (line.startsWith("addx")) {
      const tokens = line.split(" ");
      instructions.push(new NoOp());
      instructions.push(new AddOp(parseInt(tokens[1])));
    } else {
      console.error(`Wrong input ${line} is not supported`);
      Deno.exit(-1);
    }
  }
  return instructions;
}

export function run(
  ops: Op[],
  check: Set<number> = new Set<number>(),
): [number, number, number] {
  let signalStrength = 0;
  let registerX = 1;
  let cycle = 0;

  ops.forEach((op) => {
    cycle++;
    if (check.has(cycle)) {
      signalStrength += cycle * registerX;
    }
    if (op instanceof AddOp) {
      registerX += op.value;
    }
  });
  return [cycle, registerX, signalStrength];
}

function part1() {
  const [_c, _x, signalStrength] = run(
    parse(readLines("../inputs/input10").filter((line) => line.length > 0)),
    new Set([20, 60, 100, 140, 180, 220]),
  );
  console.log(`Part 1: ${signalStrength}`);
}

part1();

const WIDTH = 40;
const HEIGHT = 6;
const index = (x: number, y: number) => WIDTH * y + x;

export function run2(ops: Op[]) {
  const pixels = new Array(WIDTH * HEIGHT).fill(".");
  let spritePosition = 1;
  let cycle = 0;
  ops.forEach((op) => {
    if (spritePosition === cycle % 40) {
      pixels[cycle] = "#";
    }
    if (cycle > 0 && spritePosition === (cycle - 1) % 40) {
      pixels[cycle] = "#";
    }
    if (cycle < WIDTH * HEIGHT && spritePosition === (cycle + 1) % 40) {
      pixels[cycle] = "#";
    }
    cycle++;

    if (op instanceof AddOp) {
      spritePosition += op.value;
    }
  });
  draw(pixels);
}

function draw(pixels: string[]) {
  for (let y = 0; y < HEIGHT; ++y) {
    const line = [];
    for (let x = 0; x < WIDTH; ++x) {
      line.push(pixels[index(x, y)]);
    }
    console.log(line.join(""));
  }
}

function part2() {
  console.log(`Part 2:`);
  run2(
    parse(readLines("../inputs/input10").filter((line) => line.length > 0)),
  );
}

part2();
