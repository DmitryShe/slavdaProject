let map;

ymaps.ready(init);

function init() {
    map = new ymaps.Map('map', {
        center: [55.65, 37.22],
        zoom: 10
    }, {
        searchControlProvider: 'yandex#search'
    });

    
}
