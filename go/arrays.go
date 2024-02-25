package main

import "fmt"

func main() {
	// collection of items with same type
	// Fixed size
	grades := [3]int{97, 85, 93}
	fmt.Println("grades:", grades)

	var students [3]string
	students[0] = "Ash"
	fmt.Println(students)
	fmt.Println("# of students:", len(students))

	a := [3]int{1, 2, 3}
	b := a
	b[1] = 5
	fmt.Println(b)
}
