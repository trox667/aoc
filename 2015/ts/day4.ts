import md5 from "npm:md5@2.3.0";

const key = "ckczppom";
const prefix = "00000";
let hash = md5(`${key}${0}`);
let count = 0;

while (!hash.startsWith(prefix)) {
  hash = md5(`${key}${++count}`);
}
console.log(`Part1: ${count}`);

const prefix2 = "000000";
hash = md5(`${key}${0}`);
count = 0;

while (!hash.startsWith(prefix2)) {
  hash = md5(`${key}${++count}`);
}
console.log(`Part2: ${count}`);
