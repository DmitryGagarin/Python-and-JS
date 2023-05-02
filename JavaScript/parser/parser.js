const main = document.querySelector('.main');
const form = document.querySelector('form');
const input = document.querySelector('input');
const button = document.querySelector('button');
const wrapper = document.createElement('div')

form.addEventListener('submit', async (e) => {
    e.preventDefault()
    const inputValue = Object.fromEntries(new FormData(e.target))
    const request = await fetch(`https://api.github.com/users/${inputValue.name}`)
    if (request.ok){
        const data = await request.json()
        wrapper.appendChild(card(data))
        main.appendChild(wrapper)
        input.value = " "
    } else {
        alert("User doesn't exist")
    }
})

function card(profileData){
    const element = document.createElement('div')
    element.classList.add('profile')
    element.innerHTML = `
    <img class="search-image" src=${profileData.avatar_url}</img>
    <p class="search-text"><span> Name: </span> ${profileData.name}</p>
    <p class="search-text"><span> Town: </span> ${profileData.location}</p>
    <p class="search-text"><span> About: </span> ${profileData.bio}</p>`
    element.appendChild(deleteButton())
    return element  
}

function deleteButton(){
    const element = document.createElement('button')
    element.classList.add('delete-button')
    element.innerText = "Delete"
    element.addEventListener('click', (e) => {
        wrapper.innerHTML = ' '
    }) 
    return element
}