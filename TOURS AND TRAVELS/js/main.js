$('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    dots:false,
    // autoplay:true,
    // autoplayTimeout: 3000,
    navText: ['<i class="fa-solid fa-arrow-left-long nav-arrow">', '<i class="fa-solid fa-arrow-right-long nav-arrow">'],
    responsive:{
        0:{
            items:1
        },
        600:{
            items:2
        },
        1000:{
            items:3
        }
    }
})

AOS.init();