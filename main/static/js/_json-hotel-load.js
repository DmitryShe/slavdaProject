/* добавим кнопке submit поисковой форме обработчик */ 
const appForm = document.getElementById('HotelsForm');
appForm.addEventListener('submit', handleFormSubmit);


async function handleFormSubmit(event) {
    event.preventDefault();
    
    const data = serializeForm(event.target);
    const response = await sendData(data);

    // получим данные, загрузим карту
    // console.log('responsw', response);

    const map = await ymaps.ready(init(response));
}

/* данные формы */
function serializeForm(formNode) {
    const { elements } = formNode;
    const data = new FormData();

    Array.from(elements)
        .filter((item) => !!item.name)
        .forEach((element) => {
            const { name, type } = element;
            const value = type === 'checkbox' ? element.checked : element.value;
            data.append(name, value);
        });
    //console.log(Array.from(data.entries()));
    return data;
}

/* получаем json от бэк энда */ 
async function sendData(data) {
    let arr = Array.from(data.entries());
    let url = `/hotels?${arr[0][0]}=${arr[0][1]}&${arr[1][0]}=${arr[1][1]} `;
    //console.log(url);

    let response = await fetch(url, {
        method: "get",
        headers: { "X-Requested-With": "XMLHttpRequest", }
    });

    function createColorTable(json) {
        let uniqCollection = new Set();
        let table = {};
        let colors = [
            'tags-orange', 'tags-blue', 'tags-pink', 'tags-red', 'tags-green', 'tags-brown', 'tags-coral'
        ];
        for (el in json) {
            uniqCollection.add(json[el]['placementType']);
        };
        let i = 0
        for (let el of uniqCollection) {
            if (colors[i]) {
                table[el] = colors[i];
                i += 1
            } else {
                table[el] = colors[0];
            }
            
        };

        return table;

    };

    if (response.ok) {
        var json = await response.json();
        
        document.querySelectorAll('div.hotels-card-elem').forEach(el => el.remove());
        
        let colorTable = createColorTable(json);

        for (key in json) {
            createCards(json[key], colorTable);

        };
        
        return json;
    } else {
        //console.log('error');
    };
}

/* создаем карточки отелей */
function createCards(data, colorTable) {
    let card = document.getElementsByClassName('hotels-cards-container')[0];
    //console.log('card: ', card);
    //console.log('remCard:', removeCard);
    let tagsArray = [];
    let temp = data['tags']
    let i = 0;
    for (key in temp) {
        if (i < 3) {
            tagsArray.push(temp[key]['title']);
            i += 1;
            // console.log(i);
        };
        //console.log('te', key, temp[key]['title']);
    };
    i = 0;
    let html = tagsArray.map((item) => `<li class="tags__elem">${item}</li>`).join('');
    //console.log('tagsarr', html);
    
    card.insertAdjacentHTML('afterbegin',
        `<div class="hotels-card-elem">
            <a class="opacity-1" href="${data['pageLink']}">
            <div class="hotels-card-elem__img_wrap">
                <img class="hotels-card-elem__img" src="${data['imageUrl']}" alt="" />
            </div>

            <div class="hotels-card-elem__type ${colorTable[data['placementType']]}">
                <p>${data['placementType']}</p>
            </div>

            <div class="hotels-card-elem__price">
                <p>Цена: ${data['price']}</p>
            </div>

            <div class="hotels-card-elem__header_wrap">
                <ul class="tags-text">${html}</ul>   
                <h4 class="hotels-card-elem__header">${data['title']}</h4>
            </div>

            <div class="tags">
                
                
            </div>
            </a>
        </div>`
    )
}


var hotelsMap;
function init(data) {
    if (hotelsMap) { hotelsMap.destroy(); hotelsMap = null; }
    //console.log('init', data);
    hotelsMap = new ymaps.Map('HotelsMap', {
        center: [56.02529833784815,92.86024757246774],
        zoom: 10
    }, {
        searchControlProvider: 'yandex#search'
    }),
    objectManager = new ymaps.ObjectManager({
        // Чтобы метки начали кластеризоваться, выставляем опцию.
        clusterize: true,
        // ObjectManager принимает те же опции, что и кластеризатор.
        gridSize: 32,
        clusterDisableClickZoom: true,
        
    });
    // Чтобы задать опции одиночным объектам и кластерам,
    // обратимся к дочерним коллекциям ObjectManager.
    objectManager.objects.options.set('preset', 'islands#greenDotIcon');
    objectManager.clusters.options.set('preset', 'islands#greenClusterIcons');
    hotelsMap.geoObjects.add(objectManager);

    let geoData = {
        "type": "FeatureCollection",
        "features": []
    };

    for (el in data) {
        //console.log('e', data[el]);
        geoData.features.push({ 
            'type': "Feature",
            'id': data[el].id,
            'geometry': {
                "type": "Point", 
                "coordinates": [
                    parseFloat(data[el].coordinates.x),
                    parseFloat(data[el].coordinates.y)
                ]
            },
            "properties": {
                "clusterCaption": `<strong> ${data[el].coordinates.title}</strong>`,
                "iconCaption": `${data[el].coordinates.title}`,
            }
            
        });
    }
    //console.log('geoData after', geoData);
    objectManager.add(geoData);

    
}