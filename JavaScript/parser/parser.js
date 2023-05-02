document.querySelector('button').onclick = myClick;

function myClick(){
    let a = document.querySelector('.input').value
    console.log(a)
    document.querySelector('.out').innerHTML += a
}
