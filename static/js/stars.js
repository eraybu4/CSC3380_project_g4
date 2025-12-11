/**
* stars.js
* Increments through star PNGs and updates the PNG if the starTotal amount is met. 
* When the user enters the amount, the corresponding stars will light up. 
*/

document.getElementById("enterButton").addEventListener("click", function(e) {

const starTotal = Number(document.getElementById("starAmount").value);
    e.preventDefault();


for (let i = 1; i <= 17; i++) {

    const starElement = document.getElementById("star" + i);
    if (starTotal >= i) {
        starElement.src = "img/StarActivated.png";

    } else {
        starElement.src = "img/StarNotActivated.png"
    }
}


});


