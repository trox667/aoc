package io.trox667

class Day1 : Day {
    fun groupByNewLine(input: String): List<Int> {
        val groups =
            input.split("\n\n").map { it -> it.split("\n").filter { t -> t.isNotEmpty() }.map { v -> v.toInt() }.sum() }
        return groups
    }

    override fun part1(): Int = groupByNewLine(readInput(1)).sortedDescending().first()

    override fun part2(): Int = groupByNewLine(readInput(1)).sortedDescending().take(3).sum()
}