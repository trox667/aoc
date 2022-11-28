export function readLines(file: string): string[] {
  return Deno.readTextFileSync(file).split("\n").filter((line) =>
    line.length > 0
  );
}
