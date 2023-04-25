/**
 * 
 */

const progressCircle = document.querySelector(".autoplay-progress svg");
const progressContent = document.querySelector(".autoplay-progress span");

var swiper = new Swiper(".video-swiper", {
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
var newsSwiper = new Swiper(".news-swiper", {
    slidesPerView: 3,
    centeredSlides: true,
    spaceBetween: 30,
    autoplay: {
        delay: 150000,
        disableOnInteraction: false
    },
    /*pagination: {
      el: ".swiper-pagination",
      type: "fraction",
    },*/
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });


/** excursions swiper */
var newsSwiper = new Swiper(".excursions-swiper", {
    speed: 600,
    parallax: true,
    /*pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },*/
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
});