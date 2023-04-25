let modal = document.getElementById('temp');

let img = document.getElementById('tempImg');
let modalImg = document.getElementById("img01");
let captionText = document.getElementById("caption");

img.onclick = () => {
    modal.style.display = 'block';
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
};

let span = document.getElementsByClassName('close')[0];
span.onclick = () => {
    modal.style.display = "none";
};