function fetchCatImage(){
    let image = document.querySelector('.img')
    fetch("https://api.thecatapi.com/v1/images/search")
    .then(resp => resp.json())
    .then(json => image.src = json[0].url)
}

function btnClick(){
    let button = document.querySelector('.button')
    button.addEventListener('click', fetchCatImage)
}

document.addEventListener('DOMContentLoaded', () => {
    fetchCatImage()
    btnClick()
})