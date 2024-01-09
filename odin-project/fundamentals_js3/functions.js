// Functions allow the code to be called many times without repetition

// Function Declaration

function showMessage(){
    alert('Hello everyone!!');
}
showMessage();

//Local variables
// we cannot access the variables which are declared inside the function

// Outer variables(Global variables)

let username = 'John'
function greeting(){
    console.log(`Nice to meet you, ${username}`)
}
greeting()
// We can modify the outer variable inside the function as well


// Assignment
function add7(num){
    return num + 7;
}
result = add7(3)
console.log(result)

function multiply(a, b){
    return a*b
}
result_n = multiply(4, 5)
console.log(result_n)

function capitalize(str){
    return str[0].toUpperCase() + str.slice(1).toLowerCase()
}

result_2 = capitalize('javaSCript')
console.log(result_2)


function lastLetter(str){
    return str.charAt(str.length -1)
}

result_3 = lastLetter('abcd')
console.log(result_3)