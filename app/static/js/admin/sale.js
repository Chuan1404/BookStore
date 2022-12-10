// execute when html loaded
window.addEventListener("load", () => {
  let addProductBtn = document.querySelector("#addProduct");
  let exportReceiptBtn = document.querySelector('#export-receipt')

  let code_input = document.querySelector("#code");
  let cardbox = document.querySelectorAll(".cardbox");
  let inputAmount = document.querySelectorAll(".input-amount");

  addProductBtn.addEventListener("click", (e) => {
    e.preventDefault();
    add_book_by_id(code_input.value);
  });

  exportReceiptBtn?.addEventListener('click', e => {
    e.preventDefault()
    let form = document.forms[0]
    let formData = new FormData(form);
    let formProps = Object.fromEntries(formData);
    if(formProps.name == 0) alert('Chưa nhập tên khách hàng')
    else form.submit()
  })

  cardbox.forEach((c) =>
    c.addEventListener("click", (e) =>
      delete_book_by_id(e.currentTarget.getAttribute("book_id"))
    )
  );

  inputAmount.forEach((item) => {
    let buttons = item.querySelectorAll("button");
    let input = item.querySelector("input");

    input.addEventListener('blur', e => {
      update_amount_book(item.getAttribute("pro_id"), input.value);
    })

    buttons.forEach((btn) => {
      btn.addEventListener("click", (e) => {
        update_amount_book(item.getAttribute("pro_id"), input.value);
      });
    });
  });

  function add_book_by_id(id) {
    fetch("/api/pay/add", {
      method: "post",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(id),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data)
        data.status == 400 && alert(data.err);
        data.status == 200 && location.reload();
      });
  }

  function update_amount_book(id, newAmount) {
    fetch("/api/pay/update", {
      method: "post",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ id, newAmount }),
    })
      .then((res) => res.json())
      .then((data) => data.status == 200 && location.reload());
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
