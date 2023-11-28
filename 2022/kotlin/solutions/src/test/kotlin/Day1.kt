import io.trox667.Day1
import org.junit.jupiter.api.Test
import kotlin.test.assertEquals

class Day1 {
    @Test
    fun `read input1`() {
        val day1 = Day1()
        assert(day1.readInput(1).isNotEmpty())
    }

    @Test
    fun `part 1`() {
        val day1 = Day1()
        assertEquals(66616, day1.part1())
    }

    @Test
    fun `part 2`() {
        val day1 = Day1()
        assertEquals(199172, day1.part2())
    }
}