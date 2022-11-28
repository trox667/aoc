import { readLines } from "./utils.ts";

export type Instruction = {
  op: "and" | "assign" | "not" | "or" | "lshift" | "rshift";
  a: string | number;
  b: string | number;
};

function parseValue(token: string): string | number {
  if (!Number.isNaN(parseInt(token))) {
    return parseInt(token);
  } else {
    return token;
  }
}

function toInstruction(line: string): [string, Instruction] {
  const tokens = line.split(" ");
  if (line.includes("AND")) {
    return [tokens[4], {
      op: "and",
      a: parseValue(tokens[0]),
      b: parseValue(tokens[2]),
    }];
  } else if (line.includes("OR")) {
    return [tokens[4], {
      op: "or",
      a: parseValue(tokens[0]),
      b: parseValue(tokens[2]),
    }];
  } else if (line.includes("LSHIFT")) {
    return [tokens[4], {
      op: "lshift",
      a: parseValue(tokens[0]),
      b: parseValue(tokens[2]),
    }];
  } else if (line.includes("RSHIFT")) {
    return [tokens[4], {
      op: "rshift",
      a: parseValue(tokens[0]),
      b: parseValue(tokens[2]),
    }];
  } else if (line.includes("NOT")) {
    return [tokens[3], { op: "not", a: parseValue(tokens[1]), b: "" }];
  } else {
    return [tokens[2], { op: "assign", a: parseValue(tokens[0]), b: "" }];
  }
}

export function parse(lines: string[]): Map<string, Instruction> {
  const instructions = new Map<string, Instruction>();

  lines.forEach((line) => {
    const [target, instruction] = toInstruction(line);
    instructions.set(target, instruction);
  });

  return instructions;
}

function getValue(value: string | number): number | undefined {
  if (typeof value === "number") {
    return value;
  } else {
    return stack.get(value);
  }
}

function applyInstruction(
  target: string,
  instruction: Instruction,
  instructions: Map<string, Instruction>,
): number {
  switch (instruction.op) {
    case "assign": {
      const value = getValue(instruction.a);
      if (value !== undefined) {
        stack.set(target, value);
        instructions.delete(target);
      }
      break;
    }
    case "and": {
      const aValue = getValue(instruction.a);
      const bValue = getValue(instruction.b);

      if (aValue !== undefined && bValue !== undefined) {
        stack.set(target, aValue & bValue);
        instructions.delete(target);
      }
      break;
    }
    case "or": {
      const aValue = getValue(instruction.a);
      const bValue = getValue(instruction.b);

      if (aValue !== undefined && bValue !== undefined) {
        stack.set(target, aValue | bValue);
        instructions.delete(target);
      }
      break;
    }
    case "lshift": {
      const aValue = getValue(instruction.a);
      const bValue = getValue(instruction.b);

      if (aValue !== undefined && bValue !== undefined) {
        stack.set(target, aValue << bValue);
        instructions.delete(target);
      }
      break;
    }
    case "rshift": {
      const aValue = getValue(instruction.a);
      const bValue = getValue(instruction.b);

      if (aValue !== undefined && bValue !== undefined) {
        stack.set(target, aValue >> bValue);
        instructions.delete(target);
      }
      break;
    }
    case "not": {
      const aValue = getValue(instruction.a);
      if (aValue !== undefined) {
        stack.set(target, ~aValue & 0xffff);
        instructions.delete(target);
      }
      break;
    }
  }

  return stack.get(target) ?? 0;
}

export function applyInstructions(
  instructions: Map<string, Instruction>,
): Map<string, number> {
  while (instructions.size > 0) {
    for (const [target, instruction] of instructions.entries()) {
      if (applyInstruction(target, instruction, instructions) !== 0) break;
    }
  }
  return stack;
}

const stack = new Map<string, number>();

function part1() {
  stack.clear();
  const instructions = parse(readLines("../inputs/input07"));
  applyInstructions(instructions);
  const part1 = stack.get("a");
  console.log(`Part 1: ${part1}`);
}

part1();

function part2() {
  stack.clear();
  const instructions = parse(readLines("../inputs/input07"));
  instructions.set("b", {
    op: "assign",
    a: 3176,
    b: "",
  });
  applyInstructions(instructions);
  const part2 = stack.get("a");
  console.log(`Part 2: ${part2}`);
}

part2();
