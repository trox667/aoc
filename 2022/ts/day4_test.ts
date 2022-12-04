import { contains, overlap, parse, run1, run2 } from "./day4.ts";
import { assertEquals } from "./deps.ts";

const sample = [
  "2-4,6-8",
  "2-3,4-5",
  "5-7,7-9",
  "2-8,3-7",
  "6-6,4-6",
  "2-6,4-8",
];

Deno.test("sample parse", () => {
  const expected = [
    [{ start: 2, end: 4 }, { start: 6, end: 8 }],
    [{ start: 2, end: 3 }, { start: 4, end: 5 }],
    [{ start: 5, end: 7 }, { start: 7, end: 9 }],
    [{ start: 2, end: 8 }, { start: 3, end: 7 }],
    [{ start: 6, end: 6 }, { start: 4, end: 6 }],
    [{ start: 2, end: 6 }, { start: 4, end: 8 }],
  ];
  for (let i = 0; i < sample.length && i < expected.length; ++i) {
    assertEquals(parse(sample[i]), expected[i], `${i}`);
  }
});

Deno.test("sample contains", () => {
  const expected = [false, false, false, true, true, false];
  for (let i = 0; i < sample.length && i < expected.length; ++i) {
    assertEquals(contains(parse(sample[i])), expected[i], `${i}`);
  }
});

Deno.test("sample part1", () => {
  const expected = 2;
  assertEquals(run1(sample), expected);
});

Deno.test("sample overlap", () => {
  const expected = [false, false, true, true, true, true];
  for (let i = 0; i < sample.length && i < expected.length; ++i) {
    assertEquals(overlap(parse(sample[i])), expected[i], `${i}`);
  }
});

Deno.test("sample part2", () => {
  const expected = 4;
  assertEquals(run2(sample), expected);
});
