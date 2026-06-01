const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('nav-links');
const navbar = document.getElementById('navbar');

if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        hamburger.classList.toggle('active');
    });

    navLinks.querySelectorAll('.nav-link').forEach((link) => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            hamburger.classList.remove('active');
        });
    });
}

window.addEventListener('scroll', () => {
    if (navbar) {
        navbar.classList.toggle('scrolled', window.scrollY > 40);
    }
});

const currentPath = window.location.pathname.replace(/\/$/, '') || '/';
document.querySelectorAll('.nav-link').forEach((link) => {
    const href = link.getAttribute('href').replace(/\/$/, '') || '/';
    if (href === currentPath) {
        link.classList.add('active');
    }
});

const revealEls = document.querySelectorAll('.scroll-reveal');
if (revealEls.length && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.12 }
    );
    revealEls.forEach((el) => observer.observe(el));
}
