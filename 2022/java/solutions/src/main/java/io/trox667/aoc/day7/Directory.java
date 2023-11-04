package io.trox667.aoc.day7;

import java.util.ArrayList;
import java.util.List;

public class Directory extends File {
    private final List<File> files;
    private final Directory parent;

    public Directory(Directory parent, String name) {
        super(name, 0);
        this.parent = parent;
        files = new ArrayList<>();
    }

    public void addFile(File file) {
        this.files.add(file);
    }

    public int getSize() {
        int size = 0;
        for (File file : files) {
            size += file.getSize();
        }
        return size;
    }

    public Directory getParent() {
        return parent;
    }

    public List<Directory> getDirectories() {
        var directories = new ArrayList<Directory>();
        for (File file : files) {
            if (file instanceof Directory) {
                directories.add((Directory) file);
            }
        }
        return directories;
    }

    public Directory getDirectory(String name) {
        for (File file : files) {
            if (file instanceof Directory && file.getName().equals(name)) {
                return (Directory) file;
            }
        }
        return null;
    }
}
