// functions work with class
export function addClass(element, className) {
    return element.classList.add(className)
}

export function hasClass(element, className) {
    return element.classList.contains(className)
}

export function removeClass(element, className) {
    return element.classList.remove(className)
}

export function toggleClass(element, className) {
    return element.classList.toggle(className)
}

// functions work with .cardbox
export function activeCardbox() {
    // query all elements have .cardbox
    let cardbox = document.querySelectorAll('.cardbox')


    cardbox.forEach(item => {
        item.addEventListener('click', (e) => {
            // check parent of item has class cardbox-parent
            let condition = hasClass(item.parentNode, 'cardbox-parent')
            if (condition) {
                let siblings = getAllSiblings(item)

                // remove .active of all siblings
                siblings.forEach(sib => removeClass(sib, 'active'))
                addClass(item, 'active')
            }
        })
    })
}

// function work with .accordion
export function accordion() {
    let accordion_titles = document.querySelectorAll('.accordion__title')

    accordion_titles.forEach(title => {
        title.addEventListener('click', () => {
            toggleClass(title.parentNode, 'active')

            let panel = title.nextElementSibling
            panel.style.maxHeight = hasClass(title.parentNode, 'active') ? panel.scrollHeight + 'px' : 0
        })
    })
}
// functions use to get all siblings of element

export function getAllSiblings(element) {
    let currentItem = element.parentNode.firstChild // first element
    let sibs = []

    do {
        if (currentItem.nodeType == 3) continue; //text node
        sibs.push(currentItem)
    } while (currentItem = currentItem.nextSibling)

    return sibs
}

