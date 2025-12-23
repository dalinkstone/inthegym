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

func fibo(num int) int {
	if num == 0 {
		return 0
	}

	if num == 1 {
		return 1
	}

	return fibo(num - 1) + fibo(num - 2)
}

func main() {
	fmt.Println("This should return 385, we are passing the number 10")
	result := recurs(10)
	fmt.Printf("%v\n", result)

	fmt.Println("This should return the fibonacci of 10 intervals")
	result2 := fibo(10)
	fmt.Printf("%v\n", result2)
}
