
function showMessage(){
    console.log('Hello, everyone')
} //function declaration
 
showMessage(); //function call

// LOCAL VARIABLE
// a variable declared inside a function is only visible inside the function

let name = 'John'
// a variable declared outside of any function are called global
function message(){
    greetings = `Congratulations! ${name}`
    console.log(greetings)
}

message();

function add7(num){
    return num + 7;
}
console.log(add7(3))

function multiply(num1, num2){
    return num1*num2
}

result = multiply(42, 4)
console.log(result)


function capitalize(str){
    return str.charAt(0).toUpperCase() + str.slice(1, ).toLowerCase(); 
}

str2 = capitalize("oPENSOUrce")
console.log(str2)

function lastLetter(str){
    return str.charAt((str.length - 1))
}

str3 = lastLetter("heyya")
console.log(str3)