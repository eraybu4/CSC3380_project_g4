// fake star count (idk what will happen)
const userStars = 120;

// wait for page load
document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".card");

  cards.forEach(card => {
    const btn = card.querySelector(".star-btn");
    if (!btn) return;

    const starCost = parseInt(btn.textContent);

    // check stars
    if (userStars < starCost) {
      btn.disabled = true;
      btn.classList.add("disabled");
      btn.title = "You need more stars for this reward 😔";
    } else {
      btn.title = "Click to redeem ✨";
    }

    // click highlight
    btn.addEventListener("click", () => {
      cards.forEach(c => c.classList.remove("selected"));
      card.classList.add("selected");

      const rewardName = card.querySelector("h3").textContent;
      alert(`You picked:\n${rewardName}`);
    });
  });
});
