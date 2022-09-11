import { assertEquals } from "https://deno.land/std@0.154.0/testing/asserts.ts";

const parseSideLengths = (input: string) => {
  return input.split("\n").filter((line) => line.length > 0).map((line) =>
    line.trim().split("  ").filter((token) => token.length > 0).map((token) =>
      parseInt(token)
    )
  );
};

const parseSideLengths2 = (input: string) => {
  const result = [];
  const tokens = parseSideLengths(input);
  for (let i = 0; i < tokens[0].length; ++i) {
    for (let j = 0; j < tokens.length; j += 3) {
      result.push([tokens[j][i], tokens[j + 1][i], tokens[j + 2][i]]);
    }
  }
  return result;
};

const triangle = (a: number, b: number, c: number): boolean =>
  a + b > c && b + c > a && a + c > b;

const TEST = false;

if (TEST) {
  Deno.test("part1", () => {
    assertEquals(triangle(5, 10, 25), false);
  });
} else {
  const run = (input: string): number => {
    const result = parseSideLengths(input).filter((tokens) =>
      triangle(tokens[0], tokens[1], tokens[2])
    );
    return result.length;
  };
  const run2 = (input: string): number => {
    const result = parseSideLengths2(input).filter((tokens) =>
      triangle(tokens[0], tokens[1], tokens[2])
    );
    return result.length;
  };

  const input = await Deno.readTextFile("../inputs/input03");
  console.log(`Part 1: ${run(input)}`);
  console.log(`Part 2: ${run2(input)}`);
}
