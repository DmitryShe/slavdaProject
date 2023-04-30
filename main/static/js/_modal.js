let modal = document.getElementById('index-modal');
let cardNews = document.getElementsByClassName('index-news__swiper-slide');
let closeModal = document.getElementsByClassName('index-modal__close')[0];


for (let i = 0; i < cardNews.length; i++) {
    cardNews[i].onclick = () => {
        modal.style.display = "block";
    }
}

closeModal.onclick = () => {
    modal.style.display = "none";
}

window.onclick = (event) => {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}