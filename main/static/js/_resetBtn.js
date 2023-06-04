/* скрипт для кнопки reset очищающей опции формы */
const btnReset = document.getElementById('BtnReset');
const PriceSelect = HotelsFilter.price;
const TypeSelect = HotelsFilter.type;

btnReset.addEventListener('click', () => {
    PriceSelect.options[0].selected = true;
    TypeSelect.options[0].selected = true;
});