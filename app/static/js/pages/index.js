import { addClass, hasClass, removeClass } from "../modules.js";

// query

window.addEventListener("load", () => {
  let buttons = document.querySelectorAll(".addToCart");

  buttons.forEach((btn) => {
    btn.addEventListener("click", async (e) => {
      let id = e.currentTarget.getAttribute("pro_id");
      let img = e.currentTarget.getAttribute("pro_img");
      let name = e.currentTarget.getAttribute("pro_name");
      let price = e.currentTarget.getAttribute("pro_price");
      console.log(id, img, name, price);
      await addToCart(id, img, name, price);
    });
  });

  viewMode();
});

function viewMode() {
  let homeProduct = document.querySelector(".home__shop--bottom");
  let products = homeProduct.querySelectorAll(".product");

  let gridMode = document.querySelectorAll(".home__shop--top .cardbox")[0];
  let listMode = document.querySelectorAll(".home__shop--top .cardbox")[1];

  // change view mode by clicking cardbox
  gridMode.addEventListener("click", () => {
    addClass(homeProduct, "grid");
    changeViewMode();
  });
  listMode.addEventListener("click", () => {
    removeClass(homeProduct, "grid");
    changeViewMode();
  });

  // change view mode
  function changeViewMode() {
    if (hasClass(homeProduct, "grid")) {
      products.forEach((product) => {
        addClass(product, "col-12 col-md-6 col-lg-4");
        removeClass(product, "row");
        removeClass(product.querySelector(".product__img"), "col-4");
        removeClass(product.querySelector(".product__info"), "col-8");
      });
    } else {
      products.forEach((product) => {
        removeClass(product, "col-12 col-md-6 col-lg-4");
        addClass(product, "row");
        addClass(product.querySelector(".product__img"), "col-4");
        addClass(product.querySelector(".product__info"), "col-8");
      });
    }
  }
}

