
let container = document.querySelector(".container");
let createGridBtn = document.querySelector("#create-grid");
let clearGridBtn = document.querySelector("#clear-grid");
let widthRange = document.querySelector("#width-range");
let heightRange = document.querySelector("#height-range");
let widthValue = document.querySelector("#width-value");
let heightValue = document.querySelector("#height-value");
let colorInput = document.querySelector('#color-input');
let eraseBtn = document.querySelector('#erase-btn');
let paintBtn = document.querySelector('#paint-btn');

createGridBtn.addEventListener('click', function(){
    for(let i = 0; i < widthRange.value; i++){
        const gridCol = document.createElement('div');
        gridCol.classList.add('gridCol');
        gridCol.textContent = 'test'
        container.appendChild(gridCol)
    }
})




