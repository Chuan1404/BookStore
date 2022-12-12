// execute when html loaded
window.addEventListener("load", () => {
  let dateInput = document.querySelector("#date");
  let submitBtn = document.querySelector("#submitImport");

  setInputValue(dateInput);

  dateInput?.addEventListener("change", (e) => {
    window.location.search = `?current_date=${e.target.value}`;
  });

  submitBtn.addEventListener("click", async (e) => {
    e.preventDefault();
    if (confirm("Hoàn tất nhập?")) {
      const res = await submitNote(e.target.getAttribute("note_id"));

      if (res.status) window.location.reload();
    }
  });
});

function setInputValue(input) {
  let search = window.location.search;
  if (search) {
    input.value = search.split("=")[1];
  } else {
    let date = new Date();
    input.value = `${date.getFullYear()}-${date.getMonth() + 1}-${date
      .getDate()
      .toString()
      .padStart(2, "0")}`;
  }
}

function submitNote(note_id) {
  return fetch("/api/submit-note", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ note_id }),
  }).then((res) => res.json());
}
