package main

import (
	"fmt"
)

func twosum(nums []int, target int) []int {
	result := make(map[int]int)

	for i, num := range nums {
		diff := target - num

		if j, found := result[diff]; found {
			return []int{j, i}
		}

		result[num] = i
	}
	return []int{}

}

func main() {

	fmt.Println("This first test is passing an array of [3, 5, 4, 6] with a target of 7")

	arr_arg := []int{3, 5, 4, 6}

	result := twosum(arr_arg, 7)

	fmt.Printf("%v", result)

}
