import java.io.File

fun readInput(): List<Int> {
    return File("../inputs/input06").readLines()[0].split(',').map { it.toInt() }
}

fun run(state: List<Int>, days: Int = 80): Long {
    val numbers = LongArray(9)
    for (s in state) {
        numbers[s] += 1L
    }

    for (day in 0..days-1) {
        val countNew = numbers[0]
        numbers[0] = 0
        for (i in 1..8) {
            if (numbers[i] > 0) {
                numbers[i - 1] = numbers[i]
                numbers[i] = 0
            }
        }
        numbers[6] += countNew
        numbers[8] += countNew
    }

    return numbers.sum()
}

fun part1(): Long {
    return run(readInput())
}

fun part2(): Long {
    return run(readInput(), 256)
}