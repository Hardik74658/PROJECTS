let randomNumber = 0;
let result = "";
let score = JSON.parse(localStorage.getItem("score")) || {
    win: 0,
    lose: 0,
    tie: 0,
};
document.querySelector(
    ".js-scores"
).innerHTML = `Wins : ${score.win} , Losses : ${score.lose} , Ties : ${score.tie} `;
function resetScores() {
    score.win = 0;
    score.lose = 0;
    score.tie = 0;
    localStorage.removeItem("score");
    document.querySelector(
        ".js-scores"
    ).innerHTML = `Wins : ${score.win} , Losses : ${score.lose} , Ties : ${score.tie} `;
    document.querySelector(".js-result").innerHTML = "";
    document.querySelector(".js-move").innerHTML = "";
}



function playGame(playerMove) {
    let computerMove = pickComputerMove();
    if (playerMove === computerMove) {
        result = "Tie";
    } else if (playerMove === "Rock") {
        if (computerMove === "Paper") {
            result = "You Lose";
        } else {
            result = "You Win";
        }
    } else if (playerMove === "Paper") {
        if (computerMove === "Scissors") {
            result = "You Lose";
        } else {
            result = "You Win";
        }
    } else if (playerMove === "Scissors") {
        if (computerMove === "Rock") {
            result = "You Lose";
        } else {
            result = "You Win";
        }
    }
    if (result === "You Win") {
        score.win++;
    } else if (result === "You Lose") {
        score.lose++;
    } else {
        score.tie++;
    }
    localStorage.setItem("score", JSON.stringify(score));
    document.querySelector(
        ".js-scores"
    ).innerHTML = `Wins : ${score.win} , Losses : ${score.lose} , Ties : ${score.tie} `;
    document.querySelector(".js-result").innerHTML = `${result}.`;
    document.querySelector(
        ".js-move"
    ).innerHTML = `You <img src="img/${playerMove}-emoji.png" alt="" srcset="" /> <img src="img/${computerMove}-emoji.png" alt="" srcset="" />   Computer`;
    // alert(
    // 	`You Pick ${playerMove},Computer Pick ${computerMove},${result}.
    //     Win : ${score.win} Lose : ${score.lose} Tie : ${score.tie} `
    // );
}
function pickComputerMove() {
    let randomNumber = Math.random();
    if (randomNumber >= 0 && randomNumber < 0.33) {
        computerMove = "Rock";
    } else if (randomNumber >= 0.33 && randomNumber < 0.66) {
        computerMove = "Paper";
    } else {
        computerMove = "Scissors";
    }
    return computerMove;
}

var intervalId ;
var isAutoPlaying = false;

function autoPlay(){

    if(!isAutoPlaying)
    {
        intervalId = setInterval(() => {
            playGame(pickComputerMove());
            isAutoPlaying = true;
        },1000)
    }
    else{
        clearInterval(intervalId);
        isAutoPlaying=false;
    }
}

document.querySelector(".reset-btn").addEventListener("click",()=> {
    resetScores();
})
document.querySelector(".auto-play-btn").addEventListener("click",()=> {
    autoPlay();
})
document.querySelector(".rock-btn").addEventListener("click",()=>{
    playGame("Rock")
})
document.querySelector(".paper-btn").addEventListener("click",()=>{
    playGame("Paper")
})
document.querySelector(".scissor-btn").addEventListener("click",()=>{
    playGame("Scissors")
})
document.body.addEventListener("keydown",(event) => {
    if(event.key == "r" || event.key == "R"){
        playGame("Rock");     
    }
    else if(event.key == "p" || event.key == "P"){
        playGame("Paper");
    }
    else if(event.key == "s" || event.key == "S"){
        playGame("Scissors");
    }
});