package io.trox667


fun toPlay(token: String): Play = when (token) {
    "A" -> Play.Rock
    "B" -> Play.Paper
    "C" -> Play.Scissors
    else -> {
        throw Error("Invalid Play '${token}'")
    }
}

enum class Play {
    Rock,
    Paper,
    Scissors
}

fun toReason(token: String): Reason = when (token) {
    "X" -> Reason.Rock
    "Y" -> Reason.Paper
    "Z" -> Reason.Scissors
    else -> {
        throw Error("Invalid Reason ${token}")
    }
}

enum class Reason {
    Rock,
    Paper,
    Scissors
}

fun toChoose(token: String, play: Play): Reason = when (token) {
    "X" -> {
        when (play) {
            Play.Rock -> Reason.Scissors
            Play.Scissors -> Reason.Paper
            Play.Paper -> Reason.Rock
        }
    }
    "Y" -> {
        when (play) {
            Play.Rock -> Reason.Rock
            Play.Scissors -> Reason.Scissors
            Play.Paper -> Reason.Paper
        }
    }
    "Z" -> {
        when (play) {
            Play.Rock -> Reason.Paper
            Play.Scissors -> Reason.Rock
            Play.Paper -> Reason.Scissors
        }
    }
    else -> {
        throw Error("Invalid Choose ${token} - ${play}")
    }
}

fun pointsSelection(reason: Reason): Int = when (reason) {
    Reason.Rock -> 1
    Reason.Paper -> 2
    Reason.Scissors -> 3
}

fun pointsRound(play: Play, reason: Reason): Int {
    return when (play) {
        Play.Rock -> {
            when (reason) {
                Reason.Rock -> 3
                Reason.Scissors -> 0
                Reason.Paper -> 6
            }
        }

        Play.Paper -> {
            when (reason) {
                Reason.Rock -> 0
                Reason.Scissors -> 6
                Reason.Paper -> 3
            }
        }

        Play.Scissors -> {
            when (reason) {
                Reason.Rock -> 6
                Reason.Scissors -> 3
                Reason.Paper -> 0
            }
        }
    }
}

class Day2 : Day {
    override fun part1(): Int {
        val input = readInput(2)
        val rounds = input.split("\n").filter { t -> t.isNotEmpty() }.map { it -> it.split(" ") }
        var sum = 0
        for (round in rounds) {
            sum += pointsRound(toPlay(round.first()), toReason(round.last())) + pointsSelection(toReason(round.last()))
        }
        return sum
    }

    override fun part2(): Int {
        val input = readInput(2)
        val rounds = input.split("\n").filter { t -> t.isNotEmpty() }.map { it -> it.split(" ") }
        var sum = 0
        for (round in rounds) {
            sum += pointsRound(toPlay(round.first()), toChoose(round.last(), toPlay(round.first()))) + pointsSelection(toChoose(round.last(), toPlay(round.first())))
        }
        return sum
    }
}