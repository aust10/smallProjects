
const btn = document.getElementById('button')
const body = document.getElementById('body')
const input = document.getElementById('color')

btn.onclick = function() {
    const color = input.value
    makeButton(color)
}

function makeButton(color) {
    const button = document.createElement('button');
    button.innerText = color

    button.onclick = function() {
        body.style.backgroundColor = color
    }

    button.addEventListener('mouseover', function() {
        button.style.color = color
    })

    button.addEventListener('mouseleave', function() {
        button.style.color = "black"
    })

    body.appendChild(button)
}