package main

import "fmt"

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
}
