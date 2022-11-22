// functions work with class
export function addClass(element, className) {
  className = className.split(" ");
  return className.forEach((classname) => element.classList.add(classname));
}

export function hasClass(element, className) {
  return element.classList.contains(className);
}

export function removeClass(element, className) {
  className = className.split(" ");

  return className.forEach((classname) => element.classList.remove(classname));
}

export function toggleClass(element, className) {
  return element.classList.toggle(className);
}

// functions work with .cardbox
export function activeCardbox() {
  // query all elements have .cardbox
  let cardbox = document.querySelectorAll(".cardbox");

  cardbox.forEach((item) => {
    item.addEventListener("click", (e) => {
      // check parent of item has class cardbox-parent
      let condition = hasClass(item.parentNode, "cardbox-parent");
      if (condition) {
        let siblings = getAllSiblings(item);

        // remove .active of all siblings
        siblings.forEach((sib) => removeClass(sib, "active"));
        addClass(item, "active");
      }
    });
  });
}

// function work with .accordion
export function accordion() {
  let accordion_titles = document.querySelectorAll(".accordion__title");

  accordion_titles.forEach((title) => {
    title.addEventListener("click", () => {
      toggleClass(title.parentNode, "active");

      let panel = title.nextElementSibling;
      panel.style.maxHeight = hasClass(title.parentNode, "active")
        ? panel.scrollHeight + "px"
        : 0;
    });
  });
}
// functions use to get all siblings of element

export function getAllSiblings(element) {
  let currentItem = element.parentNode.firstChild; // first element
  let sibs = [];

  do {
    if (currentItem.nodeType == 3) continue; //text node
    sibs.push(currentItem);
  } while ((currentItem = currentItem.nextSibling));

  return sibs;
}
// function work with .re-checkout__none
export function none_checkout() {
  let re_checkout = document.querySelectorAll("#re_checkout");
  console.log("Hello");

  re_checkout.classList.toggle("re-checkout__none");
}

// function work with form
export function validate({ form, nameInputList = [], options = {} }) {
  let emailRegex =
    /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  let phoneRegex =
    /^[(]{0,1}[0-9]{3}[)]{0,1}[-\s\.]{0,1}[0-9]{3}[-\s\.]{0,1}[0-9]{4}$/;
  let errs = {};
  nameInputList.forEach((name) => {
    let currentInput = form.querySelector(`input[name=${name}]`);

    if (!currentInput.value) errs[name] = "This field must not be blank";
    else if (name == "username" && currentInput.value.length < 6)
      errs[name] = "6 characters at least";
    else if (name == "email" && !emailRegex.test(currentInput.value))
      errs.email = "Invalid email";
    else if (name == "phone_number" && !phoneRegex.test(currentInput.value))
      errs[name] = "Invalid phone number";
    else if (name == "password" && currentInput.value.length < 3)
      errs[name] = "3 characters at least";
    else if (name == "confirm") {
      let password = form.querySelector('input[name="password"').value;
      if (currentInput.value != password)
        errs.confirm = "Password and confirm password are not the same";
    }
  });

  return errs;
}
