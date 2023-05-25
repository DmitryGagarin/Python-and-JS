const addButton = document.querySelector('.add-button');

addButton.addEventListener('click', () => {
  const checkbox = document.createElement('input')
  const checkLabel = document.createElement('label')
  const textbox = document.createElement('input')

  checkbox.type = 'checkbox'
  checkbox.classList.add('check-box')

  checkLabel.classList.add('check-label')

  textbox.type = 'text'
  textbox.classList.add('text-box')


  const container = document.querySelector('.container')

  container.appendChild(checkbox)
  container.appendChild(textbox)
  container.appendChild(checkLabel)
})
