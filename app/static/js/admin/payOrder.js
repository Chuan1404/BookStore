window.addEventListener("load", (e) => {
  let payOderderBtn = document.querySelector("#payOrder");

  payOderderBtn?.addEventListener("click", (e) => {
    if(confirm('Xác nhận thanh toán hóa đơn')) payOrder(e.currentTarget.getAttribute("order_id"));
  });
});

function payOrder(id) {
  fetch("/api/pay-order", {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(id),
  })
    .then((res) => res.json())
    .then(data => data.status && location.reload())
}
