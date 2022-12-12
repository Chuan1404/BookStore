window.addEventListener("load", async () => {
  let selects = document.querySelectorAll("select");
  let date = new Date();

  let searchObj = convert_search_to_object(window.location.search);

  if (!searchObj.month) searchObj.month = date.getMonth() + 1;
  if (!searchObj.year) searchObj.year = date.getFullYear();

  selects.forEach((select, index) => {
    select.querySelectorAll("option").forEach((item) => {
      !index
        ? item.value == searchObj.month &&
          item.setAttribute("selected", '1')
        : item.value == searchObj.year &&
          item.setAttribute("selected", '1');
    });

    select.addEventListener("change", (e) => {
      let value = e.currentTarget.value;

      !index
        ? (searchObj.month = value)
        : (searchObj.year = value);

      window.location.search = convert_object_to_search(searchObj);
    });
  });
});

function convert_search_to_object(search) {
  search = search ? search.slice(1).split("&") : search;

  let obj = {};
  search &&
    search.length &&
    search.forEach((query) => {
      query = query.split("=");

      obj[query[0]] = query[1];
    });

  return obj;
}

function convert_object_to_search(obj) {
  let search = "?";
  console.log(Object.entries(obj));
  Object.entries(obj).forEach((arr, index) => {
    search += index == 0 ? arr.join("=") : "&" + arr.join("=");
  });

  return search;
}
