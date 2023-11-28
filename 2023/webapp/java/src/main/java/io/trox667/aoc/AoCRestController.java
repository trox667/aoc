package io.trox667.aoc;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AoCRestController {
    @GetMapping("/aoc/")
    public String index() {
        return "Hello World!";
    }
}
