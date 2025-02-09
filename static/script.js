document.addEventListener('DOMContentLoaded', function() {
    // Video controls
    const video = document.getElementById('bg-video');
    video.playbackRate = 0.5;

    // Scroll animations
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(255,255,255,0.98)';
            navbar.style.boxShadow = '0 2px 10px rgba(0,0,0,0.2)';
        } else {
            navbar.style.background = 'rgba(255,255,255,0.95)';
            navbar.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
        }
    });
});


const slider = document.querySelector('.slider');
        const slides = document.querySelectorAll('.slide');
        const prevBtn = document.querySelector('.prev');
        const nextBtn = document.querySelector('.next');
        const dotsContainer = document.querySelector('.pagination-dots');
        
        let currentSlide = 0;
        const totalSlides = slides.length;

        // Create pagination dots
        slides.forEach((_, index) => {
            const dot = document.createElement('div');
            dot.classList.add('dot');
            if (index === 0) dot.classList.add('active');
            dot.addEventListener('click', () => goToSlide(index));
            dotsContainer.appendChild(dot);
        });

        // Update slides and dots
        function updateSlider() {
            slider.style.transform = `translateX(-${currentSlide * 100}%)`;
            document.querySelectorAll('.dot').forEach((dot, index) => {
                dot.classList.toggle('active', index === currentSlide);
            });
        }

        // Next slide
        function nextSlide() {
            currentSlide = (currentSlide + 1) % totalSlides;
            updateSlider();
        }

        // Previous slide
        function prevSlide() {
            currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
            updateSlider();
        }

        // Go to specific slide
        function goToSlide(index) {
            currentSlide = index;
            updateSlider();
        }

        // Event listeners
        nextBtn.addEventListener('click', nextSlide);
        prevBtn.addEventListener('click', prevSlide);

        // Auto-play
        let autoPlay = setInterval(nextSlide, 5000);

        // Pause on hover
        slider.parentElement.addEventListener('mouseenter', () => {
            clearInterval(autoPlay);
        });

        slider.parentElement.addEventListener('mouseleave', () => {
            autoPlay = setInterval(nextSlide, 5000);
        });


const swiper = new Swiper('.swiper-container', {
    slidesPerView: 3,
    spaceBetween: 20,
    loop: true,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    breakpoints: {
        320: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 2,
        },
        1024: {
            slidesPerView: 3,
        },
     
    }
});     

// fourth page

const slider2 = document.querySelector('.slider2');
        const prevBtn2 = document.querySelector('.prev-btn2');
        const nextBtn2 = document.querySelector('.next-btn2');
        const cards = document.querySelectorAll('.card');

        let cardWidth = cards[0].offsetWidth + 20; // Card width + gap

        // Navigation buttons
        nextBtn2.addEventListener('click', () => {
            slider2.scrollBy({
                left: cardWidth,
                behavior: 'smooth'
            });
        });

        prevBtn2.addEventListener('click', () => {
            slider2.scrollBy({
                left: -cardWidth,
                behavior: 'smooth'
            });
        });

        // Handle scroll events
        slider2.addEventListener('scroll', () => {
            const showPrev = slider2.scrollLeft > 0;
            const showNext = slider2.scrollLeft < (slider2.scrollWidth - slider2.clientWidth);
            
            prevBtn2.style.display = showPrev ? 'block' : 'none';
            nextBtn2.style.display = showNext ? 'block' : 'none';
        });

        // Initialize button visibility
        window.addEventListener('load', () => {
            prevBtn2.style.display = 'none';
            nextBtn2.style.display = slider2.scrollWidth > slider2.clientWidth ? 'block' : 'none';
        });

        // Handle window resize
        window.addEventListener('resize', () => {
            cardWidth = cards[0].offsetWidth + 20;
        });



        // for animaton text heading
const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, {
            threshold: 0.5
        });

        // Observe the animated heading
        const heading = document.querySelector('.animated-heading');
        observer.observe(heading);

        // Pause animation when hovering
        const scrollingText = document.querySelector('.scrolling-text');
        scrollingText.addEventListener('mouseenter', () => {
            scrollingText.style.animationPlayState = 'paused';
        });

        scrollingText.addEventListener('mouseleave', () => {
            scrollingText.style.animationPlayState = 'running';
        });        



        