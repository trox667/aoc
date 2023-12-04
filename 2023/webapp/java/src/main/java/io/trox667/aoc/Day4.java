package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Path;
import java.util.*;
import java.util.stream.IntStream;

public class Day4 extends Day {

    private static class Card {
        private int cardId;
        private HashSet<Integer> matches;

        private Card() {
            this.matches = new HashSet<>();
        }

        public int play() {
            return (int) Math.pow(2, matches.size() - 1);
        }

        public IntStream play2() {
            return IntStream.range(cardId+1, cardId+matches.size()+1);
        }

        public static Card fromString(String input) {
            var game = new Card();
            game.cardId = Integer.parseInt(input.split(":")[0].replaceAll("Card ", "").trim());
            var allNumbers = input.split(":")[1];
            var numbersSplitted = allNumbers.split(" \\| ");
            var winningNumbersText = numbersSplitted[0].trim();
            var ownNumbersText = numbersSplitted[1].trim();
            game.matches = new HashSet<>(Arrays.stream(ownNumbersText.split(" ")).filter(s -> !s.isEmpty()).map(Integer::parseInt).toList());
            game.matches.retainAll(Arrays.stream(winningNumbersText.split(" ")).filter(s -> !s.isEmpty()).map(Integer::parseInt).toList());
            return game;
        }

        public int getCardId() {
            return cardId;
        }
    }

    public Day4(Path path) {
        super(path);
    }

    @Override
    public Object part1() {
        try {
            return this.readInput().stream().map(Card::fromString).map(Card::play).reduce(0, Integer::sum);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Object part2() {
        try {
            var cardCount = new HashMap<Integer, Integer>();
            var cards = this.readInput().stream().map(Card::fromString).toList();
            cards.stream().forEach(card -> cardCount.put(card.getCardId(), 1));
            cards.stream().forEach(card -> {
                IntStream.range(0, cardCount.getOrDefault(card.getCardId(), 0)).forEach(_i -> {
                    card.play2().forEach(newCard -> cardCount.put(newCard, cardCount.getOrDefault(newCard, 0) + 1));
                });
            });
            return cardCount.values().stream().reduce(0, Integer::sum);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
