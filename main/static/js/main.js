import { setTheme, changeModeBtnImg } from './_mode.js';
// import { getFetch } from './_res.js'


const currenTheme = localStorage.getItem('theme') || 'light';

changeModeBtnImg(currenTheme);
setTheme();

// getFetch();
/*async function getFetch() {
    // let address = document.location.href;
    console.log('async fun is run');
    let response = await fetch('/test', {
        method: 'get',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json'
        }
    });
    
    let data = await response.json();
    console.log(await data);
}

const fetchFunc = document.getElementById('test_btn');
fetchFunc.onclick = () => getFetch();*/