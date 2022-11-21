import { addClass, hasClass, removeClass } from "../modules.js";

// query

window.addEventListener("load", () => {
  viewMode();
});
function none_checkout() {
  let re_checkout = document.querySelector("#re_checkout");
  console.log("Hello");

  re_checkout.classList.toggle("re-checkout__none");
}
