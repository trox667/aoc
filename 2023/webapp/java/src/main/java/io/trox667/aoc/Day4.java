package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Path;
import java.util.*;

public class Day4 extends Day {

    private static class Card {
        private int cardId;
        private List<Integer> winningNumbers;
        private List<Integer> ownNumbers;

        private Card() {
        }

        public int play() {
            var count = 0;
            for (var number : ownNumbers) {
                if (winningNumbers.contains(number)) {
                    count++;
                }
            }

            return (int) Math.pow(2, count - 1);
        }

        public List<Integer> play2() {
            var count = 0;
            for (var number : ownNumbers) {
                if (winningNumbers.contains(number)) {
                    count++;
                }
            }
            var cards = new ArrayList<Integer>();
            for (var i = cardId + 1; i <= cardId + count; i++) {
                cards.add(i);
            }
            return cards;
        }

        public static Card fromString(String input) {
            var game = new Card();
            game.cardId = Integer.parseInt(input.split(":")[0].replaceAll("Card ", "").trim());
            var allNumbers = input.split(":")[1];
            var numbersSplitted = allNumbers.split(" \\| ");
            var winningNumbers = numbersSplitted[0].trim();
            var ownNumbers = numbersSplitted[1].trim();
            game.winningNumbers = Arrays.stream(winningNumbers.split(" ")).filter(s -> !s.isEmpty()).map(Integer::parseInt).toList();
            game.ownNumbers = Arrays.stream(ownNumbers.split(" ")).filter(s -> !s.isEmpty()).map(Integer::parseInt).toList();
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
            for (var card : cards) {
                cardCount.put(card.getCardId(), 1);
            }
            for (var card : cards) {
                var count = cardCount.getOrDefault(card.getCardId(), 0);
                for (var i = 0; i < count; i++) {
                    var newCards = card.play2();
                    for (var newCard : newCards) {
                        cardCount.put(newCard, cardCount.getOrDefault(newCard, 0) + 1);
                    }
                }
            }
            return cardCount.values().stream().reduce(0, Integer::sum);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
