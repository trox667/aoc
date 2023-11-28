import io.trox667.*
import io.trox667.Day3
import org.junit.jupiter.api.Test
import kotlin.test.assertEquals

class Day3 {
    val sample = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

    @Test
    fun `sample contains six rucksacks`() {
        assertEquals(getRucksacks(sample).size, 6)
    }

    @Test
    fun `first rucksack compartmens`() {
        val pair = Pair("vJrwpWtwJgWr", "hcsFMMfFFhFp")
        assertEquals(getCompartments(getRucksacks(sample)[0]), pair)
    }

    @Test
    fun `check priorities`() {
        assertEquals(getPriority('a'), 1)
        assertEquals(getPriority('z'), 26)
        assertEquals(getPriority('A'), 27)
        assertEquals(getPriority('Z'), 52)
    }

    @Test
    fun `get duplicate of first rucksack`() {
        assertEquals(getDuplicate(getCompartments(getRucksacks(sample)[0])), 'p')
        assertEquals(getDuplicate(getCompartments(getRucksacks(sample)[1])), 'L')
        assertEquals(getDuplicate(getCompartments(getRucksacks(sample)[2])), 'P')
        assertEquals(getDuplicate(getCompartments(getRucksacks(sample)[3])), 'v')
        assertEquals(getDuplicate(getCompartments(getRucksacks(sample)[4])), 't')
        assertEquals(getDuplicate(getCompartments(getRucksacks(sample)[5])), 's')
    }

    @Test
    fun `part 1`() {
        val day3 = Day3()
        assertEquals(day3.part1(), 7997)
    }

    @Test
    fun `create the first group`() {
        val group = Triple(
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg"
        )
        assertEquals(getGroups( getRucksacks(sample))[0], group)
    }

    @Test
    fun `common badge of the first group`() {
        assertEquals(getGroups( getRucksacks(sample))[0].commonBadge(),'r')
    }

    @Test
    fun `part 2`() {
        val day3 = Day3()
        assertEquals(day3.part2(), 2545)
    }
}