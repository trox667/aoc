package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;

public class Day15 extends Day {
    private static class HASHAlgorithm {

        public static long getHash(String input) {
            var hash = 0L;
            for (var c : input.toCharArray()) {
                var code = (int) c;
                hash += code;
                hash *= 17;
                hash %= 256;
            }
            return hash;
        }
    }

    private static class InitializationSequence {
        public static long fromStrings(List<String> lines) {
            var result = 0L;
            for (var line : lines) {
                result += Arrays.stream(line.split(",")).map(HASHAlgorithm::getHash).reduce(0L, Long::sum);
            }
            return result;
        }
    }

    private record Step(String label, String operation, int focalLength) {
        public long getHash() {
            return HASHAlgorithm.getHash(this.label);
        }
    }

    private record Lens(String label, int focalLength) {};

    private static class Box {
        private HashMap<String, Integer> labelsToLenses;
        private List<Lens> lenses;

        public Box() {
            this.labelsToLenses = new HashMap<>();
            this.lenses = new ArrayList<Lens>();
        }

        public Lens remove(String label) {
            if (labelsToLenses.containsKey(label)) {
                int index = labelsToLenses.get(label);
                labelsToLenses.remove(label);
                var oldLense = lenses.remove(index);
                for (var i = index; i < lenses.size(); i++) {
                    labelsToLenses.put(lenses.get(i).label(), i);
                }
            }
            return null;
        }

        public void add(Lens lens) {
            if (labelsToLenses.containsKey(lens.label())) {
                int index = labelsToLenses.get(lens.label());
                var oldLens = lenses.set(index, lens);
            } else {
                labelsToLenses.put(lens.label(), lenses.size());
                lenses.add(lens);
            }
        }
    }

    private static class Facility {
        private HashMap<Long, Box> boxes;

        public Facility() {
            this.boxes = new HashMap<>();
        }

        public static Facility fromStrings(List<String> lines) {
            var facility = new Facility();
            for (var line : lines) {
                var steps = line.split(",");
                for (var step : steps) {
                    var tokens = step.split("=|-");
                    var label = tokens[0];
                    var focalLength = tokens.length > 1 ? Integer.parseInt(tokens[1]) : 0;
                    var operation = step.contains("=") ? "=" : "-";
                    var hash = HASHAlgorithm.getHash(label);
                    if (!facility.boxes.containsKey(hash)) {
                        facility.boxes.put(hash, new Box());
                    }
                    if (operation == "=") {
                        facility.boxes.get(hash).add(new Lens(label, focalLength));
                    } else {
                        facility.boxes.get(hash).remove(label);
                    }
                }
            }
            return facility;
        }

        public long getFocusingPower() {
            var overallPower = 0L;
            for (var i = 0L; i < 256L; i++) {
                if (this.boxes.containsKey(i)) {
                    var box = this.boxes.get(i);
                    if (box.lenses.size() == 0) {
                        continue;
                    }
                    var boxIndex = i + 1L;
                    for (var j = 0; j < box.lenses.size(); j++) {
                        overallPower += boxIndex * (j + 1) * box.lenses.get(j).focalLength;
                    }
                }
            }
            return overallPower;
        }
    }

    public Day15(Path path) {
        super(path);
    }

    @Override
    public Object part1() {
        try {
            return InitializationSequence.fromStrings(this.readInput());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Object part2() {
        try {
            var facility = Facility.fromStrings(this.readInput());
            return facility.getFocusingPower();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
