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
});


/** excursions swiper */
var excursionsSwiper = new Swiper(".excursions-swiper", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: "auto",
    coverflowEffect: {
        rotate: 50,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows: true,
    },
    pagination: {
      el: ".swiper-pagination",
    },
});