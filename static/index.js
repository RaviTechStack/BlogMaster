let dots = document.querySelectorAll(".circle")
let slider = document.querySelector("#slider")

dots.forEach((ele, index)=>{
    ele.addEventListener("click", ()=>{
        slider.style.transform = `translateX(${index * -90}vw`
    })
})

let dots2 = document.querySelectorAll(".circles")
let slider2 = document.querySelector("#slider2")

dots2.forEach((ele, index)=>{
    ele.addEventListener("click", ()=>{
        slider2.style.transform = `translateX(${index * -70}vw`
    })
})

let menu = document.querySelector("#mobile-menu")
let menuBtn = document.querySelector("#menuBtn")
let crossBtn = document.querySelector("#crossBtn")


menuBtn.addEventListener("click", ()=>{
    menu.style.transform = `translateX(0vw)`
})

crossBtn.addEventListener("click", ()=>{
    menu.style.transform = `translateX(25vw)`
})