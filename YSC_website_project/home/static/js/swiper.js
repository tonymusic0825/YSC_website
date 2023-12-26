// Swiper
const swiper = new Swiper('.swiper', {
    loop: true,
    direction: 'horizontal',
    pagination: {
      el: '.swiper-pagination',
    },

    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
});

// Date for footer
const date = document.getElementById("date")
const currentYear = new Date().getFullYear()
date.textContent = currentYear