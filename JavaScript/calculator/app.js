const inputLeft = document.querySelector('.left');
const inputRight = document.querySelector('.right');

const plus = document.getElementById('plus');
const minus = document.getElementById('minus');
const multiply = document.getElementById('multiply');
const divide = document.getElementById('divide');

const resultElement = document.querySelector('.result');

function showResult() {
  const valueLeft = Number(inputLeft.value);
  const valueRight = Number(inputRight.value);

  let result;

  if (plus.checked) {
    result = valueLeft + valueRight;
  } else if (minus.checked) {
    result = valueLeft - valueRight;
  } else if (multiply.checked) {
    result = valueLeft * valueRight;
  } else if (divide.checked) {
    result = valueLeft / valueRight;
  }

  if (result !== undefined) {
    resultElement.textContent = "Result: " + result;
  } else {
    resultElement.textContent = "No operation selected";
  }
}

plus.addEventListener('click', showResult);
minus.addEventListener('click', showResult);
multiply.addEventListener('click', showResult);
divide.addEventListener('click', showResult);