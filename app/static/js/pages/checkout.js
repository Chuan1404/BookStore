// import { addClass, hasClass, removeClass } from "../modules.js";

// query

window.addEventListener("load", () => {
  // viewMode();
  none_checkout();
});
function none_checkout() {
  let re_checkout = document.querySelector("#re_checkout");

  re_checkout.classList.toggle("re-checkout__none");
}

function addToCart(id, img, name, price) {
  fetch("/api/add-cart", {
    method: "post",
    body: JSON.stringify({
      id: id,
      img: img,
      name: name,
      price: price,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then(function (res) {
      console.info(res);
      return res.json();
    })
    .then(function (data) {
      console.info(data);

      let counter = document.querySelector("#cartCounter");
      counter.innerText = data.total_quantity;
    })
    .catch(function (err) {
      console.error(err);
    });
}
