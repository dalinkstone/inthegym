package main

import (
	"fmt"
)

func validate(first, second string) bool {

	if len(first) != len(second) {
		return false
	}

	count := [26]int{}

	for i := range len(first) {
		count[first[i]-'a']++
		count[second[i]-'a']--
	}

	for _, val := range count {
		if val != 0 {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println("This should return false, testing jar and jam")
	result1 := validate("jar", "jam")
	fmt.Printf("%v/n", result1)

	fmt.Println("This should return true, testing racecar and carrace")
	result2 := validate("racecar", "carrace")
	fmt.Printf("%v\n", result2)
}
