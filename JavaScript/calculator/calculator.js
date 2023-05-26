const input = document.getElementsByClassName("left-box-input")[0]; // getElementsByClassName return a collection
const output = document.getElementsByClassName('right-box-output')[0]

var dollar = document.querySelector("input[value='dollar-input']")
var euro = document.querySelector("input[value='euro-input']")
var yuan = document.querySelector("input[value='yuan-input']")


input.addEventListener('input', () => {
    const inputValue = input.value // 
    
    let currency = 2

    const regex = /^[0-9]*$/; // only allow numbers
    if (!regex.test(inputValue)) {
        inputValue.value = value.replace(/[^0-9]/g, ""); // remove non-numeric characters
    }

    if (dollar.checked){
        currency = 78.99
    }
    else if (euro.checked){
        currency = 84.73
    }
    else if (yuan.checked){
        currency = 11.18
    }

    output.value = inputValue * currency
})

