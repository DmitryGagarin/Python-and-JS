const navBar = document.querySelector("nav")
const openBtns = document.querySelectorAll(".login")


openBtns.forEach((menuBtn) => {
  menuBtn.addEventListener("click", () => {
    navBar.classList.toggle("open");
  });
});


