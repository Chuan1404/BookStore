import { inputAmount } from "../modules.js";

// execute when html loaded
window.addEventListener("load", () => {
  let addProductBtn = document.querySelector("#addProduct");
  let code_input = document.querySelector("#code");

  let cardbox = document.querySelector(".cardbox");

  inputAmount()


  addProductBtn.addEventListener("click", (e) => {
    e.preventDefault();
    get_book_by_id(code_input.value);
  });

  cardbox.addEventListener("click", (e) =>
    delete_book_by_id(e.currentTarget.getAttribute("book_id"))
  );


  function get_book_by_id(id) {
    fetch("/api/pay/add", {
      method: "post",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(id),
    })
      .then((res) => res.json())
      .then((data) => {
        data.status == 400 && alert(data.err);
        data.status == 200 && location.reload();
      });
  }

  function delete_book_by_id(id) {
    if (confirm("Xác nhận xóa ?")) {
      fetch("/api/pay/delete", {
        method: "post",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(id),
      })
        .then((res) => res.json())
        .then((data) => data.status == 200 && location.reload());
    }
  }
});
