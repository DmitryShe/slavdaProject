let modal = document.getElementsByClassName('hotels-modal')[0];
let btnOpenMap = document.getElementById('OnMapBtn');
let closeModal = document.getElementsByClassName('hotels-modal__close')[0];
let modalContainer = document.getElementsByClassName('hotels-modal-container')[0];



btnOpenMap.onclick = () => {
    modal.style.display = "block";
}

closeModal.onclick = () => {
    modal.style.display = "none";
}

window.onclick = (event) => {
    if (event.target == modalContainer) {
        console.log('true')
        modal.style.display = "none";
    }
}

