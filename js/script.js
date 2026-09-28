const BUSINESS = {
    name: "Team Seven System Solution",
    whatsapp: "919360039283",
    phone: "9360039283",
    prices: {
        portfolio: "₹2,999",
        static: "₹6,500",
        custom: "Get Custom Quote",
        hosting: "Get Custom Quote"
    }
};

document.addEventListener('DOMContentLoaded', () => {
    // Inject prices for website packages
    const priceElements = {
        'price-portfolio': BUSINESS.prices.portfolio,
        'price-static': BUSINESS.prices.static,
        'price-custom': BUSINESS.prices.custom,
        'price-hosting': BUSINESS.prices.hosting
    };

    for (const [id, price] of Object.entries(priceElements)) {
        const el = document.getElementById(id);
        if (el) el.textContent = price;
    }

    // Mobile menu toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            menuToggle.classList.toggle('active');
            
            // Toggle icon between bars and times
            const icon = menuToggle.querySelector('i');
            if (icon) {
                if (navLinks.classList.contains('active')) {
                    icon.classList.remove('fa-bars');
                    icon.classList.add('fa-times');
                } else {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            }
        });

        // Close menu when clicking a link
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                menuToggle.classList.remove('active');
                const icon = menuToggle.querySelector('i');
                if (icon) {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            });
        });
    }

    // Sticky header
    const header = document.getElementById('header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // Generic WhatsApp click handler for elements with data-wa-msg
    const waButtons = document.querySelectorAll('[data-wa-msg]');
    waButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const msg = btn.getAttribute('data-wa-msg');
            const url = `https://wa.me/${BUSINESS.whatsapp}?text=${encodeURIComponent(msg)}`;
            window.open(url, '_blank');
        });
    });

    // Call buttons handler
    const callButtons = document.querySelectorAll('[data-call]');
    callButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            window.location.href = `tel:+${BUSINESS.phone}`;
        });
    });

    // Quote Form Submit
    const quoteForm = document.getElementById('quote-form');
    if (quoteForm) {
        quoteForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('q-name').value;
            const mobile = document.getElementById('q-mobile').value;
            const service = document.getElementById('q-service').value;
            const req = document.getElementById('q-requirement').value;
            const budget = document.getElementById('q-budget').value;
            const loc = document.getElementById('q-location').value;
            const contact = document.getElementById('q-contact').value;

            const msg = `Hi ${BUSINESS.name},\n\nI would like to request a quotation.\n\n*Name:* ${name}\n*Mobile:* ${mobile}\n*Service:* ${service}\n*Requirement:* ${req}\n*Budget:* ${budget}\n*Location:* ${loc}\n*Preferred Contact:* ${contact}\n\nPlease provide me with a quotation.`;
            const url = `https://wa.me/${BUSINESS.whatsapp}?text=${encodeURIComponent(msg)}`;
            window.open(url, '_blank');
        });
    }

    // Job Form Submit
    const jobForm = document.getElementById('job-form');
    if (jobForm) {
        jobForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('j-name').value;
            const mobile = document.getElementById('j-mobile').value;
            const email = document.getElementById('j-email').value;
            const position = document.getElementById('j-position').value;
            const exp = document.getElementById('j-exp').value;
            const skills = document.getElementById('j-skills').value;
            const loc = document.getElementById('j-location').value;
            const intro = document.getElementById('j-intro').value;

            const msg = `Hi ${BUSINESS.name},\n\nI am submitting a job enquiry.\n\n*Name:* ${name}\n*Mobile:* ${mobile}\n*Email:* ${email}\n*Position:* ${position}\n*Experience:* ${exp}\n*Skills:* ${skills}\n*Location:* ${loc}\n*Introduction:* ${intro}\n\nPlease let me know about available opportunities.`;
            const url = `https://wa.me/${BUSINESS.whatsapp}?text=${encodeURIComponent(msg)}`;
            window.open(url, '_blank');
        });
    }

    // Add animation on scroll classes
    const animateElements = document.querySelectorAll('.card, .section-header');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    });

    animateElements.forEach(el => observer.observe(el));
});
