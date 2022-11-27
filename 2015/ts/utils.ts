export function readLines(file: string): string[] {
  const content = Deno.readTextFileSync(file);
  return content.split("\n");
}
