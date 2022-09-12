import { createHash } from "https://deno.land/std@0.155.0/hash/mod.ts";

// const input = "abbhdwsy";
const input = "abc";

let loop = true;
let index = 0;
let hits = 0;

while (loop) {
  const hasher = createHash("md5");
  hasher.update(`${input}${index}`);
  const hash = hasher.toString();
  if (index > 3_000_000) {
    console.log(hash);
  }
  if (hash.startsWith("00000")) {
    console.log(hash);
    hits += 1;
    if (hits >= 8) {
      loop = false;
    }
  }
  console.log(index);
  index++;
}
