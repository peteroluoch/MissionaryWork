// Initialize Mission Carousel when the document is ready
document.addEventListener('DOMContentLoaded', function() {
    // Check if the mission carousel element exists
    const missionCarouselElement = document.querySelector('.mission-carousel');
    
    if (missionCarouselElement) {
        // Initialize Swiper
        const missionCarousel = new Swiper('.mission-carousel', {
            slidesPerView: 1,
            spaceBetween: 20,
            loop: true,
            autoplay: {
                delay: 5000,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
            breakpoints: {
                // When window width is >= 640px
                640: {
                    slidesPerView: 2,
                    spaceBetween: 20,
                },
                // When window width is >= 1024px
                1024: {
                    slidesPerView: 3,
                    spaceBetween: 30,
                },
            },
            effect: 'slide',
            speed: 800,
            grabCursor: true,
        });
        
        console.log('Mission carousel initialized successfully');
    } else {
        console.warn('Mission carousel element not found');
    }
});
