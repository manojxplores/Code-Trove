// variables are containers for storing values
// var x = 5
// var y = 6

// console.log(x + y)

let x = 4
let y = 3
console.log(x + y)

x = 10
console.log(x + y)

// constant values cannot be changed

const price1 = 80
const price2 = 90
// price2 = 79
// console.log(price2)


// names may contain letters, digits , underscore and even '$'
// name must begin with either a letter or underscore or '$'
// names are case-sensitive
// JS keywords cannot be used as variable names

let person, car;

person = 'john'
car = "Volvo"
console.log(person, car)

// ES6 introduced const and let keyword which have Block scope
// Variables defined with let cannot be redeclared
// But using var keyword, we can redeclare variables again

let name = "ash"

/*
{  Not allowed since let has blockscope
    let a = 42
    let a = 89
}

{
let a = 42;
var a = 56
} 

{
    var a = 42;
    let a = 53
}

{
    let a = 42
}
// console.log(a) --->throws an error (let has block scope)
{
    var text = "hola"
}

console.log(text) 
// (var has global scope)

*/



// OPERATORS
/* ARITHMETIC OPERATORS( +, -, *, %, **, /)
   ASSIGNMENT OPERATORS( %=, +=, -=, *= , /=...)
   COMPARISION OPERATORS( ==, !+, >, <, >= , <=, ?)
   LOGICAL OPERATORS(&&, ||, !)

*/

let text1 = "John "
let text2 = "Doe"
console.log("Good Morning " + text1 + text2)

// DATA TYPES

// JS is a dynamically typed language 
// same variable can hold mulitple data types
let counter = 120
console.log(typeof counter)
counter = false
console.log(typeof counter)

let counter2; 
console.log(typeof counter2)


const cars = ['volvo', 'bmw', 'ferrari']
// we can access the array items using index
console.log(cars[0])

const person1 = {
    firstName : 'ash',
    lastName : 'Ketchum',
    age : 18
}


