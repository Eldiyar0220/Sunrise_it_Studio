var introSwiper = new Swiper('.intro__swiper-container', {
    pagination: {
        el: '.intro__swiper-pagination',
        clickable: true,
    },
    loop: true,
    navigation: {
        nextEl: '.intro__swiper-next',
        prevEl: '.intro__swiper-prev',
    },
});

var ProcessSwiper = new Swiper('.process__swiper-container', {
    direction: 'vertical',
    pagination: {
        el: '.process__swiper-pagination',
        clickable: true,
    },
});

var EmployeeSwiper = new Swiper('.employee__swiper-container', {
    pagination: {
        el: '.employee__swiper-pagination',
        clickable: true,
    },
    slidesPerView: 5,
    spaceBetween: 24,
    loop: true,
    navigation: {
        nextEl: '.employee__swiper-next',
        prevEl: '.employee__swiper-prev',
    },

    breakpoints: {
        320: {
            slidesPerView: 1,
        },
        425: {
            slidesPerView: 2,
        },
        768: {
            slidesPerView: 3,
        },
        1024: {
            slidesPerView: 4,
        },
        1200: {
            slidesPerView: 5,
        }
    }
});

var countries = ['Китай', 'Турция']
var deliverySwiper = new Swiper('.delivery__swiper-container', {
    pagination: {
        el: '.delivery__pagination',
        clickable: true,
        renderBullet: function (index, className) {
            return '<span class="' + className + '">' + (countries[index]) + '</span>';
        },
    },
    loop: true,
    spaceBetween: 24,
    navigation: {
        nextEl: '.delivery__swiper-next',
        prevEl: '.delivery__swiper-prev',
    },
});


