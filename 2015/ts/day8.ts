import { readLines } from "./utils.ts";

export function totalNumber(line: string): number {
  return line.length;
}

export function memoryNumber(line: string): number {
  const tokens = line.split("");
  let count = 0;
  for (let i = 0; i < tokens.length - 1; ++i) {
    const a = tokens[i];
    const b = tokens[i + 1];
    if (a === "\\") {
      if (b === "\\") {
        count++;
        i++;
      } else if (b === '"') {
        count++;
        i++;
      } else if (b === "x") {
        if (i < tokens.length - 3) {
          count++;
          i += 3;
        }
      }
    } else if (a === '"') {
      continue;
    } else {
      count++;
    }
  }

  return count;
}

export function representation(lines: string[]): number {
  const result: [number, number] = lines.filter((line) => line.length > 0)
    .reduce((acc, line) => {
      return [acc[0] + totalNumber(line), acc[1] + memoryNumber(line)];
    }, [0, 0]);
  return result[0] - result[1];
}

function part1() {
  const part1 = representation(readLines("../inputs/input08"));
  console.log(`Part 1: ${part1}`);
}

part1();

export function encode(line: string): number {
  const tokens = line.split("");
  let count = 0;
  for (let i = 0; i < tokens.length; ++i) {
    const a = tokens[i];
    const b = tokens[i + 1];
    if (a === "\\") {
      if (b === "\\") {
        count += 4;
        i++;
      } else if (b === '"') {
        count += 4;
        i++;
      } else if (b === "x") {
        if (i < tokens.length - 3) {
          const c = String.fromCharCode(parseInt(
            "0" + tokens[i + 1] + tokens[i + 2] + tokens[i + 3],
            16,
          ));
          count += 5;
          i += 3;
        }
      }
    } else if (a === '"') {
      count += 3;
    } else {
      count++;
    }
  }
  return count;
}

export function representation2(lines: string[]): number {
  const result: [number, number] = lines.filter((line) => line.length > 0)
    .reduce((acc, line) => {
      return [acc[0] + encode(line), acc[1] + line.length];
    }, [0, 0]);
  return result[0] - result[1];
}

function part2() {
  const part2 = representation2(readLines("../inputs/input08"));
  console.log(`Part 2: ${part2}`);
}

part2();
