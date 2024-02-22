const navBar = document.querySelector('.navbar_container')
window.addEventListener('scroll', () => {
  navBar.classList.toggle('stick', this.window.scrollY > 0)
})

const subForm = document.getElementById('subscription_form')

subForm.addEventListener('submit', e => {
  e.preventDefault()

  if (validateSubscription() === false) {
    return
  } else {
    subForm.submit()
  }
})

const validateSubscription = () => {
  var input,
    i,
    valid = true
  input = subForm.getElementsByTagName('input')
  for (i = 0; i < input.length; i++) {
    if (input[i].value == '') {
      document.querySelector('.subscribe_message').style.display = 'flex'
      document.querySelector('.subscribe_message').innerHTML =
        'Email is required!'
      valid = false
    }
  }
  return valid // return the valid status
}


const searchBtn = document.getElementById("search-btn")
const searchForm = document.querySelector(".search-form_container")
searchBtn.addEventListener("click", () => {
  searchForm.classList.toggle("search-show")
})


searchForm.addEventListener('click', (e) => {
  const searchFormDim = searchForm.getBoundingClientRect()
  if (
      e.clientX < searchFormDim.left ||
      e.clientX > searchFormDim.right ||
      e.clientY < searchFormDim.top ||
      e.clientY > searchFormDim.bottom 
  ) {
      searchForm.classList.add("search-show2")
      console.log("yay")
  } else {
    
  }
})