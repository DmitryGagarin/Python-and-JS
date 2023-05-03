const main = document.querySelector('.main') 
const form = document.querySelector('form')
const input = document.querySelector('input')
const button = document.querySelector('button')
const mainWrapper = document.createElement('div')

form.addEventListener('submit', async (e) => {
    e.preventDefault()
    const inputValue = Object.fromEntries(new FormData(e.target))
    const profileCard = await fetch(`https://api.github.com/users/${inputValue.name}`)
    const reposCard = await fetch(`https://api.github.com/users/${inputValue.name}/repos`)
    if (profileCard.ok && reposCard.ok) {
        const accountData = await profileCard.json()
        const repositoriesData = await reposCard.json()
        mainWrapper.appendChild(accountCard(accountData, repositoriesData))
        main.appendChild(mainWrapper)
        input.value = ''
    } else {
        alert("User doesn't exist")
    }
})

function accountCard(profileData, repositoriesData) {
    const element = document.createElement('div')
    element.classList.add('profile')
    element.innerHTML = `
      <img class="search-image" src=${profileData.avatar_url}></img>
      <p class="search-text"><span class="card-label"> NickName: </span>${profileData.login}</p>
      <p class="search-text"><span class="card-label"> Information: </span>${profileData.bio}</p>
      <p class="search-text"><span class="card-label"> Number of Repositories: </span>${profileData.public_repos}</p>
      <p class="search-text"><span class="card-label"> Time Creation: </span>${profileData.created_at}</p>
      <p class="search-text"><span class="card-label"> Last Activity: </span>${profileData.updated_at}</p>
      <p class="search-text"><span class="card-label"> Link to the profile: </span><a href="https://github.com/${profileData.login}/" target="_blank">${profileData.login}</a></p>
    `
    const reposWrapper = document.createElement('div')
    reposWrapper.classList.add('repos-wrapper')
    repositoriesData.forEach((repo) => {
      reposWrapper.appendChild(repoCard(repo))
    })
    element.appendChild(reposWrapper)
    element.appendChild(deleteButton())

    const activityWrapper = document.createElement('div')
    activityWrapper.classList.add('activity-wrapper')
    element.appendChild(activityWrapper)
    return element
}

function repoCard(repoData) {
    const element = document.createElement('div')
    element.classList.add('repo')
    element.innerHTML = `
      <p class="search-text"><span class="repository-name"> Repository Name: </span> ${repoData.name}</p>
      <p class="search-text"><span class="repository-link"> Link to the repository: </span> <a href="${repoData.html_url}" target="_blank">${repoData.html_url}</a></p>
    `
    return element;
}

function deleteButton() {
    let element = document.querySelector('.delete-button')
    element.addEventListener('click', (e) => {
        mainWrapper.innerHTML = ''
    })
    return element;
  }