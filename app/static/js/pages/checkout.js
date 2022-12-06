import { hasClass, formAdress } from "../modules.js";

let accordion = document.querySelector(".accordion");

window.addEventListener("load", () => {
  // none_checkout();
  formAdress()
});
window.addEventListener("resize", () => {
  if (window.innerWidth >= 992) {
    if (hasClass(accordion, "active"))
      accordion.querySelector(".accordion__title").click();
  }
});
function none_checkout() {
  let re_checkout = document.querySelector("#re_checkout");

  re_checkout.classList.toggle("re-checkout__none");
}



