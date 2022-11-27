import { readLines } from "./utils.ts";

const lines = readLines("../inputs/input01");

for (const line of lines) {
  const values = line.split("").map((token) => token === ")" ? -1 : 1);
  const part1 = values.reduce(
    (acc, value) => acc + value,
    0,
  );
  let part2 = 0;
  let acc = 0;
  for (let i = 0; i < values.length; ++i) {
    acc += values[i];
    if (acc < 0) {
      part2 = i + 1;
      break;
    }
  }
  console.log(`Part 1: ${part1}`);
  console.log(`Part 2: ${part2}`);
}
