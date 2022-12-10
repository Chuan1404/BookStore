import {
  accordion,
  activeCardbox,
  toggleClass,
  inputAmount,
  hasClass,
} from "./modules.js";

let userCard = document.querySelector(".header__card .user");
let headerBox = document.querySelector(".header__box");

let btns = document.querySelectorAll("button");
// execute when html loaded
window.addEventListener("load", () => {
  activeCardbox();
  accordion();
  inputAmount();

  btns.forEach((btn) => {
    if (hasClass(btn, "disable"))
      btn.addEventListener("click", (e) => e.preventDefault());
  });
  userCard?.addEventListener("click", (e) => {
    toggleClass(headerBox, "active");
  });
});
