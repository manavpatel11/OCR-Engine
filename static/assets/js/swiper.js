
var swiper =  new Swiper(".product-category", {
    loop:true,
    slidesPerView: 1,
    spaceBetween: 30,
    navigation: {
        clickable: true,
        nextEl: ".button-product-category-next",
        prevEl: ".button-product-category-prev",
    },
    breakpoints: {
        767: {
            slidesPerView: 2,
            spaceBetween: 30,
        },
        992: {
            slidesPerView: 3,
            spaceBetween: 30,
        },
        1200: {
            slidesPerView: 4,
            spaceBetween: 30,
        },
    },
});

var swiper =  new Swiper(".author", {
    loop:false,
    slidesPerView: 1,
    spaceBetween: 30,
    navigation: {
        clickable: true,
        nextEl: ".button-author-next",
        prevEl: ".button-author-prev",
    },
    breakpoints: {
        767: {
            slidesPerView: 2,
            spaceBetween: 30,
        },
        992: {
            slidesPerView: 4,
            spaceBetween: 30,
        },
        1200: {
            slidesPerView: 6,
            spaceBetween: 30,
        },
    },
});

var swiper =  new Swiper(".product-category-1", {
    loop:false,
    slidesPerView: 1,
    spaceBetween: 30,
    navigation: {
        clickable: true,
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        767: {
            slidesPerView: 1,
            spaceBetween: 30,
        },
        992: {
            slidesPerView: 2,
            spaceBetween: 30,
        },
        1200: {
            slidesPerView: 4,
            spaceBetween: 30,
        },
    },
});

var swiper =  new Swiper(".product-category2", {
    loop:false,
    slidesPerView: 1,
    spaceBetween: 30,
    navigation: {
        clickable: true,
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        767: {
            slidesPerView: 1,
            spaceBetween: 30,
        },
        992: {
            slidesPerView: 2,
            spaceBetween: 30,
        },
        1200: {
            slidesPerView: 3,
            spaceBetween: 30,
        },
    },
});

var swiper =  new Swiper(".collection-over", {
    loop:true,
    autoplay: {
        waitForTransition: false,
        delay: 0,
    },
    slidesPerView: 1,
    spaceBetween: 30,
    speed: 5000,
    navigation: false,
    breakpoints: {
        767: {
            slidesPerView: 1,
            spaceBetween: 30,
        },
        992: {
            slidesPerView: 2,
            spaceBetween: 30,
        },
        1200: {
            slidesPerView: 3,
            spaceBetween: 30,
        },
    },
});


var swiper =  new Swiper(".slider-home", {
    loop:true,
    // autoplay: {
    //     waitForTransition: false,
    //     delay: 5000,
    // },
    slidesPerView: 1,
    spaceBetween: 30,

});

var swiper =  new Swiper(".slider-card-product", {
    loop:false,
    slidesPerView: 1,
    navigation: {
        clickable: true,
        nextEl: ".btn-card-product-next",
        prevEl: ".btn-card-product-prev",
    },
});


var swiperthump = new Swiper(".slider-thump", {
    loop: true,
    spaceBetween: 0,
    slidesPerView: 3,
    centeredSlides: true,
    freeMode: true,
    watchSlidesProgress: true,
    effect: "coverflow",
    grabCursor: true,
    coverflowEffect: {
        rotate: 0,
        stretch: 15,
        depth: 320,
        modifier: 1,
        slideShadows: false,
    },
  });
var swiper2 = new Swiper(".slider-home-3", {
    loop: true,
    autoplay: {
        delay: 5000,
    },
    slidesPerView: 1,
    spaceBetween:0,
    thumbs: {
        swiper: swiperthump,
    },
});

var swiper =  new Swiper(".live-auction", {
    loop:true,
    slidesPerView: 1,
    spaceBetween: 30,
    navigation: {
        clickable: true,
        nextEl: ".button-live-auction-next",
        prevEl: ".button-live-auction-prev",
    },
    pagination: {
        el: ".swiper-pagination-live-auction",
        clickable: true,
    },
    loop: true,
    breakpoints: {
        767: {
            slidesPerView: 2,
            spaceBetween: 30,
        },
        992: {
            slidesPerView: 2,
            spaceBetween: 30,
        },
        1200: {
            slidesPerView: 4,
            spaceBetween: 30,
        },
    },
});




var swiper1 = new Swiper(".mySwiper1", {
    direction: "vertical",
    spaceBetween: 15,
    grabCursor: true,
    loop: true,
    breakpoints: {
        0: {
            slidesPerView: 'auto'
        },
        991: {
            slidesPerView: 4
        },
    },
    shortSwipes: false,
    longSwipes: false,
    allowTouchMove: true,
    autoplay: {
    delay: 1, 
    }, 
    freeMode: true, 
    speed: 2000,
    disableOnInteraction: true
});
$(".mySwiper1").hover(function() {
    (this).swiper1.autoplay.stop();
}, function() {
    (this).swiper1.autoplay.start();
});
var swiper2 = new Swiper(".mySwiper2", {
    direction: "vertical",
    spaceBetween: 15,
    grabCursor: true,
    loop: true,
    breakpoints: {
        0: {
            slidesPerView: 'auto'
        },
        991: {
            slidesPerView: 4
        },
    },
    shortSwipes: false,
    longSwipes: false,
    allowTouchMove: true,
    autoplay: {
    delay: 1, 
    }, 
    freeMode: true, 
    speed: 2200,
    disableOnInteraction: true
});
$(".mySwiper2").hover(function() {
    (this).swiper2.autoplay.stop();
}, function() {
    (this).swiper2.autoplay.start();
});

var swiper_thump = new Swiper(".slideThumbMain", {
    loop: true,
    spaceBetween: 30,
    slidesPerView: 'auto',
    freeMode: true,
    watchSlidesProgress: true,
    breakpoints: {
        991: {
            slidesPerView: 'auto'
        },
        1100: {
            slidesPerView:  "auto"
        },
    },
    });
    var swiper2 = new Swiper(".slideThumb", {
    loop: true,
    spaceBetween: 15,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    thumbs: {
        swiper: swiper_thump,
    },
    });