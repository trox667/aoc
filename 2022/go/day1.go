package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	content, err := os.ReadFile("../inputs/input1")
	if err != nil {
		fmt.Println("Could not open input")
	}

	var sums []int
	groups := strings.Split(string(content), "\n\n")
	for i := 0; i < len(groups); i++ {
		lines := strings.Split(groups[i], "\n")
		var sum int = 0
		for j := 0; j < len(lines); j++ {
			line := lines[j]
			if len(line) > 0 {
				val, err := strconv.Atoi(line)
				if err == nil {
					sum += val
				}
			}
		}
		sums = append(sums, sum)
	}

	sort.Slice(sums, func(i, j int) bool {
		return sums[i] > sums[j]
	})

	if len(sums) >= 3 {

		fmt.Println("Part 1:", sums[0])
		fmt.Println("Part 2:", sums[2]+sums[1]+sums[0])
	}
}
