package main

import "fmt"

// variables > Store information or data
func main() {

	// var variableName dataType
	// Strings
	var nameOne string = "mario"
	var nameTwo = "ash"
	var nameThree string

	nameThree = "peach"
	fmt.Println(nameOne, nameTwo, nameThree)

	// integers
	var a int = 42
	b := 42 //shorthand
	fmt.Println(a + b)

	// bits & memory
	var numberOne int8 = 57 //- 127 to 127
	fmt.Println(numberOne)

}
