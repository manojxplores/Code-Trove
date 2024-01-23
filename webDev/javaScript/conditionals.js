// perform different actions based on diff conditions




let year = prompt("In which year ES16 was published?")

if (year == 2016) {
    console.log("you are right!")
} else {
    console.log("Nope")
}

let age = prompt('Enter your age:')

if (age <= 15){
    console.log("Hey kid!")
}else if(age < 21 && age > 15){
    console.log("Hello")
}else{
    console.log('Greetings!')
}