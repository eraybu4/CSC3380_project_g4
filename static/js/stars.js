document.getElementById("enterButton").addEventListener("click", function(e) {

const starTotal = Number(document.getElementById("starAmount").value);
    e.preventDefault();


for (let i = 0; i <= 17; i++) {

    const starElement = document.getElementById("star" + i);
    if (starTotal >= i) {
        starElement.src = "img/StarActivated.png";

    } else {
        starElement.src = "img/StarNotActivated.png"
    }
}


});
