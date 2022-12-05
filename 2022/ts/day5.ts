import { assert } from "./deps.ts";
import { readLines } from "./utils.ts";

export function parseStacks(lines: string[]): Stacks {
  const stacks: Stacks = [[], [], [], [], [], [], [], [], [], []];
  lines.forEach((line) => {
    let stackIndex = 0;
    for (let i = 0; i < line.length; ++i) {
      if (
        i < line.length - 3 &&
        line[i] + line[i + 1] + line[i + 2] + line[i + 3] === "    "
      ) {
        stackIndex++;
        i += 3;
        continue;
      } else if (line[i] === "[") {
        stacks[stackIndex].push(line[i + 1]);
        stackIndex++;
        // i += 2;
      }
    }
    return line;
  });

  for (const stack of stacks) {
    stack.reverse();
  }

  return stacks;
}

export function parseInstructions(lines: string[]): Instruction[] {
  return lines.map((line) => {
    const tokens = line.split(" ");
    return {
      move: parseInt(tokens[1]),
      from: parseInt(tokens[3]),
      to: parseInt(tokens[5]),
    };
  });
}

export function parse(lines: string[]): [Stacks, Instruction[]] {
  const stackLines = [];
  const instructionLines = [];
  let isStack = true;
  for (const line of lines) {
    if (line.length === 0) {
      isStack = false;
      continue;
    }
    if (isStack) {
      stackLines.push(line);
    } else {
      instructionLines.push(line);
    }
  }
  // remove index line
  stackLines.pop();
  return [parseStacks(stackLines), parseInstructions(instructionLines)];
}

type Instruction = { move: number; from: number; to: number };
type Stack = string[];
type Stacks = Stack[];

export function applyInstruction(
  stacks: Stacks,
  instruction: Instruction,
): Stacks {
  const { move, from, to } = instruction;

  const tmp = [];
  for (let i = 0; i < move; ++i) {
    tmp.push(stacks[from - 1].pop() || "");
  }

  for (let i = 0; i < tmp.length; ++i) {
    stacks[to - 1].push(tmp[i]);
  }

  return stacks;
}

export function applyInstructions(
  stacks: Stacks,
  instructions: Instruction[],
  applyFunc = applyInstruction,
): Stacks {
  for (const instruction of instructions) {
    stacks = applyFunc(stacks, instruction);
  }
  return stacks;
}

export function getTop(stacks: Stacks): string {
  let result = "";
  for (const stack of stacks) {
    result += stack.length > 0 ? stack[stack.length - 1] : "";
  }
  return result;
}

export function run1(lines: string[]): string {
  const [stacks, instructions] = parse(lines);
  const resultStacks = applyInstructions(stacks, instructions);
  return getTop(resultStacks);
}

function part1() {
  const lines = readLines("../inputs/input5");
  const part1 = run1(lines);
  console.log(`Part 1: ${part1}`);
}

part1();

export function applyInstruction2(
  stacks: Stacks,
  instruction: Instruction,
): Stacks {
  const { move, from, to } = instruction;

  const tmp = [];
  for (let i = 0; i < move; ++i) {
    tmp.push(stacks[from - 1].pop() || "");
  }

  tmp.reverse();

  for (let i = 0; i < tmp.length; ++i) {
    stacks[to - 1].push(tmp[i]);
  }

  return stacks;
}

export function run2(lines: string[]): string {
  const [stacks, instructions] = parse(lines);
  const resultStacks = applyInstructions(
    stacks,
    instructions,
    applyInstruction2,
  );
  return getTop(resultStacks);
}

function part2() {
  const lines = readLines("../inputs/input5");
  const part2 = run2(lines);
  console.log(`Part 2: ${part2}`);
}

part2();
