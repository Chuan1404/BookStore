import { hasClass, formAdress } from "../modules.js";

let accordion = document.querySelector(".accordion");

window.addEventListener("load", () => {
  // none_checkout();
  formAdress();
});
window.addEventListener("resize", () => {
  if (window.innerWidth >= 992) {
    if (hasClass(accordion, "active"))
      accordion.querySelector(".accordion__title").click();
  }
});
