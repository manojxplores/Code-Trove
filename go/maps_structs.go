package main

import "fmt"

func main() {
	grade := map[string]int{
		"student1": 92,
		"student2": 83,
		"student3": 95,
	}
	fmt.Println(grade)

	score := grade["student2"]
	fmt.Println(score)
	_, ok := grade["student3"]
	fmt.Println(ok)

	// struct
	type person struct {
		name string
		age  int
	}
}
