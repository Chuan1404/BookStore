import { addClass, validate } from '../modules.js'

// query
let form = document.querySelector('form#register')
let submitBtn = form.querySelector('button')
window.addEventListener('load', () => {
    submitBtn.addEventListener('click', e => {
        e.preventDefault()

        // delete all err message
        form.querySelectorAll('p.text-danger').forEach(item => item.remove())

        // validate form
        let errs = validate({form: form, nameInputList: ['username', 'name', 'password', 'confirm', 'phone_number', 'email']})
        if (Object.keys(errs).length) {
            Object.keys(errs).forEach(name => {
                let input = form.querySelector(`input[name=${name}]`)
    
                // create err message
                let p = document.createElement('p')
                addClass(p, 'text-danger')
                p.innerHTML = errs[name]
    
                // add err message after input
                form.insertBefore(p, input.nextSibling)
    
            })
        }
        // validate success
        else {
            form.submit()
        }
    })
})


