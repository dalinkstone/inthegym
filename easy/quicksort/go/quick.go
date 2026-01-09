package main

import (
	"fmt"
)

func quick_sort(nums []int, start int, end int) []int {

	if end - start <= 1 {
		return nums
	}

	pivot := nums[end]
	left := start

	for i := start; i < end; i++ {
		if nums[i] < pivot {
			temp := nums[left]
			nums[left] = nums[i]
			nums[i] = temp
			left++
		}
	}

	nums[end] = nums[left]

	nums[left] = pivot

	quick_sort(nums, start, left - 1)
	quick_sort(nums, left + 1, end)

	return nums
}

func main() {
	fmt.Println("This is quick sort and we are passing the array [2, 3, 4, 1, 6, 5]")
	fmt.Println("This should return [1, 2, 3, 4, 5, 6]")

	input_nums := []int{2, 3, 4, 1, 5, 6}

	result := quick_sort(input_nums, 0, len(input_nums) - 1)

	fmt.Printf("%v", result)
}
