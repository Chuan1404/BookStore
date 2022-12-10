// query

window.addEventListener("load", () => {
  let buttons = document.querySelectorAll(".addToCart");
  let input = document.querySelector(".input-amount input");

  buttons.forEach((btn, index) => {
    btn.addEventListener("click", (e) => {
      let id = e.currentTarget.getAttribute("pro_id");
      let img = e.currentTarget.getAttribute("pro_img");
      let name = e.currentTarget.getAttribute("pro_name");
      let price = e.currentTarget.getAttribute("pro_price");
      let amount = input.value;
      addToCart(id, img, name, price, amount, index);
    });
  });

  function addToCart(id, img, name, price, amount, index) {
    fetch("/api/add-cart", {
      method: "post",
      body: JSON.stringify({
        id: id,
        img: img,
        name: name,
        price: price,
        amount: amount
      }),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then(function (res) {
        return res.json();
      })
      .then(function (data) {
        let counter = document.querySelector("#cartCounter");
        counter.innerText = data.total_header_cart;
        if (index == 0) {
          window.scrollTo(0, 0);
        } else window.location.pathname = "/checkout";
      })
      .catch(function (err) {
        console.error(err);
      });
  }
});
