const navBar = document.querySelector("nav")
const loginBtn = document.querySelectorAll(".login")
const regBtn = document.querySelectorAll(".registration")

loginBtn.forEach(menuBtn => {
  menuBtn.addEventListener("click", () => {
    navBar.classList.toggle("open");
  });
});

regBtn.forEach(menuBtn => {
  menuBtn.addEventListener("click", () =>{
    navBar.classList.toggle("open")
  })
})



