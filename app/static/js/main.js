// query


window.onload = () => {
    activeCardbox()
}

// functions work with class
function addClass(element, className) {
    return element.classList.add(className)
}

function hasClass(element, className) {
    return element.classList.contains(className)
}

function removeClass(element, className) {
    return element.classList.remove(className)
}

// functions work with .cardbox
function activeCardbox() {
    // query all elements have .cardbox
    let cardbox = document.querySelectorAll('.cardbox')


    cardbox.forEach(item => {
        item.addEventListener('click', (e) => {
            //check parent of item has class cardbox-parent
            condition = hasClass(item.parentNode, 'cardbox-parent')
            if (condition) {
                siblings = getAllSiblings(item)

                siblings.forEach(sib => removeClass(sib, 'active'))
                addClass(item, 'active')
            }
        })
    })
}

// functions work to get all siblings of element

function getAllSiblings(element) {
    let currentItem = element.parentNode.firstChild // first element
    let sibs = []

    do {
        if (currentItem.nodeType == 3) continue; //text node
        sibs.push(currentItem)
    } while (currentItem = currentItem.nextSibling)

    return sibs
}

