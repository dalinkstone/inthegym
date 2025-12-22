package main

import (
	"fmt"
)

type Set struct {
	elements map[string]struct{}
}

func NewSet() *Set {
	return &Set {
		elements: make(map[string]struct{}),
	}
}

func (s *Set) Add(value string) {
	s.elements[value] = struct{}{}
}

func (s *Set) Remove(value string) {
	delete(s.elements, value)
}

func (s *Set) Contains(value string) bool {
	_, found := s.elements[value]
	return found
}

func lrp(text string) int {
	
	result := 0
	l := 0
	set := NewSet()

	for i := 0; i < len(text); i++ {
		for set.Contains(string(text[i])) {
			set.Remove(string(text[l]))
			l += 1
		}

		set.Add(string(text[i]))

		result = max(result, i - l + 1)

	}

	return result

}

func main() {
	fmt.Println("This should return 3 because we are testing xyzxyz")
	res := lrp("xyzxyz")
	fmt.Printf("%v\n", res)

	fmt.Println("This should return 4 because we test xxabcxxdf")
	res2 := lrp("xxabcxxdf")
	fmt.Printf("%v\n", res2)
}
