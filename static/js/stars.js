document.getElementById("enterButton").addEventListener("click", function(e) {

const starTotal = Number(document.getElementById("starAmount").value);
    e.preventDefault();


for (let i = 1; i <= 17; i++) {

    const starElement = document.getElementById("star" + i);
    if (starTotal >= i * 5) {
        starElement.src = "img/StarActivated.png";

    } else {
        starElement.src = "img/StarNotActivated.png"
    }
}


});
