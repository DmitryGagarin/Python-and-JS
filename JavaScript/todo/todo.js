const addButton = document.querySelector(".add-button")


addButton.addEventListener('click', () => {
    const newDiv = document.createElement('div');
    newDiv.textContent = 'This is a new div';
    container.appendChild(newDiv);
});