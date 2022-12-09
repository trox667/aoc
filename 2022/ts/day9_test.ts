import { applyInstruction, parse, run, run2 } from "./day9.ts";
import { assertEquals } from "./deps.ts";

const sample = ``.split("\n");

Deno.test("sample run", () => {
  const input = ["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2"];
  const instructions = parse(input);
  const result = run(instructions);
  const expected = new Set([
    "0:0",
    "1:0",
    "2:0",
    "3:0",
    "4:1",
    "4:2",
    "4:3",
    "3:4",
    "2:4",
    "1:2",
    "2:2",
    "3:2",
    "3:3",
  ]);
  assertEquals(result, expected);
});

Deno.test("sample run2", () => {
  const input = ["R 5", "U 8", "L 8", "D 3", "R 17", "D 10", "L 25", "U 20"];
  const instructions = parse(input);
  const result = run2(instructions);
  const expected = new Set([
    "0:0",
    "1:1",
    "2:2",
    "1:3",
    "2:4",
    "3:5",
    "4:5",
    "5:5",
    "6:4",
    "7:3",
    "8:2",
    "9:1",
    "10:0",
    "9:-1",
    "8:-2",
    "7:-3",
    "6:-4",
    "5:-5",
    "4:-5",
    "3:-5",
    "2:-5",
    "1:-5",
    "0:-5",
    "-1:-5",
    "-2:-5",
    "-3:-4",
    "-4:-3",
    "-5:-2",
    "-6:-1",
    "-7:0",
    "-8:1",
    "-9:2",
    "-10:3",
    "-11:4",
    "-11:5",
    "-11:6",
  ]);
  assertEquals(result, expected);
});
