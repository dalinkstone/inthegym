package main

import (
	"fmt"
)

func quick_sort(nums []int) []int {

	return nums
}

func main() {
	fmt.Println("This is quick sort and we are passing the array [2, 3, 4, 1, 6, 5]")
	fmt.Println("This should return [1, 2, 3, 4, 5, 6]")

	input_nums := []int{2, 3, 4, 1, 5, 6}

	result := quick_sort(input_nums)

	fmt.Printf("%v", result)
}
