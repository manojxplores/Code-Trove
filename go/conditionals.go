package main

import (
	"fmt"
	"math/rand"
)

var num int = rand.Intn(50)

func main() {
	fmt.Println(num)
	if num%2 == 0 {
		fmt.Println("num is even")
	} else {
		fmt.Println("num is odd")
	}
}
