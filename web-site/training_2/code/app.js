$(function sideNav() {
  $('#Head a').on('click', function () {
    var link = $(this).data('nav');
    $('.' + link).toggleClass('Slide');
  });
  $('.AsideWrap').on('click', function () {
    $('.Slide').toggleClass('Slide');
  });
});

