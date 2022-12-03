import { parse, run, run2 } from "./day3.ts";
import { assertEquals } from "./deps.ts";

const sample = [
  "vJrwpWtwJgWrhcsFMMfFFhFp",
  "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
  "PmmdzqPrVvPwwTWBwg",
  "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
  "ttgJtRGJQctTZtZT",
  "CrZsJsPPZsGzwwsLwLmpwMDw",
];

Deno.test("sample parse", () => {
  const expected = [
    ["vJrwpWtwJgWr", "hcsFMMfFFhFp"],
    ["jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"],
    ["PmmdzqPrV", "vPwwTWBwg"],
  ];
  for (let i = 0; i < 3; ++i) {
    assertEquals(parse(sample[i]), expected[i]);
  }
});

Deno.test("sample part1", () => {
  const expected = [16, 38, 42, 22, 20, 19];
  assertEquals(run(sample), expected);
  const result = 157;
  assertEquals(run(sample).reduce((acc, value) => acc + value, 0), result);
});

Deno.test("sample part2", () => {
  const expected = [18, 52];
  assertEquals(run2(sample), expected);
  const result = 70;
  assertEquals(run2(sample).reduce((acc, value) => acc + value, 0), result);
});
