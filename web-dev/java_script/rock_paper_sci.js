function getComputerChoice() {
    let num = Math.floor((Math.random() * 3) + 1);
    let str;
    if (num == 1) {
        str = 'r';
    } else if (num == 2) {
        str = 'p';
    } else {
        str = 's';
    }
    return str;
}

function playRound(playerSelection, computerSelection) {
    let result;

    if (playerSelection === computerSelection) {
        result = 'Thats a tie';
    } else if (playerSelection === 'r' && computerSelection === 'p') {
        result = 'you lose';
    } else if (playerSelection === 'r' && computerSelection === 's') {
        result = 'you win';
    } else if (playerSelection === 'p' && computerSelection === 's') {
        result = 'you lose';
    } else if (playerSelection === 'p' && computerSelection === 'r') {
        result = 'you win';
    } else if (playerSelection === 'p' && computerSelection === 'p') {
        result = 'Thats a tie';
    } else if (playerSelection === 's' && computerSelection === 'p') {
        result = 'you win';
    } else if (playerSelection === 's' && computerSelection === 'r') {
        result = 'you lose';
    } else if (playerSelection === 's' && computerSelection === 's') {
        result = 'Thats a tie';
    }

    return result;
}

let result = playRound(prompt('Enter your choice:'), getComputerChoice());
console.log(result);

