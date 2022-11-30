// execute when html loaded
window.addEventListener("load", () => {
  let dateInput = document.querySelector("#date");

  dateInput.addEventListener("change", async (e) => {
    // const res = await get_note_by_date(e.target.value);
    // res.data = JSON.parse(res.data)
    // console.log(res)
  });

  // function get_note_by_date(date) {
  //   return fetch("/admin/import", {
  //     method: "POST",
  //     headers: {
  //       "Content-Type": "application/json",
  //     },
  //     body: JSON.stringify(date),
  //   }).then(res => res.json())
  // }
});
