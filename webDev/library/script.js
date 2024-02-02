
function Book(title, author, num, status){
    this.title = title;
    this.author = author;
    this.num = num;
    this.status = status;
}

const myLibrary = []

function addBook(book) {
    const main = document.getElementById('main');
    const container = document.createElement('div');
    container.classList.add('container'); 
    const ul = document.createElement('ul');

    for (const key in book) {
        const li = document.createElement('li');
        li.textContent = `${book[key]}`;
        ul.appendChild(li);
    }

    container.appendChild(ul);
    main.appendChild(container);
}

function newBook(){
    const title = document.getElementById('title').value
    const author = document.getElementById('author').value;
    const num = document.getElementById('num').value;
    const status = document.getElementById('status').value;
    const newBookObj = new Book(title, author, num, status)
    myLibrary.push(newBookObj);
    addBook(newBookObj)
   
}

const book1 = new Book("Project Hail Mary", "Andy Weir", 475, false);

const btn = document.getElementById('btn');

const new_btn = document.getElementById('btn')
new_btn.addEventListener('click', function(){
    
    newBook();

})