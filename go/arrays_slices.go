package main

import "fmt"

func main() {
	// Array > Fixed length
	// var ages [3]int = [3]int{20, 45, 30}
	var ages = [3]int{20, 45, 30} //infers the type automatically
	fmt.Println(ages, len(ages))

	names := [3]string{"peach", "mario", "ash"}
	fmt.Println(names, len(names))

	// Slices (use arrays under the hood)
	var scores = []int{100, 35, 46}
	scores_new := append(scores, 42) //doesnot change the original variables
	fmt.Println(scores_new, len(scores_new))

	// slice ranges
	rangeOne := names[1:3] //second index is exclusive
	fmt.Println(rangeOne)
	rangeTwo := names[2:]
	fmt.Println(rangeTwo)
}
