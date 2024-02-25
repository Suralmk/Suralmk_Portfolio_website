const navBar = document.querySelector('.navbar_container')
window.addEventListener('scroll', () => {
  navBar.classList.toggle('stick', this.window.scrollY > 0)
})

// const BASE_URL = 'http://127.0.0.1:2500/subscribe/'
// const csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0]
//   .defaultValue
// console.log()
// const subForm = document.getElementById('subscription_formm')
// subForm.addEventListener('submit', async event => {
//   event.preventDefault()
//   const email = event.target.querySelector('#email').value

//   if (validateSubscription() === false) {
//     return
//   } else {
//     var options = {
//       method: 'POST',
//       headers: {
//         'content-Type': 'application/json',
//         'X-CSRFToken': csrftoken
//       },
//       body: {
//         email: JSON.stringify(email),
//         age: 12
//       }   
//     }
//     try {
//        $.a (BASE_URL, options)
//        console.log(options)
//     } catch (err) {
//       console.log(err)
//     }

//   }
// })

// const validateSubscription = () => {
//   var input,
//     i,
//     valid = true
//   input = subForm.getElementsByTagName('input')
//   for (i = 0; i < input.length; i++) {
//     if (input[i].value == '') {
//       document.querySelector('.subscribe_message').style.display = 'flex'
//       document.querySelector('.subscribe_message').innerHTML =
//         'Email is required!'
//       valid = false
//     }
//   }
//   return valid // return the valid status
// }

const searchBtn = document.getElementById('search-btn')
const searchDialog = document.querySelector('dialog')
searchBtn.addEventListener('click', () => {
  searchDialog.showModal()
})

searchDialog.addEventListener('click', e => {
  const searchFormDim = searchDialog.getBoundingClientRect()
  if (
    e.clientX < searchFormDim.left ||
    e.clientX > searchFormDim.right ||
    e.clientY < searchFormDim.top ||
    e.clientY > searchFormDim.bottom
  ) {
    searchDialog.close()
  } else {
  }
})

document.getElementById('switch-dark').addEventListener('click', () => {
  document.body.classList.toggle('dark-theme')
})
