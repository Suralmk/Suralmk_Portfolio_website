// sticky navbar
const navBar = document.querySelector('.navbar_container')
window.addEventListener('scroll', () => {
  navBar.classList.toggle('stick', this.window.scrollY > 0)
})

// search modal show
const searchBtn = document.getElementById('search-btn')
const searchDialog = document.querySelector('dialog')
searchBtn.addEventListener('click', () => {
  searchDialog.showModal()
})

// close search modal when outside its boundary is clicked
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


// nav menu

const mobileNavBtns = document.querySelector(".navbar-menus")
const NavBtn = document.querySelector(".nav-menu-btn")

NavBtn.addEventListener("click", () => {
  console.log("dd")
  mobileNavBtns.classList.toggle("active")
}) 