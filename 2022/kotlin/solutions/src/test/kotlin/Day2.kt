import io.trox667.Play
import io.trox667.Reason
import io.trox667.Day2
import io.trox667.pointsRound
import org.junit.jupiter.api.Test
import kotlin.test.assertEquals

class Day2 {

    @Test
    fun `opponent should win`() {
        assertEquals(0, pointsRound(Play.Rock, Reason.Scissors))
        assertEquals(0, pointsRound(Play.Scissors, Reason.Paper))
        assertEquals(0, pointsRound(Play.Paper, Reason.Rock))
    }

    @Test
    fun `player should win`() {
        assertEquals(6, pointsRound(Play.Paper, Reason.Scissors))
        assertEquals(6, pointsRound(Play.Rock, Reason.Paper))
        assertEquals(6, pointsRound(Play.Scissors, Reason.Rock))
    }

    @Test
    fun `result is a draw`() {
        assertEquals(3, pointsRound(Play.Scissors, Reason.Scissors))
        assertEquals(3, pointsRound(Play.Paper, Reason.Paper))
        assertEquals(3, pointsRound(Play.Rock, Reason.Rock))
    }

    @Test
    fun `part 1`() {
        val day2 = Day2()
        assertEquals(12586, day2.part1())
    }

    @Test
    fun `part 2`() {
        val day2 = Day2()
        assertEquals(13193, day2.part2())
    }
}