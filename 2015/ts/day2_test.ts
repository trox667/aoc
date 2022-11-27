import { assertEquals } from "./deps.ts";
import {
  bowRibbon,
  BoxDimension,
  boxSurfaceArea,
  extraPaper,
  parse,
  ribbon,
} from "./day2.ts";

Deno.test("sample parsing", () => {
  const data = ["2x3x4"];
  const expected: BoxDimension[] = [{ length: 2, width: 3, height: 4 }];
  assertEquals(parse(data), expected);
});

Deno.test("sample surface area", () => {
  const data: BoxDimension[] = [
    { length: 2, width: 3, height: 4 },
    { length: 1, width: 1, height: 10 },
  ];
  const expected = [52, 42];
  for (let i = 0; i < data.length && expected.length; ++i) {
    assertEquals(boxSurfaceArea(data[i]), expected[i]);
  }
});

Deno.test("sample extra paper", () => {
  const data: BoxDimension[] = [
    { length: 2, width: 3, height: 4 },
    { length: 1, width: 1, height: 10 },
  ];
  const expected = [6, 1];
  for (let i = 0; i < data.length && expected.length; ++i) {
    assertEquals(extraPaper(data[i]), expected[i]);
  }
});

Deno.test("sample ribbon", () => {
  const data: BoxDimension[] = [
    { length: 2, width: 3, height: 4 },
    { length: 1, width: 1, height: 10 },
  ];
  const expected = [10, 4];
  for (let i = 0; i < data.length && expected.length; ++i) {
    assertEquals(ribbon(data[i]), expected[i]);
  }
});

Deno.test("sample bow ribbon", () => {
  const data: BoxDimension[] = [
    { length: 2, width: 3, height: 4 },
    { length: 1, width: 1, height: 10 },
  ];
  const expected = [24, 10];
  for (let i = 0; i < data.length && expected.length; ++i) {
    assertEquals(bowRibbon(data[i]), expected[i]);
  }
});
