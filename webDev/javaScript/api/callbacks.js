// callbacks are the functions that are passed onto to another function as an argument
// synchronous prog
let a = "Ash"
let b = 21
console.log(`${a} is ${b} years old`);

// Asynchronous prog
console.log('start')
setTimeout(function(){
    console.log("hello world!")
}, 3000)

console.log('end')

let promise = new Promise(function(resolve, reject){
    console.log('hola!')
})
console.log('hello!')
setTimeout(function(){
    console.log('see you in 2 secs')
}, 2000)
console.log('Myself Ash')