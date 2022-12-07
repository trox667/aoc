import { Directory, File, parse, run, run2, Tree } from "./day7.ts";
import { assertEquals } from "./deps.ts";

const sample = `$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k`.split("\n");

Deno.test("sample parse", () => {
  const expected = new Tree(
    new Directory(
      "/",
      [
        new Directory("a", [
          new Directory("e", [
            new File("i", 584),
          ]),
          new File("f", 29116),
          new File("g", 2557),
          new File("h.lst", 62596),
        ]),
        new File("b.txt", 14848514),
        new File("c.dat", 8504156),
        new Directory("d", [
          new File("j", 4060174),
          new File("d.log", 8033020),
          new File("d.ext", 5626152),
          new File("k", 7214296),
        ]),
      ],
    ),
  );
  assertEquals(parse(sample), expected);
  assertEquals(expected.directories().length, 4);
});

Deno.test("sample part1", () => {
  const expected = 95437;
  assertEquals(run(sample), expected);
});

Deno.test("sample part2", () => {
  const expected = 24933642;
  assertEquals(run2(sample), expected);
});
