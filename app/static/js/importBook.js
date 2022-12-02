// execute when html loaded
window.addEventListener("load", () => {
  let dateInput = document.querySelector("#date");
  setInputValue(dateInput)

  dateInput?.addEventListener("change", (e) => {
    window.location.search = `?current_date=${e.target.value}`
  });

});

function setInputValue(input) {
  let search = window.location.search
  if (search) {
    input.value = search.split('=')[1]
  }
}