import { char_count, char_position, parse } from "../day02";

test("parse line", () => {
  expect(parse("1-3 a: abcde")).toStrictEqual(["abcde", "a", 1, 3]);
});

test("char_count", () => {
  expect(char_count("abcde", "a")).toBe(1);
});

test("char_position", () => {
  expect(char_position("abcde", "a", 1)).toBeTruthy();
  expect(char_position("cdgef", "b", 1)).toBeFalsy();
  expect(char_position("ccccccccc", "c", 2)).toBeTruthy();
});
