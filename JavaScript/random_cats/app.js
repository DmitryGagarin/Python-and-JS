function catButtonClick(){
    const buttonCat = document.querySelector('.button-cat')
    buttonCat.addEventListener('click', () => {
    const catImage = document.querySelector('.cat-img')
    fetch("https://api.thecatapi.com/v1/images/search")
    .then(resp => resp.json())
    .then(json => catImage.src = json[0].url)
    })
}

function dogButtonClick(){
    const buttonDog = document.querySelector('.button-dog')
    buttonDog.addEventListener('click', () => {
    const dogImage = document.querySelector('.dog-img')
    fetch("https://dog.ceo/api/breeds/image/random ")
    .then(resp => resp.json())
    .then(json => dogImage.src = json.message)
    })
}

document.addEventListener('DOMContentLoaded', () => {
    catButtonClick()
    dogButtonClick()
})