import { hasClass, formAddress } from "../modules.js";

let accordion = document.querySelector(".accordion");
let orderForm = document.querySelector("#order-form");
let submitBtn = document.querySelector("#btn-submit");

window.addEventListener("load", () => {
  // none_checkout();
  formAddress();

  submitBtn.addEventListener("click", (e) => {
    e.preventDefault();

    if (confirm("Bạn chắc chắn muốn thanh toán không?") == true) {

      const formData = {
        name: orderForm.querySelector("input[name='name']").value,
        phone_number: orderForm.querySelector("input[name='phone_number']")
          .value,
        city: orderForm.querySelector("select[name='city']").value,
        district: orderForm.querySelector("select[name='district']").value,
        ward: orderForm.querySelector("select[name='ward']").value,
        address: orderForm.querySelector("textarea[name='address']").value,
        pay_method: orderForm.querySelector("select[name='pay_method']")
      };

      fetch("/api/checkout", {
        method: "post",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      })
        .then(function (res) {
          return res.json();
        })
        .then(function (data) {
          if (data.status == 200) {
            console.log(window.location)
            window.location.pathname = '/user_order'
          }
          else {
            alert(data.err)
          }
        })
        .catch(function (err) {
          console.error(err);
        });
    }
  });
});
window.addEventListener("resize", () => {
  if (window.innerWidth >= 992) {
    if (hasClass(accordion, "active"))
      accordion.querySelector(".accordion__title").click();
  }
});
