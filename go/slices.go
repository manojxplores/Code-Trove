package main

import "fmt"

func main() {
	// dynamically-sized
	withData := []int{0, 1, 2, 3, 4, 5}
	fmt.Println(withData[3])

	newSlice := withData[2:4]
	fmt.Println(newSlice)
	nextSlice := append(newSlice, 42, 8)
	fmt.Println(nextSlice)

	a := make([]int, 5)
	fmt.Println(a)
}
