function Book(title, author, status) {
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
        li.textContent = `${book[key]}`; // Display key-value pairs
        ul.appendChild(li);
    }

    const removeBtn = document.createElement('button');
    removeBtn.textContent = 'Remove';
    removeBtn.addEventListener('click', function () {
        removeBook(book);
    });

    const edit_status = document.createElement('button');
    edit_status.textContent = 'Edit Status'
    edit_status.addEventListener('click', function () {
        book.status = book.status === 'Read' ? 'Not Yet' : 'Read';
        refreshLibrary();
    });

    container.appendChild(ul);
    container.appendChild(removeBtn);
    container.appendChild(edit_status);
    main.appendChild(container);
}

function newBook() {
    const title = document.getElementById('title').value;
    const author = document.getElementById('author').value;
    const status = document.getElementById('status').value;
    const newBookObj = new Book(title, author, status);
    myLibrary.push(newBookObj);
    addBook(newBookObj);
    console.log(myLibrary);
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
    console.log(myLibrary);
}

const new_btn = document.getElementById('btn');
new_btn.addEventListener('click', function () {
    newBook();
});
