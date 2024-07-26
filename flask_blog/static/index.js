// ************* Trending Post Slider ************* 

let dots = document.querySelectorAll(".circle")
let sno = 1
let slider = document.querySelector("#slider")

dots.forEach((ele, index)=>{
    ele.addEventListener("click", ()=>{
        sno = index
        slider.style.transform = `translateX(${sno * -90}vw`
    })
})

const slide =()=>{
    if(sno==4){
        sno=0
    }
    slider.style.transform = `translateX(${sno * -90}vw`
    sno++; 
}

setInterval(slide, 3000)


// ************* Random Post Slider ************* 

let sno2 = 1
let dots2 = document.querySelectorAll(".circles")
let slider2 = document.querySelector("#slider2")

dots2.forEach((ele, index)=>{
    ele.addEventListener("click", ()=>{
        index = sno2
        slider2.style.transform = `translateX(${sno2 * -70}vw`
    })
})
const slide2 =()=>{
    if(sno2==3){
        sno2=0
    }
    slider2.style.transform = `translateX(${sno2 * -70}vw`
    sno2++; 
}

setInterval(slide2, 3000)

// ************* Hamburger Menu started ************* 

let menu = document.querySelector("#mobile-menu")
let menuBtn = document.querySelector("#menuBtn")
let crossBtn = document.querySelector("#crossBtn")


menuBtn.addEventListener("click", ()=>{
    menu.style.transform = `translateX(0vw)`
})

crossBtn.addEventListener("click", ()=>{
    menu.style.transform = `translateX(25vw)`
})