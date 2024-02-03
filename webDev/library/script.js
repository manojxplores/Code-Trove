function Book(title, author, status){
    this.title = title;
    this.author = author;
    this.status = status;
}

const myLibrary = [];
let bookCounter = 0;

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

    const edit_container = document.createElement('div');
    edit_container.classList.add(`${bookCounter++}`);
    
    
    const removeBtn = document.createElement('button');
    removeBtn.textContent = 'Remove';
    removeBtn.addEventListener('click', function() {
        removeBook(book);
    });

    edit_container.appendChild(removeBtn);
    container.appendChild(ul);
    container.appendChild(edit_container);
    main.appendChild(container);
}

function newBook(){
    const title = document.getElementById('title').value;
    const author = document.getElementById('author').value;
    const status = document.getElementById('status').value;
    const newBookObj = new Book(title, author, status);
    myLibrary.push(newBookObj);
    addBook(newBookObj);
}

function removeBook(book) {
    const index = myLibrary.indexOf(book);
    if (index !== -1) {
        myLibrary.splice(index, 1);
        refreshLibrary();
    }
}

function refreshLibrary() {
    const main = document.getElementById('main');
    main.innerHTML = ''; 

    myLibrary.forEach(addBook);
}

const new_btn = document.getElementById('btn');
new_btn.addEventListener('click', function(){
    newBook();
});
