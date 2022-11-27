import { assertEquals } from "./deps.ts";
import { isNice, isNice2 } from "./day5.ts";

Deno.test("sample part 1", () => {
  const data = [
    "ugknbfddgicrmopn",
    "aaa",
    "jchzalrnumimnmhp",
    "haegwjzuvuyypxyu",
    "dvszwmarrgswjxmb",
  ];
  const expected = [true, true, false, false, false];
  for (let i = 0; i < data.length && i < expected.length; ++i) {
    assertEquals(isNice(data[i]), expected[i]);
  }
});
Deno.test("sample part 2", () => {
  const data = [
    "qjhvhtzxzqqjkmpb",
    "aaa",
    "xxyxx",
    "uurcxstgmygtbstg",
    "ieodomkazucvgmuy",
  ];
  const expected = [true, false, true, false, false];
  for (let i = 0; i < data.length && i < expected.length; ++i) {
    assertEquals(isNice2(data[i]), expected[i]);
  }
});
