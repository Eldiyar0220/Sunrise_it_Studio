var acc = $('.accordion__title');
var accContent = ('.accordion__answer');

acc.on('click', function () {
    if ($(this).hasClass('active')) {
        acc.removeClass('active');
        $(this).siblings(accContent).slideUp(150);
    } else {
        acc.removeClass('active');
        acc.siblings(accContent).slideUp(150);
        $(this).addClass('active');
        $(this).siblings(accContent).slideDown(150);
    }
});


$('.sign__eye').on('click', function () {
    if ($(this).siblings('.sign__input').attr('type') === 'password') {
        $(this).siblings('.sign__input').attr('type', 'text');
        $(this).addClass('visible');
    }else {
        $(this).siblings('.sign__input').attr('type', 'password');
        $(this).removeClass('visible');
    }
})