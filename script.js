document.addEventListener('DOMContentLoaded', () => {
  // --- Header Scroll Effect ---
  const header = document.querySelector('.site-header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 10) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  // --- Mobile Navigation ---
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const navLinks = document.getElementById('nav-links');
  let isMenuOpen = false;

  mobileMenuBtn?.addEventListener('click', () => {
    isMenuOpen = !isMenuOpen;
    mobileMenuBtn.setAttribute('aria-expanded', isMenuOpen);
    navLinks.classList.toggle('open');
    
    // Toggle icon (Hamburger vs Close)
    const icon = mobileMenuBtn.querySelector('svg');
    if (isMenuOpen) {
      icon.innerHTML = `<path d="M18 6 6 18"></path><path d="m6 6 12 12"></path>`;
    } else {
      icon.innerHTML = `<line x1="4" x2="20" y1="12" y2="12"></line><line x1="4" x2="20" y1="6" y2="6"></line><line x1="4" x2="20" y1="18" y2="18"></line>`;
    }
  });

  // Close mobile menu on click
  navLinks?.addEventListener('click', (e) => {
    if (e.target.tagName === 'A' && isMenuOpen) {
      isMenuOpen = false;
      mobileMenuBtn.setAttribute('aria-expanded', false);
      navLinks.classList.remove('open');
      const icon = mobileMenuBtn.querySelector('svg');
      icon.innerHTML = `<line x1="4" x2="20" y1="12" y2="12"></line><line x1="4" x2="20" y1="6" y2="6"></line><line x1="4" x2="20" y1="18" y2="18"></line>`;
    }
  });

  // --- Scroll Reveals ---
  const revealElements = document.querySelectorAll('.reveal');
  
  const revealOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px"
  };

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('active');
      observer.unobserve(entry.target);
    });
  }, revealOptions);

  revealElements.forEach(el => revealObserver.observe(el));

  // --- Counter Animation ---
  const counters = document.querySelectorAll('.counter');
  let animatedCounters = new Set();

  const counterObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const target = entry.target;
      if (animatedCounters.has(target)) return;
      
      animatedCounters.add(target);
      const targetValue = parseInt(target.getAttribute('data-target').replace(/,/g, ''), 10);
      const duration = 2000;
      const startTime = performance.now();
      
      function updateCounter(currentTime) {
        const elapsedTime = currentTime - startTime;
        const progress = Math.min(elapsedTime / duration, 1);
        // Easing out cubic
        const easeProgress = 1 - Math.pow(1 - progress, 3);
        
        const currentVal = Math.floor(easeProgress * targetValue);
        target.innerText = currentVal.toLocaleString() + (target.getAttribute('data-suffix') || '');
        
        if (progress < 1) {
          requestAnimationFrame(updateCounter);
        } else {
          target.innerText = targetValue.toLocaleString() + (target.getAttribute('data-suffix') || '');
        }
      }
      
      requestAnimationFrame(updateCounter);
    });
  }, { threshold: 0.5 });

  counters.forEach(counter => counterObserver.observe(counter));

  // --- Contact Form Validation ---
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const name = document.getElementById('name');
      const email = document.getElementById('email');
      const message = document.getElementById('message');
      
      let isValid = true;
      
      if (!name.value.trim()) {
        name.classList.add('invalid');
        isValid = false;
      } else {
        name.classList.remove('invalid');
      }
      
      if (!email.value.trim() || !/^\\S+@\\S+\\.\\S+$/.test(email.value)) {
        email.classList.add('invalid');
        isValid = false;
      } else {
        email.classList.remove('invalid');
      }
      
      if (!message.value.trim()) {
        message.classList.add('invalid');
        isValid = false;
      } else {
        message.classList.remove('invalid');
      }
      
      if (isValid) {
        // Show success
        const submitBtn = contactForm.querySelector('button[type="submit"]');
        submitBtn.style.display = 'none';
        
        const successMsg = document.getElementById('form-success');
        successMsg.style.display = 'flex';
        successMsg.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> Thank you! We'll be in touch shortly.`;
        
        contactForm.reset();
      }
    });
    
    // Clear validation on input
    const inputs = contactForm.querySelectorAll('.form-input');
    inputs.forEach(input => {
      input.addEventListener('input', () => {
        input.classList.remove('invalid');
      });
    });
  }
});
