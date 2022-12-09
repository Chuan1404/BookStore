// query

window.addEventListener("load", () => {
  let buttons = document.querySelectorAll(".addToCart");

  buttons.forEach((btn) => {
    btn.addEventListener("click", async (e) => {
      let id = e.currentTarget.getAttribute("pro_id");
      let img = e.currentTarget.getAttribute("pro_img");
      let name = e.currentTarget.getAttribute("pro_name");
      let price = e.currentTarget.getAttribute("pro_price");
      await addToCart(id, img, name, price);
    });
  });

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
        return res.json();
      })
      .then(function (data) {
        let counter = document.querySelector("#cartCounter");
        counter.innerText = data.total_header_cart;
        window.location.pathname = '/checkout'
      })
      .catch(function (err) {
        console.error(err);
      });
  }
});
