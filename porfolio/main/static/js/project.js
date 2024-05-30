let sileIndex = 1;
showSlides(sileIndex)

function moveSlide(n) {
    sileIndex +=n
    showSlides(sileIndex)
}

function showSlides(n){
    let i;
    let slides = document.getElementsByClassName("carousel-item")
    if (n > slides.length) {
        sileIndex=1
    }
    if (n<1) {
        sileIndex= slides.length;
    }
    for (let i=0; i < slides.length; i++){
        slides[i].style.display="none"
    }
    slides[sileIndex -1].style.display="flex"
}