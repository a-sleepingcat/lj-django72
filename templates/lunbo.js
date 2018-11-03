$(function () {
    var swiper = new Swiper('.swiper-container', {
        pagination: '.swiper-pagination',
        // nextButton: '.swiper-button-next',
        // prevButton: '.swiper-button-prev',
        paginationClickable: true,
        spaceBetween: 30,
        centeredSlides: true,
        autoplay: 2500,
        autoplayDisableOnInteraction: false
        loop: ture
    });

})
// <div class="swiper-container" id="topSwiper">
//             <div class="swiper-wrapper">
//                 {% for wheel in wheels %}
//                     <div class="swiper-slide">
//                         <img src="{{ wheel.img }}" alt="">
//                     </div>
//                 {% endfor %}
//             </div>
//             <div class="swiper-pagination"></div>
//         </div>