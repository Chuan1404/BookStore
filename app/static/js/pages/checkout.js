import { hasClass, formAddress } from "../modules.js";

let accordion = document.querySelector(".accordion");
let orderForm = document.querySelector("#order-form");
let submitBtn = document.querySelector("#btn-submit");
let deleteBtn = document.querySelector("#delete-btn");

window.addEventListener("load", () => {
  formAddress();

  submitBtn.addEventListener("click", (e) => {
    e.preventDefault();

    if (confirm("Bạn chắc chắn muốn đặt sách không?") == true) {
      
      let form = new FormData(orderForm)
      let formData = Object.fromEntries(form)
      
      fetch("/api/checkout", {
        method: "post",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      })
        .then(function (res) {
          return res.json();
        })
        .then(function (data) {
          if (data.status == 200) window.location.pathname = "/user_order";
          else alert(data.err);
        })
        .catch(function (err) {
          console.error(err);
        });
    }
  });

  deleteBtn?.addEventListener("click", (e) => {
    if (confirm("Xác nhận xóa?")) {
      deleteCart(e.currentTarget.getAttribute('pro_id'));
    }
  });

  function deleteCart(id) {
    fetch("/api/checkout/delete", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(id),
    })
      .then((res) => res.json())
      .then((data) => data.status == 200 && window.location.reload());
  }
});
window.addEventListener("resize", () => {
  if (window.innerWidth >= 992) {
    if (hasClass(accordion, "active"))
      accordion.querySelector(".accordion__title").click();
  }
});
