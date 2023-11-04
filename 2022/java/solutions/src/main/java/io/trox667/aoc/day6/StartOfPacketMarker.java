package io.trox667.aoc.day6;

public class StartOfPacketMarker {
    protected char[] marker;

    public StartOfPacketMarker() {
        this.marker = new char[] { 'a', 'a', 'a', 'a' };
    }

    public boolean checkSequence(char[] sequence) {
        for (int i = 0; i < sequence.length; i++) {
            for (int j = i + 1; j < sequence.length; j++) {
                if (sequence[i] == sequence[j]) {
                    return false;
                }
            }
        }
        this.marker = sequence;
        return true;
    }

    public boolean isValid() {
        // all values in marker should be unique
        for (int i = 0; i < marker.length; i++) {
            for (int j = i + 1; j < marker.length; j++) {
                if (marker[i] == marker[j]) {
                    return false;
                }
            }
        }
        return true;
    }

    public char[] getMarker() {
        return marker;
    }
}
