package main

import (
	"fmt"
)

func validate(first, second string) bool {

	if len(first) != len(second) {
		return false
	}

	countFirst := make(map[string]int)
	countSecond := make(map[string]int)

	return false
}

func main() {
	fmt.Println("This should return false, testing jar and jam")
	result1 := validate("jar", "jam")
}
