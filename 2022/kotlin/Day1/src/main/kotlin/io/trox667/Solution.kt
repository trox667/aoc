package io.trox667

import java.io.File

class Calories(private val values: ArrayList<Int> = ArrayList<Int>()) {

    fun addCalorie(calorie: Int) {
        this.values.add(calorie)
    }

    fun sum(): Int {
        return this.values.sum()
    }
}

fun main() {
    val input = File("input1").readLines()
    val allCalories = ArrayList<Calories>()
    var calories = Calories()
    for (i in input) {
        if (i.isNotEmpty()) {
            calories.addCalorie(i.toInt())
        } else {
            allCalories.add(calories)
            calories = Calories()
        }
    }

    val maxCalories = allCalories.maxOfOrNull { it.sum() }
    println("Part 1: $maxCalories")

    val sortedCalories = allCalories.map { it.sum() }.sortedDescending()
    val topThreeCalories = sortedCalories.take(3).sum()
    println("Part 2: $topThreeCalories")
}