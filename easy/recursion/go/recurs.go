package main 

import (
	"fmt"
)

func recurs(num int) int {
	if num <= 1 {
		return 1
	} 

	return num * num + recurs(num - 1)

}

func main() {
	fmt.Println("This should return 385, we are passing the number 10")
	result := recurs(10)
	fmt.Printf("%v\n", result)
}
