// Custom JavaScript for Pastor Prince Obasi-Ike Website

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize animations for elements with animation classes
    initAnimations();
    
    // Initialize mobile menu toggle
    initMobileMenu();
    
    // Initialize smooth scrolling for anchor links
    initSmoothScroll();
    
    // Initialize gallery filtering (if on media page)
    if (document.querySelector('.gallery-filter')) {
        initGalleryFilter();
    }
    
    // Initialize testimonial slider (if present)
    if (document.querySelector('.testimonial-slider')) {
        initTestimonialSlider();
    }
});

// Function to initialize animations
function initAnimations() {
    // Add animation classes to elements as they come into view
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    
    if (animatedElements.length > 0) {
        // Create an Intersection Observer
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animated');
                    // Unobserve after animation is triggered
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });
        
        // Observe each animated element
        animatedElements.forEach(element => {
            observer.observe(element);
        });
    }
}

// Function to initialize mobile menu
function initMobileMenu() {
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });
    }
}

// Function to initialize smooth scrolling for anchor links
function initSmoothScroll() {
    const anchorLinks = document.querySelectorAll('a[href^="#"]:not([href="#"])');
    
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 100,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Function to initialize gallery filtering
function initGalleryFilter() {
    const filterButtons = document.querySelectorAll('.gallery-filter button');
    const galleryItems = document.querySelectorAll('.gallery-item');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            filterButtons.forEach(btn => {
                btn.classList.remove('bg-blue-600', 'text-white');
                btn.classList.add('bg-gray-200', 'hover:bg-blue-600', 'hover:text-white');
            });
            
            // Add active class to clicked button
            this.classList.remove('bg-gray-200', 'hover:bg-blue-600', 'hover:text-white');
            this.classList.add('bg-blue-600', 'text-white');
            
            const filter = this.getAttribute('data-filter');
            
            // Show/hide gallery items based on filter
            galleryItems.forEach(item => {
                if (filter === 'all' || item.classList.contains(filter)) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });
}

// Function to initialize testimonial slider
function initTestimonialSlider() {
    const testimonials = document.querySelectorAll('.testimonial-slide');
    const prevButton = document.querySelector('.testimonial-prev');
    const nextButton = document.querySelector('.testimonial-next');
    let currentIndex = 0;
    
    // Function to show current testimonial
    function showTestimonial(index) {
        testimonials.forEach((testimonial, i) => {
            if (i === index) {
                testimonial.classList.remove('hidden');
                testimonial.classList.add('animate-fade-in');
            } else {
                testimonial.classList.add('hidden');
                testimonial.classList.remove('animate-fade-in');
            }
        });
    }
    
    // Initialize with first testimonial
    showTestimonial(currentIndex);
    
    // Add event listeners to navigation buttons
    if (prevButton && nextButton) {
        prevButton.addEventListener('click', function() {
            currentIndex = (currentIndex - 1 + testimonials.length) % testimonials.length;
            showTestimonial(currentIndex);
        });
        
        nextButton.addEventListener('click', function() {
            currentIndex = (currentIndex + 1) % testimonials.length;
            showTestimonial(currentIndex);
        });
    }
    
    // Auto-rotate testimonials every 5 seconds
    setInterval(function() {
        currentIndex = (currentIndex + 1) % testimonials.length;
        showTestimonial(currentIndex);
    }, 5000);
}

// Function to validate contact form
function validateContactForm() {
    const form = document.getElementById('contact-form');
    
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form fields
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const subject = document.getElementById('subject').value.trim();
            const message = document.getElementById('message').value.trim();
            
            // Simple validation
            if (name === '' || email === '' || subject === '' || message === '') {
                alert('Please fill in all fields');
                return;
            }
            
            // Email validation
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                alert('Please enter a valid email address');
                return;
            }
            
            // If validation passes, you would typically submit the form
            // For now, just show a success message
            alert('Thank you for your message! We will get back to you soon.');
            form.reset();
        });
    }
}

// Call form validation when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    validateContactForm();
});
