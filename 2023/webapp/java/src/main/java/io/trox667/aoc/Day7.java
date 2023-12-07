package io.trox667.aoc;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.atomic.AtomicBoolean;

public class Day7 extends Day {

    private enum Card {
        ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JOKER, QUEEN, KING, ACE
    }

    private static Card cardFromChar(Character chr) {
        switch (chr) {
            case '1':
                return Card.ONE;
            case '2':
                return Card.TWO;
            case '3':
                return Card.THREE;
            case '4':
                return Card.FOUR;
            case '5':
                return Card.FIVE;
            case '6':
                return Card.SIX;
            case '7':
                return Card.SEVEN;
            case '8':
                return Card.EIGHT;
            case '9':
                return Card.NINE;
            case 'T':
                return Card.TEN;
            case 'J':
                return Card.JOKER;
            case 'Q':
                return Card.QUEEN;
            case 'K':
                return Card.KING;
            case 'A':
                return Card.ACE;
            default:
                throw new IllegalArgumentException("Invalid card: " + chr);
        }
    }

    private static class Hand {
        private final List<Card> cards;

        private Hand() {
            this.cards = new ArrayList<>();
        }

        public long getMaxStrength(boolean joker) {
            long maxStrength = 0;
            Card foundCard = null;
            AtomicBoolean usedJoker = new AtomicBoolean(false);
            for (var card : Card.values()) {
                var current = cards.stream().filter(c -> {
                    if (joker) {
                        if (c == Card.JOKER) usedJoker.set(true);
                        return c == card || c == Card.JOKER;
                    } else {
                        return c == card;
                    }
                }).count();
                if (current > maxStrength) {
                    foundCard = card;
                    maxStrength = current;
                }
            }
            if (maxStrength == 2) {
                // two pair > one pair
                for (var card : Card.values()) {
                    if (card != foundCard) {
                        if (usedJoker.get() && card == Card.JOKER) {
                            continue;
                        }
                        var current = cards.stream().filter(c -> c == card).count();
                        if (current == 2) {
                            maxStrength = 3;
                            break;
                        }
                    }
                }
            } else if (maxStrength == 4) {
                // four of a kind > full house
                maxStrength = 6;
            } else if (maxStrength == 5) {
                // five of a kind > four of a kind
                maxStrength = 7;
            } else if (maxStrength == 3) {
                // full house three of a kind + two of another kind
                maxStrength = 4;
                for (var card : Card.values()) {
                    if (card != foundCard) {
                        if (usedJoker.get() && card == Card.JOKER) {
                            continue;
                        }
                        var current = cards.stream().filter(c -> c == card).count();
                        if (current == 2) {
                            maxStrength = 5;
                            break;
                        }
                    }
                }
            }
            return maxStrength;
        }

        public static Hand fromString(String handStr) {
            var hand = new Hand();
            for (var cardStr : handStr.toCharArray()) {
                hand.cards.add(cardFromChar(cardStr));
            }
            return hand;
        }

        @Override
        public String toString() {
            return "Hand{" +
                    "cards=" + cards +
                    '}';
        }
    }

    private record HandBid(Hand hand, long bid) {
    }

    private static class Game {
        private List<HandBid> handsWithBids;

        private Game() {
            this.handsWithBids = new ArrayList<>();
        }

        private void sort(boolean joker) {
            Collections.sort(this.handsWithBids, (a, b) -> {
                if (a.hand.getMaxStrength(joker) == b.hand.getMaxStrength(joker)) {
                    for (var i = 0; i < 5; i++) {
                        var ac = a.hand.cards.get(i);
                        var bc = b.hand.cards.get(i);
                        if (joker) {
                            var av = ac == Card.JOKER ? -1 : ac.ordinal();
                            var bv = bc == Card.JOKER ? -1 : bc.ordinal();
                            if (av > bv) {
                                return 1;
                            } else if (av < bv) {
                                return -1;
                            } else {
                                continue;
                            }
                        } else {
                            if (ac.ordinal() > bc.ordinal()) {
                                return 1;
                            } else if (ac.ordinal() < bc.ordinal()) {
                                return -1;
                            } else {
                                continue;
                            }
                        }
                    }
                    return 0;
                }
                return (int) (a.hand.getMaxStrength(joker) - b.hand.getMaxStrength(joker));
            });
        }

        public long getTotalWinnings(boolean joker) {
            this.sort(joker);
            var totalWinnings = 0L;
            for (var i = 0; i < this.handsWithBids.size(); i++) {
                var handBid = this.handsWithBids.get(i);
                totalWinnings += handBid.bid * (i + 1);
            }
            return totalWinnings;
        }

        public static Game fromStrings(List<String> lines) {
            var game = new Game();
            for (var line : lines.stream().filter(l -> !l.isEmpty()).toList()) {
                var tokens = line.split(" ");
                var hand = Hand.fromString(tokens[0].trim());
                var bid = Long.parseLong(tokens[1].trim());
                game.handsWithBids.add(new HandBid(hand, bid));
            }
            return game;
        }

        @Override
        public String toString() {
            return "Game{" +
                    "handsWithBids=" + handsWithBids +
                    '}';
        }
    }

    public Day7(Path path) {
        super(path);
    }

    @Override
    public Object part1() {
        try {
            var game = Game.fromStrings(this.readInput());
            return game.getTotalWinnings(false);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Object part2() {
        try {
            var game = Game.fromStrings(this.readInput());
            return game.getTotalWinnings(true);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
