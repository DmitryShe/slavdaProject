import { setTheme, changeModeBtnImg } from './_mode.js';
//import { swiper } from './_swiper-index.js';

// 
const currenTheme = localStorage.getItem('theme') || 'light';

changeModeBtnImg(currenTheme);
setTheme();

//
