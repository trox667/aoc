import { assertEquals } from "./deps.ts";
import { parse, walk } from "./day3.ts";

Deno.test("sample parsing", () => {
  const data = [[">"], ["^>v<"]];
  const expected = [
    [[{ x: 1, y: 0 }]],
    [[{ x: 0, y: 1 }, { x: 1, y: 0 }, { x: 0, y: -1 }, { x: -1, y: 0 }]],
  ];
  for (let i = 0; i < data.length && expected.length; ++i) {
    assertEquals(parse(data[i]), expected[i]);
  }
});

Deno.test("sample values", () => {
  const data = parse([">", "^>v<"]);
  const expected = [2, 4];
  for (let i = 0; i < data.length && expected.length; ++i) {
    assertEquals(walk(data[i]), expected[i]);
  }
});
