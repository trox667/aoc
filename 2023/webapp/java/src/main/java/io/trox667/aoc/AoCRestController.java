package io.trox667.aoc;

import io.trox667.aoc.persistence.DayItem;
import io.trox667.aoc.persistence.DayRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.ResourceLoader;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Path;
import java.util.List;
import java.util.Optional;
import java.util.stream.StreamSupport;

@RestController
@RequestMapping("aoc")
public class AoCRestController {

    public static record Input(String input, String error) {
    }

    public static record Solution(String part, String error) {
    }

    @Autowired
    ResourceLoader resourceLoader;
    @Autowired
    DayRepository dayRepository;

    @GetMapping("/days")
    public List<DayItem> getDays() {
        return StreamSupport.stream(this.dayRepository.findAll().spliterator(), false).toList();
    }

    private Optional<DayItem> getDay(long day) {
        return this.dayRepository.findById(day);
    }

    @GetMapping(value = {"/solution/{day}", "/solution/{day}/{part}"})
    public Solution solution(@PathVariable("day") int day, @PathVariable("part") Optional<Integer> part) {
        try {
            var inputPath = Path.of(String.format("../../input/sample%02d", day));
            var dayClass = Class.forName("io.trox667.aoc.Day" + day);
            Day dayInstance = (Day) dayClass.getDeclaredConstructor(Path.class).newInstance(inputPath);
            if (part.isPresent() && part.get() == 1) {
                var solution = (String)dayInstance.part1();
                var dayItem = getDay(day);
                System.out.println(dayItem);
                if (dayItem.isPresent()) {
                    dayItem.get().setPart1(solution);
                    this.dayRepository.save(dayItem.get());
                } else {
                    System.out.println("Creating new day item");
                    var newDayItem = new DayItem();
                    newDayItem.setDay(day);
                    newDayItem.setPart1(solution);
                    this.dayRepository.save(newDayItem);
                }
                return new Solution(solution, "");
            } else if (part.isPresent() && part.get() == 2) {
                var solution = (String)dayInstance.part2();
                var dayItem = getDay(day);
                if (dayItem.isPresent()) {
                    dayItem.get().setPart2(solution);
                    this.dayRepository.save(dayItem.get());
                } else {
                    var newDayItem = new DayItem();
                    newDayItem.setDay(day);
                    newDayItem.setPart2(solution);
                    this.dayRepository.save(newDayItem);
                }
                return new Solution(solution, "");
            }
            return new Solution("", "Could not run Day " + day);
        } catch (Exception e) {
            System.err.println("Could not run Day " + day);
            System.err.println(e.getMessage());
            return new Solution("", "Could not run Day " + day);
        }
    }

    private Input getFileForDay(String location, String errorMessage) {
        var resource = resourceLoader.getResource(location);
        try {
            return new Input(resource.getContentAsString(Charset.defaultCharset()), "");
        } catch (IOException e) {
            System.err.println("Could not read input file, " + e.getMessage());
            return new Input("", errorMessage);
        }
    }

    @GetMapping("/sample/{day}")
    public Input sample(@PathVariable("day") int day) {
        var file = String.format("file:../../input/sample%02d", day);
        return getFileForDay(file, "Could not read sample file");
    }

    @GetMapping("/input/{day}")
    public Input input(@PathVariable("day") int day) {
        var file = String.format("file:../../input/input%02d", day);
        return getFileForDay(file, "Could not read input file");
    }
}
