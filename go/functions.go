package main

import "fmt"

func add(x int, y int) int {
	return x + y
}

func swap(x string, y string) (string, string) {
	return y, x
}

func main() {
	fmt.Println(add(19, 13))
	a, b := swap("dont", "panic")
	fmt.Println(a, b)
}
