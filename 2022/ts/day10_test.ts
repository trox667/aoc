import { AddOp, NoOp, parse, run, run2 } from "./day10.ts";
import { assertEquals } from "./deps.ts";

const sample = `noop
addx 3
addx -5`.split("\n");

Deno.test("sample parse", () => {
  const expected = [
    new NoOp(),
    new NoOp(),
    new AddOp(3),
    new NoOp(),
    new AddOp(-5),
  ];
  assertEquals(parse(sample), expected);
});

Deno.test("sample run", () => {
  const expected = [5, -1, 0];
  assertEquals(run(parse(sample)), expected);
});

const sample2 = `addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop`.split("\n");

Deno.test("sample run with checks", () => {
  const expected = [240, 17, 13140];
  const checks = new Set([20, 60, 100, 140, 180, 220]);
  assertEquals(run(parse(sample2), checks), expected);
});

Deno.test("sample run2", () => {
  run2(parse([`addx 15`, `addx -11`, `addx 6`, `addx -3`, `addx 5`]));
});

Deno.test("sample run2", () => {
  run2(parse(sample2));
});
