package main

import (
	"fmt"
)

func InsertSort(nums []int) []int {
	for i := range len(nums) {
		j := i - 1
		for j >= 0 && nums[j+1] < nums[j] {
			temp := nums[j+1]
			nums[j+1] = nums[j]
			nums[j] = temp
			j--
		}
	}

	return nums
}

func main() {
	fmt.Println("This should sort the array [2, 3, 4, 1, 6]")
	fmt.Println("The output should be [1, 2, 3, 4, 6]")

	arr := []int{2, 3, 4, 1, 6}

	arr = InsertSort(arr)

	fmt.Printf("%v\n", arr)
}
