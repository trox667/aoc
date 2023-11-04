package io.trox667.aoc.day7;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import static java.lang.Integer.parseInt;

public class OutputParser {
    private final List<String> lines;
    private int position;
    private final Directory rootDirectory;
    private Directory currentDirectory;
    public OutputParser(List<String> lines) {
        this.lines = lines;
        this.position = 0;
        this.currentDirectory = new Directory(null, "/");
        this.rootDirectory = this.currentDirectory;
    }

    public boolean hasNext() {
        return position < lines.size();
    }

    public void next() {
        if (position >= lines.size()) {
            return;
        }

        var line = lines.get(position);
        if (line.startsWith("$")) {
            line = line.substring(2);
            if (line.startsWith("cd ")) {
                var cdCommand = new CdCommand(line);
                if (cdCommand.getTarget().equals("..")) {
                    this.currentDirectory = this.currentDirectory.getParent();
                    if (this.currentDirectory == null) {
                        this.currentDirectory = this.rootDirectory;
                    }
                } else {
                    var cdDirectory = this.currentDirectory.getDirectory(cdCommand.getTarget());
                    if (cdDirectory != null) {
                        this.currentDirectory = cdDirectory;
                    }
                }
            }
        } else {
            if (!line.isEmpty()) {
                var tokens = line.split(" ");
                if (line.startsWith("dir")) {
                    var name = tokens[1];
                    var directory = new Directory(this.currentDirectory, name);
                    currentDirectory.addFile(directory);
                } else {
                    var size = parseInt(tokens[0]);
                    var name = tokens[1];
                    var file = new File(name, size);
                    currentDirectory.addFile(file);
                }
            }
        }

        position++;
    }

    public Directory getRootDirectory() {
        return this.rootDirectory;
    }
}
