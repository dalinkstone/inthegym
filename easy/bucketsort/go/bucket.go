package main

import (
	"fmt"
)

func bucket_sort(nums []int) []int {
	return nums
}

func main() {
	fmt.Println("This is bucket sort and we are passing [2, 3, 4, 1, 6, 5]")
	fmt.Println("This should return [1, 2, 3, 4, 5, 6]")

	input_nums := []int{2, 3, 4, 1, 6, 5}

	result := bucket_sort(input_nums)

	fmt.Printf("%v", result)
}
