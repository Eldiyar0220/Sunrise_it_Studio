$(function () {
    $('.burger').on('click', function () {
        $('.header__nav-wrap').slideToggle(150);
        $(this).toggleClass('active');
    })
})

$(function () {
    $('.header__sign.dropdown .sign__in').on('click', function (e) {
        e.preventDefault();
        $('.dropdown__wrap').toggleClass('active');
        $('.sign__in-item').toggleClass('active');
    });
    // $(document).on('click', function (e) {
    //     if ($(e.target).is('.dropdown, .dropdown__wrap') === false) {
    //         $('.dropdown__wrap').removeClass('active');
    //     }
    // });
});

$(function () {
    let lastScroll = 0;
    const defaultOffset = 200;
    const header = $('.header');

    const scrollPosition = () => window.pageYOffset || document.documentElement.scrollTop;
    const hasHide = () => header.hasClass('hide');

    window.addEventListener('scroll', () => {
        if (scrollPosition() > lastScroll && !hasHide()) {
            header.addClass('hide');
        } else if (scrollPosition() < lastScroll && hasHide()) {
            header.removeClass('hide');
        }

        lastScroll = scrollPosition();
    })
})

AOS.init({});

