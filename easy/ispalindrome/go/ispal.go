package main

import (
	"fmt"
)

func palin(word string) bool {

	for i := range word {
		if word[i] != word[len(word)-1-i] {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println("This should return false because we are testing if the word monkey is a palindrome")
	result := palin("monkey")
	fmt.Printf("%v\n", result)

	fmt.Println("This should return true because we are testing if the word racecar is a palindrome")
	result2 := palin("racecar")
	fmt.Printf("%v\n", result2)
}
