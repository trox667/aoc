import { readLines } from "./utils.ts";

// min 3 vowels [aeiou]
// min one letter as pair (aa or aabb or dccd)
// not contain [ab] or [cd] or [pq] or [xy]
const vowels = "aeiou".split("");
const ignoreList = ["ab", "cd", "pq", "xy"];

function hasVowels(testString: string): boolean {
  return testString.split("").reduce((acc, token) => {
    if (vowels.findIndex((vowel) => vowel === token) >= 0) {
      return acc + 1;
    }
    return acc;
  }, 0) >= 3;
}

function hasPair(testString: string): boolean {
  const tokens = testString.split("");
  for (const token of tokens) {
    if (testString.includes(`${token}${token}`)) {
      return true;
    }
  }
  return false;
}

function hasNot(testString: string): boolean {
  for (const ignoreItem of ignoreList) {
    if (testString.includes(ignoreItem)) {
      return false;
    }
  }
  return true;
}

export function isNice(testString: string): boolean {
  return hasVowels(testString) && hasPair(testString) && hasNot(testString);
}

function part1() {
  const part1 = readLines("../inputs/input05").reduce((acc, line) => {
    if (isNice(line)) {
      return acc + 1;
    }
    return acc;
  }, 0);
  console.log(`Part1: ${part1}`);
}

part1();

// min two pair of letters without overlapping (xyxy, aabcdaa) not (aaa)
// repeated letter with offset 1 (aba, aaa, dcd)

function hasTwoPairs(testString: string): boolean {
  const tokens = testString.split("");
  for (let i = 0; i < tokens.length - 1; ++i) {
    const search = tokens[i] + tokens[i + 1];
    if (testString.substring(i + 2).includes(search)) {
      return true;
    }
  }

  return false;
}

function repeatingLetter(testString: string): boolean {
  const tokens = testString.split("");
  for (let i = 0; i < tokens.length - 2; ++i) {
    const search = tokens[i];
    if (tokens[i + 2] === search) {
      return true;
    }
  }

  return false;
}

export function isNice2(testString: string): boolean {
  return hasTwoPairs(testString) && repeatingLetter(testString);
}

function part2() {
  const part2 = readLines("../inputs/input05").reduce((acc, line) => {
    if (isNice2(line)) {
      return acc + 1;
    }
    return acc;
  }, 0);
  console.log(`Part2: ${part2}`);
}

part2();
