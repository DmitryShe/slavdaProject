/* скрипт для кнопки reset очищающей опции формы */
const btnReset = document.getElementById('BtnReset');
const DurationSelect = ExcursionsForm.hours;
const PriceStartSelect = ExcursionsForm.price_start;
const PriceEndSelect = ExcursionsForm.price_end;


btnReset.addEventListener('click', () => {
    DurationSelect[0].checked = true;
    PriceStartSelect.value = ''
    PriceEndSelect.value = ''
});