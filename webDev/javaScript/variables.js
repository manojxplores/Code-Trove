// variables are storage containers for data
// we use let keyword to create a variable

let message;
message = "Hello!"

console.log(message)

// We can declare multiple variables in a single line
// not recommended
let user = 'John', age = 18, msg = "hello!"


console.log(age)
// a variable can be declared only once
message = 'World!'
console.log(message)

/*the first character must not be a digit
the name must contain only digits, letters, '_', '$' 
variable name must not be reserved keywords */


// Once declared, const cannot be changed
const my_age = 19
// my_age  = 20 -->reassignment is not possible

console.log(23 + 97)
console.log((4 + 6 + 9) / 77)
let a = 10
console.log(a)
console.log(9*a)
let b = 7*a
console.log(b)

let MAX = 57
let actual = MAX - 13
let percentage = actual / MAX
console.log(percentage)