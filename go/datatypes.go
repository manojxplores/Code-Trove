package main

import (
	"fmt"
	"math"
)

/* basic types in go:
bool
string
int int 8 int 16 int 32 int 64
float32 float64
complex64 complex128
*/

func main() {

	var a int8 = 65
	var b float32 = 3.14
	var c string = "Hello world!"
	var d bool = true

	fmt.Println(a, b, c, d)

	fmt.Print("hello, ") //doesnt add a new line
	fmt.Println("world! ")
	fmt.Println("Ash")

	age := 35
	name := "Shaun"
	fmt.Println("my name is ", name, " & my age is", age)

	// Formatted string > String with variables embedded inside it
	// %_ > Format specifier
	fmt.Printf("my name is %v & my age is %v \n", name, age)
	fmt.Printf("my name is %q & my age is %q \n", name, age)
	fmt.Printf("my name is %v & my age is %v \n", name, age)

	value := math.Pi
	fmt.Printf("The value of pi is %0.3f", value)

}
