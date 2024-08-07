let slideIndex = 1; // Only show the image of the index that we're currently on
showSlides(slideIndex) //Code explained around 1:17:10 mark

function moveSlide(n) {
    slideIndex += n
    showSlides(slideIndex)
}

function showSlides(n) {
    let slides = document.getElementsByClassName("carousel-item")
    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length;
    }

    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"
    }
    slides[slideIndex = 1].style.display = "flex"
}