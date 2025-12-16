package main 

import (
	"fmt"
)

func binarysearch(nums []int, target int) int {

	var low int = 0
	var high int = len(nums)
	var iterations int = 0

	for low <= high {
		var mid int = (low + high) / 2
		var guess int = nums[mid]

		if guess == target {
			fmt.Printf("That is right! The guess is %v", guess)
			return mid
		}

		if guess > target {
			high = mid - 1
		} else {
			low = mid + 1
		}

		fmt.Printf("Count of iterations: %v\n", iterations)
		fmt.Printf("Guess: %v\n", guess)
		iterations = iterations + 1
	}

	return -1
}

func main() {
	fmt.Println("This first case is the numbers 1-100 with a target of 82")
	
	arr_arg := make([]int, 100)

	for i := range arr_arg {
		arr_arg[i] = i + 1
	}

	binarysearch(arr_arg, 82)
}
