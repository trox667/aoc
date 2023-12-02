package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;

public class Day2 extends Day {

    private final static record Game(int id, List<GameSet> sets) {
    }

    private final static record GameSet(int red, int green, int blue) {
    }

    public Day2(Path path) {
        super(path);
    }


    private GameSet parseGameSet(String set) {
        var cubes = set.split(", ");
        var red = 0;
        var green = 0;
        var blue = 0;
        for (var cube : cubes) {
            var tokens = cube.split(" ");
            assert tokens.length >= 2;
            var color = tokens[1];
            switch (color) {
                case "red" -> red = Integer.parseInt(tokens[0]);
                case "green" -> green = Integer.parseInt(tokens[0]);
                case "blue" -> blue = Integer.parseInt(tokens[0]);
            }
        }
        return new GameSet(red, green, blue);
    }

    private Game parseGame(String line) {
        var gameAndTail = line.split(": ");
        assert gameAndTail.length >= 2;
        var gameId = gameAndTail[0].replaceAll("Game ", "");
        var gameSets = Arrays.stream(gameAndTail[1].split("; ")).map(this::parseGameSet).toList();
        var game = new Game(Integer.parseInt(gameId), gameSets);
        return game;
    }

    private boolean isGamePossible(int maxRed, int maxGreen, int maxBlue, Game game) {
        return !game.sets.stream().anyMatch(set -> set.red() > maxRed || set.green() > maxGreen || set.blue() > maxBlue);
    }

    private int gamePower(Game game) {
        var red = 0;
        var green = 0;
        var blue = 0;
        for (var set : game.sets()) {
            red = Math.max(red, set.red());
            green = Math.max(green, set.green());
            blue = Math.max(blue, set.blue());
        }
        return red * green * blue;
    }

    @Override
    public Object part1() {
        try {
            var games = this.readInput().stream().map(this::parseGame).toList();
            return games.stream().filter(game -> isGamePossible(12, 13, 14, game)).map(game -> game.id()).reduce(0, Integer::sum);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Object part2() {
        try {
            var games = this.readInput().stream().map(this::parseGame).toList();
            return games.stream().map(this::gamePower).reduce(0, Integer::sum);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
