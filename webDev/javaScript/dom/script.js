console.log("Hello world!")
document.addEventListener('DOMContentLoaded', function () {
    // Your DOM manipulation code here
    const container = document.querySelector('.container')

    const blueHeading = document.createElement('h3')
    blueHeading.style.color = 'blue'
    blueHeading.textContent = "I'm a blue h3!"
    container.appendChild(blueHeading);

    const redParagraph = document.createElement('p')
    redParagraph.style.color = 'red'
    redParagraph.textContent = "Hey I'm red!"
    container.appendChild(redParagraph);

    const pinkDiv = document.createElement('div')
    pinkDiv.style.backgroundColor = 'pink'

    const h1Div = document.createElement('h1')
    h1Div.textContent = "I'm in a div!"
    pinkDiv.appendChild(h1Div)

    const pDiv = document.createElement('p')
    pDiv.textContent = "Me Too!"
    pinkDiv.appendChild(pDiv)

    container.appendChild(pinkDiv)

});


// function sum(a, b){
//     return a + b;
// }

// let sum = function(a, b){
//     return a + b;
// }

// let sum = (a, b) => a + b;
