import { setTheme, changeModeBtnImg } from './_mode.js';


const currenTheme = localStorage.getItem('theme') || 'light';



let closeMenuBtn = document.getElementById('menuCloseBtn');
closeMenuBtn.onclick = () => {
    document.getElementsByClassName('mobile-menu__nav')[0].style.width = "0";
    
}

let openMenuBtn = document.getElementById('menuOpenBtn');
openMenuBtn.onclick = () => {
    document.getElementsByClassName('mobile-menu__nav')[0].style.width = "100%";
}


changeModeBtnImg(currenTheme);
setTheme();



