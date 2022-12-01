import { assertEquals } from "./deps.ts";
import { mostCalories, parse, topThree } from "./day1.ts";

const sample = `1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
`.split("\n");

Deno.test("sample parse", () => {
  const expected = [6000, 4000, 11000, 24000, 10000];
  assertEquals(parse(sample), expected);
});

Deno.test("sample part1", () => {
  const expected = 24000;
  assertEquals(mostCalories(parse(sample)), expected);
});

Deno.test("sample part2", () => {
  const expected = [10000, 11000, 24000];
  assertEquals(topThree(parse(sample)), expected);
});
