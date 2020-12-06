import * as fs from "fs";

export function read_input() {
  return fs
    .readFileSync("../inputs/input05", "utf8")
    .split("\n")
    .filter((line) => line.trim().length > 0)
    .map((line) => [line.substring(0, 7), line.substring(7, 10)]);
}

function seats(input) {
  const results = [];
  for (const line of input) {
    let [row, column] = line;
    row = row.replace(/F/g, "0");
    row = row.replace(/B/g, "1");
    column = column.replace(/L/g, "0");
    column = column.replace(/R/g, "1");
    results.push(parseInt(row, 2) * 8 + parseInt(column, 2));
  }
  return results;
}

function part1() {
  const results = seats(read_input());
  console.log(results.reduce((acc, v) => (acc > v ? acc : v)));
}

function part2() {
  const seatIds = seats(read_input());
  seatIds.sort((a, b) => a - b);
  const cmpSeatIds = new Set(seatIds);
  for (const seatId of seatIds) {
    if (!cmpSeatIds.has(seatId + 1) && cmpSeatIds.has(seatId + 2)) {
      console.log(seatId + 1);
      return;
    }
  }
}

part1();
part2();
