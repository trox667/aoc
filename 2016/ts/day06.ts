import { assertEquals } from "https://deno.land/std@0.154.0/testing/asserts.ts";

const run = (input: string, desc = true): string => {
  const codes = input.split("\n").filter((line) => line.length > 0).map((
    line,
  ) => line.split(""));
  const result = [];
  for (let col = 0; col < codes[0].length; ++col) {
    const chars: Map<string, number> = new Map();
    for (let row = 0; row < codes.length; ++row) {
      const c = codes[row][col];
      const count = chars.get(c) ?? 0;
      chars.set(c, count + 1);
    }
    const countData = [...chars.entries()];
    countData.sort(([ak, ac], [bk, bc]) => {
      return desc ? bc - ac : ac - bc;
    });
    result.push(countData[0][0]);
  }
  return result.join("");
};

const TEST = false;

if (TEST) {
  const input = `eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar`;

  Deno.test("part1", () => {
    assertEquals(run(input), "easter");
  });
  Deno.test("part2", () => {
    assertEquals(run(input, false), "advent");
  });
} else {
  const input = await Deno.readTextFile("../inputs/input06");
  console.log(`Part 1: ${run(input)}`);
  console.log(`Part 2: ${run(input, false)}`);
}
