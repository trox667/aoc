import { run, run2 } from "./day8.ts";
import { assertEquals } from "./deps.ts";

const sample = `30373
25512
65332
33549
35390`.split("\n");

Deno.test("run sample", () => {
  const expected = 21;
  assertEquals(run(sample), expected);
});

Deno.test("run2 sample", () => {
  const expected = 8;
  assertEquals(run2(sample), expected);
});
