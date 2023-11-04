package io.trox667.aoc.day7;

import java.util.ArrayList;

public class FileSystem {
    private final Directory rootDirectory;
    private final static int MAX_SIZE = 70_000_000;

    public FileSystem(Directory rootDirectory) {
        this.rootDirectory = rootDirectory;
    }

    public int getDirectoriesSize() {
        var sizes = new ArrayList<Integer>();
        walkDirectoriesWithLimit(rootDirectory, sizes);
        if (rootDirectory.getSize() <= 100_000) {
            sizes.add(rootDirectory.getSize());
        }
        return sizes.stream().reduce(0, Integer::sum);
    }

    public int getDirectoryToDelete(int requiredSpace) {
        var sizes = new ArrayList<Integer>();
        var minDirSize = Integer.MAX_VALUE;
        var rootSize = rootDirectory.getSize();
        var freeSpace = MAX_SIZE - rootSize;
        walkDirectories(rootDirectory, sizes);
        for (var size : sizes) {
            var currFreeSpace = freeSpace + size;
            if (currFreeSpace >= requiredSpace) {
                minDirSize = Math.min(minDirSize, size);
            }
        }
        return minDirSize;
    }

    private void walkDirectories(Directory current, ArrayList<Integer> sizes) {
        for (var directory : current.getDirectories()) {
            var size = directory.getSize();
            sizes.add(size);
            walkDirectories(directory, sizes);
        }
    }

    private void walkDirectoriesWithLimit(Directory current, ArrayList<Integer> sizes) {
        for (var directory : current.getDirectories()) {
            var size = directory.getSize();
            if (size <= 100_000) {
                sizes.add(size);
            }
            walkDirectoriesWithLimit(directory, sizes);
        }
    }
}
