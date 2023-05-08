/**
 * 
 */

var swiper = new Swiper(".index-grid__swiper", {
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
        delay: 7000,
        disableOnInteraction: false
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
        renderBullet: function (index, className) {
            return '<span class="' + className + '">' + (index + 1) + "</span>";
        },
    },
});

/** news swiper */
var newsSwiper = new Swiper(".index-news__swiper", {
    slidesPerView: 3,
    spaceBetween: 20,
    rewind: true,
    autoplay: {
        delay: 150000,
        disableOnInteraction: false
    },
    navigation: {
        nextEl: ".index-news__button-next",
        prevEl: ".index-news__button-prev",
    },
    breakpoints: {
        0: {
            slidesPerView: 1,
        },
        500: {
            slidesPerView: 2,
        },
        769: {
            slidesPerView: 3,
        }
    }
});

/** hotels swiper */
let hotelsSwiper = new Swiper(".index-hotels__swiper", {
    slidesPerView: 4,
    spaceBetween: 30,
    freeMode: true,
    rewind: true,
    navigation: {
        nextEl: ".index-hotels__button-next",
        prevEl: ".index-hotels__button-prev",
    }
});

let foodSwiper = new Swiper(".index-food__swiper", {
    slidesPerView: 5,
    spaceBetween: 30,
    freeMode: true,
    rewind: true,
    navigation: {
        nextEl: ".index-food__button-next",
        prevEl: ".index-food__button-prev",
    }
});

let lookSwiper = new Swiper(".index-look__swiper", {
    slidesPerView: 5,
    spaceBetween: 30,
    freeMode: true,
    rewind: true,
    navigation: {
        nextEl: ".index-look__button-next",
        prevEl: ".index-look__button-prev",
    }
});







