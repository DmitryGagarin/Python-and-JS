const addButton = document.querySelector('.add-button');
const deleteButton = document.querySelector('.delete-button')
const container = document.querySelector('.container')


addButton.addEventListener('click', () => {
  const checkbox = document.createElement('input')
  const checkLabel = document.createElement('label')
  const textbox = document.createElement('input')

  checkbox.type = 'checkbox'
  checkbox.classList.add('check-box')

  checkLabel.classList.add('check-label')

  textbox.type = 'text'
  textbox.classList.add('text-box')
  textbox.maxLength = '30'

  container.appendChild(checkbox)
  container.appendChild(textbox)
  container.appendChild(checkLabel)
})

deleteButton.addEventListener('click', () => {
    const checkboxes = document.querySelectorAll('.container input[type="checkbox"]');
    const textboxes = document.querySelectorAll('.container input[type="text"]');

    checkboxes.forEach(checkbox => {
      checkbox.remove();
    })

    textboxes.forEach(textbox => {
        textbox.remove();
    })
});
  
