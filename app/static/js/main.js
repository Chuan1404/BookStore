import { accordion, activeCardbox, addClass, toggleClass } from "./modules.js";

let userCard = document.querySelector(".header__card .user");
let headerBox = document.querySelector(".header__box");
// execute when html loaded
window.addEventListener("load", () => {
  activeCardbox();
  accordion();

  userCard.addEventListener("click", (e) => {
    toggleClass(headerBox, "active");
  });
});
