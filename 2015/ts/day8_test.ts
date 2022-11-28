import { assertEquals } from "./deps.ts";
import { encode, memoryNumber, representation, totalNumber } from "./day8.ts";

Deno.test("part1 totalNumber sample", () => {
  const data = [`""`, `"abc"`, `"aaa\\"aaa"`, `"\\x27"`];
  const expected = [2, 5, 10, 6];
  for (let i = 0; i < data.length && i < expected.length; ++i) {
    assertEquals(totalNumber(data[i]), expected[i]);
  }
});

Deno.test("part1 memoryNumber sample", () => {
  const data = [`""`, `"abc"`, `"aaa\\"aaa"`, `"\\x27"`];
  const expected = [0, 3, 7, 1];
  for (let i = 0; i < data.length && i < expected.length; ++i) {
    assertEquals(memoryNumber(data[i]), expected[i]);
  }
});

Deno.test("part1 representation sample", () => {
  const data = [`""`, `"abc"`, `"aaa\\"aaa"`, `"\\x27"`];
  const expected = 12;
  for (let i = 0; i < data.length; ++i) {
    assertEquals(representation(data), expected);
  }
});

Deno.test("part2 encode sample", () => {
  const data = [`""`, `"abc"`, `"aaa\\"aaa"`, `"\\x27"`];
  const expected = [6, 9, 16, 11];
  for (let i = 0; i < data.length && i < expected.length; ++i) {
    assertEquals(encode(data[i]), expected[i]);
  }
});
