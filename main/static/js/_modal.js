let modal = document.getElementsByClassName('hotels-modal')[0];
let cardNews = document.getElementById('OnMapBtn');
let closeModal = document.getElementsByClassName('hotels-modal__close')[0];


cardNews.onclick = () => {
    modal.style.display = "block";
}

closeModal.onclick = () => {
    modal.style.display = "none";
}

window.onclick = (event) => {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}