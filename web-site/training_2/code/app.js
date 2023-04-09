const navBar = document.querySelector("nav")
const openBtns1 = document.querySelectorAll(".login")
const openBtns2 = document.querySelectorAll(".registration")
const closeBtns = document.querySelector(".login-close")

openBtns1.forEach((menuBtn) => {
  menuBtn.addEventListener("click", () => {
    navBar.classList.toggle("open");
  });
});


