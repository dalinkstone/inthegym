package main

import (
	"fmt"
)

type Set struct {
	elements map[int]struct{}
}

func NewSet() *Set {
	return &Set {
		elements: make(map[int]struct{}),
	}
}

func (s *Set) Add(value int) {
	s.elements[value] = struct{}{}
}

func (s *Set) Contains(value int) bool {
	_, found := s.elements[value]
	return found
}

func containsdup(nums []int) bool {

	set := NewSet()

	for _, i := range nums {
		if set.Contains(i) == true {
			return true
		}

		set.Add(i)
	}

	return false
}

func main() {

	fmt.Println("This should return true. Passing [1, 4, 3, 2, 4]")

	arr_arg := []int{1, 4, 3, 2, 4}

	var result bool = containsdup(arr_arg)

	fmt.Print(result)

}
