import { applyInstruction, applyInstructions, getTop, run1 } from "./day5.ts";
import { assertEquals } from "./deps.ts";

function deepCopy<T>(data: T): T {
  return JSON.parse(JSON.stringify(data));
}

const sample = `    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2`;

const stacks = [
  ["N", "Z"].reverse(),
  ["D", "C", "M"].reverse(),
  ["P"].reverse(),
];

const sampleInstructions = [
  { move: 1, from: 2, to: 1 },
  { move: 3, from: 1, to: 3 },
  { move: 2, from: 2, to: 1 },
  { move: 1, from: 1, to: 2 },
];

Deno.test("sample apply instruction #0", () => {
  // const expected = [["C"], ["M"], ["Z", "N", "D", "P"]];
  const expected = [["Z", "N", "D"], ["M", "C"], ["P"]];
  assertEquals(
    applyInstruction(deepCopy(stacks), sampleInstructions[0]),
    expected,
  );
});

Deno.test("sample apply instructions", () => {
  const expected = [["C"], ["M"], ["P", "D", "N", "Z"]];
  assertEquals(
    applyInstructions(deepCopy(stacks), sampleInstructions),
    expected,
  );
});

Deno.test("sample get top", () => {
  const expected = "CMZ";
  assertEquals(
    getTop(applyInstructions(deepCopy(stacks), sampleInstructions)),
    expected,
  );
});

Deno.test("sample part1", () => {
  const expected = "CMZ";
  assertEquals(
    run1(sample.split("\n")),
    expected,
  );
});
