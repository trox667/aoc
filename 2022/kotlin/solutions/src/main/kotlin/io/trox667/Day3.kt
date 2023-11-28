package io.trox667

import java.lang.IllegalArgumentException

typealias Rucksack = String
typealias Compartment = String
typealias Compartments = Pair<Compartment, Compartment>
typealias GroupRucksacks = Triple<Rucksack, Rucksack, Rucksack>

fun GroupRucksacks.commonBadge(): Char {
    val result = first.toSet().intersect(second.toSet().intersect(third.toSet()))
    return result.first()
}

fun getPriority(char: Char) = if (char.isUpperCase()) char.code - 38 else char.code - 96
fun getRucksacks(input: String): List<Rucksack> = input.lines()
fun getCompartments(rucksack: Rucksack): Compartments = Pair(rucksack.substring(0, rucksack.length/2), rucksack.substring(rucksack.length/2))
fun getDuplicate(compartments: Compartments): Char {
    val intersection = compartments.first.toSet().intersect(compartments.second.toSet()).toList()
    if (intersection.size != 1) throw IllegalArgumentException()
    return intersection[0]
}

fun getGroups(rucksacks: List<Rucksack>): List<GroupRucksacks> {
    var groups = mutableListOf<GroupRucksacks>()
    for (i in rucksacks.indices step 3) {
        groups.add(Triple(rucksacks[i], rucksacks[i+1], rucksacks[i+2]))
    }
    return groups
}



class Day3 : Day {
    override fun part1(): Int {
        val input = readInput(3).trim()
        val rucksacks = getRucksacks(input)
        return rucksacks.sumOf { getPriority(getDuplicate(getCompartments(it))) }
    }

    override fun part2(): Int {
        val input = readInput(3).trim()
        val rucksacks = getRucksacks(input)
        val groups = getGroups(rucksacks)
        return groups.sumOf { getPriority(it.commonBadge()) }
    }
}