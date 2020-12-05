import * as fs from "fs";

export function read_input() {
  return fs
    .readFileSync("../inputs/input04", "utf8")
    .split("\n\n")
    .map((line) => line.trim())
    .filter((line) => line.length > 0)
    .map((line) => line.replace(/\n/g, " ").split(" "));
}

const keys = new Set(["byr", "eyr", "iyr", "hcl", "ecl", "hgt", "pid"]);

function part1() {
  const input = read_input();
  const valid_passports = input.filter((arr) => {
    let valid = 0;
    for (let item of arr) {
      const kv = item.split(":");
      if (keys.has(kv[0])) valid++;
    }
    return valid >= 7;
  });
  console.log(valid_passports.length);
}

function byr(value) {
  return 1920 <= parseInt(value) && parseInt(value) <= 2002;
}
function iyr(value) {
  return 2010 <= parseInt(value) && parseInt(value) <= 2020;
}
function eyr(value) {
  return 2020 <= parseInt(value) && parseInt(value) <= 2030;
}
function hcl(value) {
  return value.match(/#([0-9]|[a-f]){6}/) != null;
}
function ecl(value) {
  return value.match(/(amb|blu|brn|gry|grn|hzl|oth)/) != null;
}
function pid(value) {
  return value.match(/^[0-9]{9}$/) != null;
}
function hgt(value) {
  const matches = value.match(/(?<height>\d+)(?<unit>in|cm)/);
  if (matches == null) return false;
  const hgt = parseInt(matches.groups["height"]);
  if (matches.groups["unit"] == "in") {
    return 59 <= hgt && hgt <= 76;
  } else {
    return 150 <= hgt && hgt <= 193;
  }
}

function part2() {
  const input = read_input();
  const valid_passports = input.filter((arr) => {
    let valid = 0;
    for (let item of arr) {
      const kv = item.split(":");
      if (kv[0] == "byr" && byr(kv[1])) valid++;
      else if (kv[0] == "iyr" && iyr(kv[1])) valid++;
      else if (kv[0] == "eyr" && eyr(kv[1])) valid++;
      else if (kv[0] == "hcl" && hcl(kv[1])) valid++;
      else if (kv[0] == "ecl" && ecl(kv[1])) valid++;
      else if (kv[0] == "hgt" && hgt(kv[1])) valid++;
      else if (kv[0] == "pid" && pid(kv[1])) valid++;
    }
    return valid >= 7;
  });
  console.log(valid_passports.length);
}

part1();
part2();
