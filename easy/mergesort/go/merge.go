package main

import (
	"fmt"
)

func MergeNums(nums []int, start int, middle int, end int) []int {
	left := start
	right := middle + 1
	temp := []int{}

	for left <= middle && right <= end {
		if nums[left] <= nums[right] {
			temp = append(temp, nums[left])
			left++
		} else {
			temp = append(temp, nums[right])
			right++
		}
	}

	for left <= middle {
		temp = append(temp, nums[left])
		left++
	}

	for right <= end {
		temp = append(temp, nums[right])
		right++
	}

	for i := start; i <= end; i++ {
		nums[i] = temp[i-start]
	}

	return nums
}

func Merge(nums []int, start int, end int) []int {

	if end-start+1 <= 1 {
		return nums
	}

	middle := (start + end) / 2

	Merge(nums, start, middle)
	Merge(nums, middle+1, end)

	MergeNums(nums, start, middle, end)

	return nums
}

func main() {

	input_nums := []int{2, 3, 4, 1, 6, 5}

	fmt.Println("This is merge sort, we are passing the array [2, 3, 4, 1, 6, 5]")
	fmt.Println("This should return [1, 2, 3, 4, 5, 6]")

	result := Merge(input_nums, 0, len(input_nums)-1)

	fmt.Printf("%v", result)

}
