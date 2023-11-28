package io.trox667

interface Day {
    fun readInput(day: Int): String {
        val file = Day::class.java.getResource("/input${day}")
        return file?.readText() ?: ""
    }

    fun part1(): Int
    fun part2(): Int
}