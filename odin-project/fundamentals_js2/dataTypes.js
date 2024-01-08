console.log('test')

// PRIMITIVE DATA TYPES:
// Contain only a single thing


// Dynamically typed-->Variables are not bound to a single data type
let message = "Hello!"
message = 123456

// Number -->Represents both integer & Floating point number

// alert(Infinity)
// alert(1 / 0) --> Infinity

console.log(NaN)//Not a number

// BIGINT
// In JavaScript, the “number” type cannot safely represent integer values larger than (253-1) (that’s 9007199254740991), or less than -(253-1) for negatives.

// STRINGS:
let str = "hello!"
let str2 = 'Single quotes are ok too'

let name = 'John'
// Embed a variable using backticks
console.log(`Nice to meet you ${name}`)

// The result is 3
console.log(`The result is ${1 + 2}`)
// The result is {1 + 2}
console.log("The result is {1 + 2}")


//BOOLEAN
let nameFieldChecked = true
let ageFieldChecked = false

// NULL
let age = null

// UNDEFINED
// a variable is declared, but not assigned
let a;
a = undefined


