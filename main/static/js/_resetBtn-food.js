/* скрипт для кнопки reset очищающей опции формы */
const btnReset = document.getElementById('BtnReset');
const PriceSelect = FoodsFilter.price;
const TypeSelect = FoodsFilter.type;
const KitchenSelect = FoodsFilter.kitchen;

btnReset.addEventListener('click', () => {
    PriceSelect.options[0].selected = true;
    TypeSelect.options[0].selected = true;
    KitchenSelect.options[0].selected = true
});