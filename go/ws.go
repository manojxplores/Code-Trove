package main

import (
	"fmt"
	"math"
)

func main() {

	fmt.Println("Welcome to Go workshop!")

	// Variable declaration
	// using "var" keyword
	var a string = "KOSS"
	var b int = 42
	var c, d = 10, 20
	fmt.Println(a, b, c, d)

	var e string
	fmt.Println(e)

	// Short Variable Declaration
	x, y := "hello", "world"
	fmt.Println(x, y)

	// If-else Statements
	n := 42
	if n%2 == 0 {
		fmt.Println("n is even")
	} else {
		fmt.Println("n is odd")
	}

	// For loop
	for i := 0; i <= 10; i++ {
		fmt.Println(i)
	}

	// NUMBER GUESSING GAME

	num, maxguesses := 25, 5
	for i := 0; i < maxguesses; i++ {
		fmt.Printf("You have %d guess(es)\n", maxguesses-i)
		fmt.Print("Enter number: ")
		var tmp int
		fmt.Scanln(&tmp)

		if tmp == num {
			fmt.Println("Correct!")
			break
		} else {
			fmt.Println("oops!")
		}
	}
	num = 63
	fmt.Println("You have Unlimited Guesses")
	for { // "while" loop
		var tmp int
		fmt.Scanln(&tmp)

		if tmp == num {
			fmt.Println("Correct!")
			break
		} else if tmp > num {
			fmt.Println("Lower..")
		} else {
			fmt.Println("Higher..")
		}
	}

	// Arrays
	var arr1 [5]int
	arr2 := [5]int{1, 2, 3, 4, 5}
	fmt.Println(arr1, arr2)

	arr2[3] = 7

	var twoD [2][3]int
	for i := 0; i < 2; i++ {
		for j := 0; j < 3; j++ {
			twoD[i][j] = i + j
		}
	}
	fmt.Println(twoD)

	// Slices
	sli := []string{"a", "b", "c"}
	fmt.Println(sli)
	fmt.Println(sli[1])

	sli = append(sli, "e", "f")
	fmt.Println(sli, len(sli))

	// maps
	// make(map[ key type ]value type)
	m := make(map[string]int)
	m["student1"] = 92
	m["student2"] = 85
	m["student3"] = 75
	fmt.Println(m)

	delete(m, "student3")
	fmt.Println(m)

	// structures
	mp := make(map[string]int) // Key: string, Value: int
	sl := make([]string, len(sli))
	copy(sl, sli)

	for _, str := range sl {
		mp[str]++
	}
	fmt.Println(sl, mp)

	val, isPresent := mp["d"] //  isPresent is an OPTIONAL return value
	fmt.Println(val, isPresent)
	delete(mp, "d")          // Delete a key
	val, isPresent = mp["d"] // If the key doesn't exist, zero value is returned
	fmt.Println(val, isPresent)

	var mp2 = map[int]string{
		1: "ONE",
		2: "TWO",
		3: "THREE",
	}
	for k, v := range mp2 {
		fmt.Println(k, "->", v)
	}

	// functions
	res := sum(3, 54)
	fmt.Println(res)

	num1, num2 := vals()
	fmt.Println(num1, num2)

	// Structs
	p1 := Point{"pt1", 12.23, 9.7}
	p2 := Point{X: 5.6, Y: 10.0}
	fmt.Println(p1.X, p2.Y)
	fmt.Println(p1.dist(p2))

}

// Functions
func sum(a int, b int) int {
	return a + b
}

// Multiple return values
func vals() (int, int) {
	return 45, 6
}

// Structs
type Point struct {
	// Fields
	label string
	X     float64
	Y     float64
}

// Struct Methods
func (p1 Point) dist(p2 Point) float64 {
	return math.Sqrt(sq(p1.X-p2.X) + sq(p1.Y-p2.Y))
}

func sq(n float64) float64 {
	return n * n
}
