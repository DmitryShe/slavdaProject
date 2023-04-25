/**
 * setTheme() - устанавливаем тему сайта (темная или светлая),
 * передаем тему в changeModeBtnImg, которая меняет иконку
 * на кнопке по смене темы (луна или солнце)
 */
function changeModeBtnImg(theme) {
    let moon = 'moon.svg'; 
    let sun = 'sun.svg';
    let path = 'static/img/svg/';
    let elem = document.getElementById('imgMode');

    theme === 'light' ? (elem.src = elem.baseURI + path + moon) : (elem.src = elem.baseURI + path + sun);
}

function setTheme() {
    let modeBtn = document.getElementById('mode');
    let currenTheme = localStorage.getItem('theme') || 'light';

    modeBtn.addEventListener('click', () => {
        let theme = localStorage.getItem('theme');
        document.documentElement.setAttribute('data-theme', theme === 'light' ? 'dark' : 'light');
        localStorage.setItem('theme', theme === 'light' ? 'dark' : 'light');
        let themeFun = localStorage.getItem('theme');
        changeModeBtnImg(themeFun);
    });

    document.documentElement.setAttribute('data-theme', currenTheme);
}

export { setTheme, changeModeBtnImg };
