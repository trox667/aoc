import { parse, play, play2, playRounds } from "./day2.ts";
import { assertEquals } from "./deps.ts";

const sample = ["A Y", "B X", "C Z", "C A"];

Deno.test("sample parse", () => {
  const expected = [[1, 2], [2, 1], [3, 3], [3, 1]];
  for (let i = 0; i < sample.length && expected.length; ++i) {
    assertEquals(parse(sample[i]), expected[i]);
  }
});

Deno.test("sample play part 1", () => {
  const expected = [8, 1, 6, 7];
  for (let i = 0; i < sample.length && expected.length; ++i) {
    assertEquals(play(parse(sample[i])), expected[i]);
  }
});

Deno.test("sample part1", () => {
  assertEquals(playRounds(sample), 22);
});

Deno.test("sample part2", () => {
  assertEquals(playRounds(sample, play2), 14);
});
