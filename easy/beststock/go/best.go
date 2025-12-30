package main

import (
	"fmt"
)

type Solution struct {
	prices []int
}

func NewSolution() *Solution {
	return &Solution{
		prices: []int{2, 5, 4, 3, 1, 6, 3, 5, 8},
	}
}

func (s *Solution) BestProfit() int {
	left, right := 0, 1
	maxProfit := 0

	for right < len(s.prices) {
		if s.prices[left] < s.prices[right] {
			profit := s.prices[right] - s.prices[left]
			
			if profit > maxProfit {
				maxProfit = profit
			}
		} else {
			left = right
		}

		right++
	}

	return maxProfit
}

func main() {

	solution := NewSolution()

	result := solution.BestProfit()

	fmt.Println("This is the best stock we are passing [2, 5, 4, 3, 1, 6, 3, 5, 8]")
	fmt.Println("This should return 7, which is the max profit of 1 and 8")
	fmt.Printf("%v", result)
}
