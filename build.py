import os

header_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Our Shoulders Foundation</title>
  <link href="https://api.fontshare.com/v2/css?f[]=satoshi@300,400,500,700&display=swap" rel="stylesheet">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body>
  <a href="#main-content" class="visually-hidden">Skip to main content</a>
  <header class="site-header">
    <div class="container nav-container">
      <a href="index.html" class="logo-container" aria-label="Our Shoulders Foundation Home">
        <img src="Our Shoulders Logo.png" alt="Our Shoulders Foundation Logo">
      </a>
      <nav aria-label="Main Navigation">
        <div class="nav-links" id="nav-links">
          <a href="about.html" class="nav-link">About</a>
          <a href="index.html#what-we-do" class="nav-link">What We Do</a>
          <a href="volunteer.html" class="nav-link">Volunteer</a>
          <a href="donate.html" class="nav-link">Donate</a>
          <a href="contact.html" class="nav-link">Contact</a>
        </div>
      </nav>
      <div style="display: flex; align-items: center; gap: var(--space-4);">
        <button class="mobile-menu-btn" id="mobile-menu-btn" aria-expanded="false" aria-label="Menu">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="4" x2="20" y1="12" y2="12"></line><line x1="4" x2="20" y1="6" y2="6"></line><line x1="4" x2="20" y1="18" y2="18"></line>
          </svg>
        </button>
      </div>
    </div>
  </header>
  <main id="main-content">
"""

footer_html = """
  </main>
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" class="logo-container footer-logo">
            <img src="Our Shoulders Logo.png" alt="Our Shoulders Foundation Logo">
          </a>
          <p style="color: rgba(255,255,255,0.7); margin-top: var(--space-2);">Shouldering Responsibilities</p>
          <div style="display: flex; gap: var(--space-4); margin-top: var(--space-4);">
            <a href="#" aria-label="Facebook"><i data-lucide="facebook" style="color: white; width: 20px;"></i></a>
            <a href="#" aria-label="Twitter"><i data-lucide="twitter" style="color: white; width: 20px;"></i></a>
            <a href="#" aria-label="Instagram"><i data-lucide="instagram" style="color: white; width: 20px;"></i></a>
            <a href="#" aria-label="LinkedIn"><i data-lucide="linkedin" style="color: white; width: 20px;"></i></a>
          </div>
        </div>
        <div>
          <h4 class="footer-heading">Quick Links</h4>
          <ul class="footer-links">
            <li><a href="about.html" class="footer-link">About</a></li>
            <li><a href="index.html#what-we-do" class="footer-link">What We Do</a></li>
            <li><a href="volunteer.html" class="footer-link">Volunteering</a></li>
            <li><a href="donate.html" class="footer-link">Donate</a></li>
            <li><a href="contact.html" class="footer-link">Contact</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-heading">Programs</h4>
          <ul class="footer-links">
            <li><a href="technical-training.html" class="footer-link">Technical Training</a></li>
            <li><a href="vocational.html" class="footer-link">Vocational Training</a></li>
            <li><a href="community.html" class="footer-link">Community Development</a></li>
            <li><a href="health-sanitation.html" class="footer-link">Health & Sanitation</a></li>
            <li><a href="environment.html" class="footer-link">Environment</a></li>
            <li><a href="farmers.html" class="footer-link">Farmers</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-heading">Contact & Legal</h4>
          <ul class="footer-links" style="color: rgba(255,255,255,0.7); font-size: var(--text-sm);">
            <li style="margin-bottom: var(--space-2);"><i data-lucide="map-pin" style="width: 16px; height: 16px; display: inline; margin-right: 4px; vertical-align:-3px;"></i> 13, 8th Street, Samayapuram, Karambakkam-Porur, Chennai &ndash; 600 116</li>
            <li style="margin-bottom: var(--space-2);"><i data-lucide="phone" style="width: 16px; height: 16px; display: inline; margin-right: 4px; vertical-align:-3px;"></i> +91 7373118000 &middot; +91 9444334487</li>
            <li style="margin-bottom: var(--space-2);"><i data-lucide="mail" style="width: 16px; height: 16px; display: inline; margin-right: 4px; vertical-align:-3px;"></i> ourshoulder@gmail.com</li>
            <li style="margin-top: var(--space-4);">Reg. No. 1/2016/BK4</li>
            <li>Sec. 12A &middot; CSR-1 &middot; Sec. 80G</li>
          </ul>
        </div>
      </div>
      <div class="footer-legal">
        <p>&copy; 2025 Our Shoulders Foundation. All Rights Reserved.</p>
      </div>
    </div>
  </footer>
  <script src="script.js"></script>
  <script>lucide.createIcons();</script>
</body>
</html>
"""

pages = [
  {
    "name": "about.html",
    "title": "About Us",
    "content": """
      <section class="page-hero reveal">
        <div class="container hero-content">
          <h1>About Us</h1>
          <p>Our strength lies in the actions of our initiatives. Learn about our vision, mission, and the philosophy that guides us.</p>
        </div>
      </section>

      <section class="section reveal">
        <div class="container grid-2" style="align-items: center;">
          <div>
            <span class="section-label">Who We Are</span>
            <h2>Our Story</h2>
            <p>Our strength lies not only in the words we stand by, but most importantly in the actions of our initiatives. From the moment we started our work in 2016, we have been committed to empowering underserved communities.</p>
          </div>
          <div>
            <img src="https://images.unsplash.com/photo-1593113630400-ea4288922497?auto=format&fit=crop&q=80&w=800" alt="Who We Are" style="border-radius: 10px;">
          </div>
        </div>
      </section>

      <section class="section section-alt reveal">
        <div class="container grid-2">
          <div class="card">
            <h3 style="color: var(--color-primary);"><i data-lucide="eye" style="display:inline; width:24px; margin-right:8px; vertical-align:-4px;"></i>OUR VISION</h3>
            <p style="font-family: var(--font-body); font-size: var(--text-lg); font-style: italic;">"To create a world where <strong>Community Empowerment</strong>, <strong>Environmental Sustainability</strong>, and <strong>ESG-Driven Development</strong> lead to lasting change."</p>
          </div>
          <div class="card delay-100">
            <h3 style="color: var(--color-primary);"><i data-lucide="target" style="display:inline; width:24px; margin-right:8px; vertical-align:-4px;"></i>OUR MISSION</h3>
            <p style="font-family: var(--font-body); font-size: var(--text-lg); font-style: italic;">"To champion <strong>ESG-Driven Development</strong> through strategic initiatives, unwavering dedication, and grassroots empowerment."</p>
          </div>
        </div>
      </section>

      <section class="section reveal">
        <div class="container text-center">
          <span class="section-label text-center mb-12" style="display: block;">Core Philosophy</span>
          <div class="grid-5 mt-8">
            <div class="concept-card"><div class="concept-icon"><i data-lucide="hammer"></i></div><div class="concept-word">CREATE</div><p class="concept-desc">Building meaningful opportunities from the ground up to ensure long-term sustainability.</p></div>
            <div class="concept-card delay-100"><div class="concept-icon"><i data-lucide="heart"></i></div><div class="concept-word">CONTRIBUTE</div><p class="concept-desc">Giving back our time, resources, and knowledge to build a stronger society.</p></div>
            <div class="concept-card delay-200"><div class="concept-icon"><i data-lucide="sliders"></i></div><div class="concept-word">CALIBRATE</div><p class="concept-desc">Continuously improving our methods for maximum impact and reach.</p></div>
            <div class="concept-card delay-300"><div class="concept-icon"><i data-lucide="link"></i></div><div class="concept-word">CONNECT</div><p class="concept-desc">Bridging the gap between resources and those in need.</p></div>
            <div class="concept-card delay-100"><div class="concept-icon"><i data-lucide="check-circle"></i></div><div class="concept-word">CORRECT</div><p class="concept-desc">Addressing structural inequalities through dedicated, actionable reform.</p></div>
          </div>
        </div>
      </section>

      <section class="section section-offset reveal">
        <div class="container text-center">
          <span class="section-label">Our Approach</span>
          <h2 class="mb-12">How We Work</h2>
          <div class="grid-3">
            <div>
              <div class="card-icon" style="margin: 0 auto var(--space-4);"><i data-lucide="users"></i></div>
              <h3>Community Outreach</h3>
              <p>Helping Those Who Need Us Most with targeted efforts, bringing resources directly to the grassroots level.</p>
            </div>
            <div>
              <div class="card-icon" style="margin: 0 auto var(--space-4);"><i data-lucide="heart-handshake"></i></div>
              <h3>Volunteering</h3>
              <p>The Future Looks Bright when we work together. We mobilize passionate individuals to drive meaningful change.</p>
            </div>
            <div>
              <div class="card-icon" style="margin: 0 auto var(--space-4);"><i data-lucide="building"></i></div>
              <h3>Local Empowerment</h3>
              <p>Change for the Better starting at the grassroots level, ensuring communities become self-sufficient and resilient.</p>
            </div>
          </div>
        </div>
      </section>

      <section class="section reveal">
        <div class="container">
          <span class="section-label text-center">Get Involved</span>
          <h2 class="text-center mb-12">Volunteer Onboarding Steps</h2>
          <div class="timeline">
            <div class="timeline-step">
              <div class="timeline-number">1</div>
              <h4>Register</h4>
            </div>
            <div class="timeline-step">
              <div class="timeline-number">2</div>
              <h4>Select Your Mode</h4>
            </div>
            <div class="timeline-step">
              <div class="timeline-number">3</div>
              <h4>Choose Your Topic</h4>
            </div>
            <div class="timeline-step">
              <div class="timeline-number">4</div>
              <h4>Make an Impact</h4>
            </div>
          </div>
        </div>
      </section>
    """
  },
  {
    "name": "technical-training.html",
    "title": "Technical Skill Training",
    "content": """
      <section class="page-hero reveal">
        <div class="container hero-content">
          <h1>Technical Skill Training</h1>
          <p>Empowering Futures with Grow with Google</p>
        </div>
      </section>

      <section class="section reveal">
        <div class="container" style="max-width: 1000px; margin: 0 auto;">
          <h2 class="mb-6">Empowering Futures with "Grow with Google"</h2>
          
          <p>In collaboration with Coursera, NASSCOM Foundation, and a consortium of 16 esteemed colleges in Tamil Nadu, our <strong>"Grow with Google"</strong> project is making waves in the realm of technical training. Our primary goal? To provide self-learning online courses to students from economically weaker backgrounds, where family incomes fall below 5 lakhs.</p>
          
          <div class="grid-2 mt-8 mb-12" style="max-width: 800px; margin-left: auto; margin-right: auto;">
            <div class="card text-center" style="border: 1px solid var(--color-primary); padding: var(--space-6); box-shadow: 0 4px 20px rgba(232, 119, 34, 0.08);">
              <div class="card-icon mx-auto" style="margin-bottom: var(--space-3); color: var(--color-primary);"><i data-lucide="users" style="width: 32px; height: 32px;"></i></div>
              <div class="stat-number counter" data-target="5000" style="font-size: var(--text-2xl); font-weight: 700; color: var(--color-primary); margin-bottom: var(--space-1);">0</div>
              <h3 style="font-size: var(--text-lg); margin-bottom: var(--space-1);">Students Enrolled</h3>
              <p style="font-size: var(--text-sm); margin: 0;">A resounding enrollment making it a beacon of opportunity.</p>
            </div>
            <div class="card text-center delay-100" style="border: 1px solid var(--color-primary); padding: var(--space-6); box-shadow: 0 4px 20px rgba(232, 119, 34, 0.08);">
              <div class="card-icon mx-auto" style="margin-bottom: var(--space-3); color: var(--color-primary);"><i data-lucide="award" style="width: 32px; height: 32px;"></i></div>
              <div class="stat-number counter" data-target="3755" style="font-size: var(--text-2xl); font-weight: 700; color: var(--color-primary); margin-bottom: var(--space-1);">0</div>
              <h3 style="font-size: var(--text-lg); margin-bottom: var(--space-1);">Successful Completions</h3>
              <p style="font-size: var(--text-sm); margin: 0;">Emerged victorious, successfully completing their chosen courses.</p>
            </div>
          </div>
          
          <p class="mb-8">The <strong>"Grow with Google"</strong> curriculum offers a range of courses tailored to meet the demands of a dynamic job market:</p>
          
          <div class="grid-3 mb-8">
            <div class="card text-center" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: var(--space-6);">
              <div class="card-icon" style="margin-bottom: var(--space-4);"><i data-lucide="megaphone" style="width: 32px; height: 32px;"></i></div>
              <h4 style="margin: 0;">Google Digital Marketing</h4>
            </div>
            <div class="card text-center delay-100" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: var(--space-6);">
              <div class="card-icon" style="margin-bottom: var(--space-4);"><i data-lucide="bar-chart-2" style="width: 32px; height: 32px;"></i></div>
              <h4 style="margin: 0;">Google Data Analytics</h4>
            </div>
            <div class="card text-center delay-200" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: var(--space-6);">
              <div class="card-icon" style="margin-bottom: var(--space-4);"><i data-lucide="server" style="width: 32px; height: 32px;"></i></div>
              <h4 style="margin: 0;">Google IT Support</h4>
            </div>
            <div class="card text-center" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: var(--space-6);">
              <div class="card-icon" style="margin-bottom: var(--space-4);"><i data-lucide="cpu" style="width: 32px; height: 32px;"></i></div>
              <h4 style="margin: 0;">Google IT Automation</h4>
            </div>
            <div class="card text-center delay-100" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: var(--space-6);">
              <div class="card-icon" style="margin-bottom: var(--space-4);"><i data-lucide="kanban" style="width: 32px; height: 32px;"></i></div>
              <h4 style="margin: 0;">Google Project Management</h4>
            </div>
            <div class="card text-center delay-200" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: var(--space-6);">
              <div class="card-icon" style="margin-bottom: var(--space-4);"><i data-lucide="pen-tool" style="width: 32px; height: 32px;"></i></div>
              <h4 style="margin: 0;">Google UX Design</h4>
            </div>
          </div>

          <p>At the intersection of technology and empowerment, <strong>"Grow with Google"</strong> is not just a project; it's a promise of brighter, more prosperous futures.</p>
          
          <p style="color: var(--color-primary); font-weight: 500;">We also provided them with soft skill sessions (Communication skills, Critical thinking, teamwork, Professional Development and Organizational behaviour workshop, Interview preparation &amp; Resume building)</p>
        </div>
      </section>

      <section class="section reveal">
        <div class="container">
          <span class="section-label text-center">At-Risk Youth</span>
          <h2 class="text-center mb-8">Vocational Training Programs</h2>
          <div class="grid-2">
            <div class="card">
              <span class="location-chip"><i data-lucide="map-pin"></i> Kelly's, Purasaiwalkam</span>
              <h3>Observation Home Boys</h3>
              <p>Specialized skill training programs aimed at rehabilitation and offering a second chance through structured education.</p>
              <p style="font-weight: 600; color: var(--color-primary); margin-top: auto;">Ongoing Support & Mentorship</p>
            </div>
            <div class="card delay-100">
              <span class="location-chip"><i data-lucide="map-pin"></i> Chengalpattu</span>
              <h3>Children Special Home</h3>
              <p>Equipping young minds with technical aptitude to secure a brighter, independent future outside the system.</p>
              <p style="font-weight: 600; color: var(--color-primary); margin-top: auto;">100+ Beneficiaries</p>
            </div>
          </div>
        </div>
      </section>

      <section class="section section-offset reveal">
        <div class="container">
          <span class="section-label text-center">Other Training</span>
          <h2 class="text-center mb-8">Additional Technical Programs</h2>
          <div class="grid-3 text-center">
            <div class="card" style="border:none; background:transparent;">
              <div class="card-icon mx-auto" style="margin: 0 auto var(--space-4);"><i data-lucide="coffee"></i></div>
              <h3>Basic Industrial Hospitality</h3>
            </div>
            <div class="card delay-100" style="border:none; background:transparent;">
              <div class="card-icon mx-auto" style="margin: 0 auto var(--space-4);"><i data-lucide="droplet"></i></div>
              <h3>RO Water Installation</h3>
            </div>
            <div class="card delay-200" style="border:none; background:transparent;">
              <div class="card-icon mx-auto" style="margin: 0 auto var(--space-4);"><i data-lucide="zap"></i></div>
              <h3>Electrical & Plumbing</h3>
            </div>
          </div>
        </div>
      </section>
    """
  },
  {
    "name": "health-sanitation.html",
    "title": "Health & Sanitation",
    "content": """
      <section class="page-hero reveal">
        <div class="container hero-content">
          <h1>Health & Sanitation</h1>
          <p>Promoting well-being and basic hygiene across communities.</p>
        </div>
      </section>

      <section class="section reveal">
        <div class="container grid-2" style="align-items: center;">
          <div>
            <div class="card">
              <span class="section-label">Emergency Relief</span>
              <h3>COVID-19 Community Intervention</h3>
              <p>A resilient 6-month operation directly supporting vulnerable populations during the pandemic peak.</p>
              <div style="display: flex; flex-wrap: wrap; gap: var(--space-4); margin-top: var(--space-4);">
                <div class="chip" style="background:var(--color-bg); border: 1px solid var(--color-border);">1,500+ Members Reached</div>
                <div class="chip" style="background:var(--color-bg); border: 1px solid var(--color-border);">6 Months Active</div>
              </div>
            </div>
          </div>
          <div>
            <span class="section-label">Partners</span>
            <h3 class="mb-4">In Collaboration With</h3>
            <ul style="list-style: none;">
              <li style="margin-bottom: var(--space-4); display: flex; align-items: center; gap: var(--space-2);"><i data-lucide="check-circle" style="color: var(--color-primary);"></i> <span style="font-weight: 500;">Greater Chennai Corporation</span></li>
              <li style="display: flex; align-items: center; gap: var(--space-2);"><i data-lucide="check-circle" style="color: var(--color-primary);"></i> <span style="font-weight: 500;">Tamil Nadu Urban Habitat Development Board</span></li>
            </ul>
          </div>
        </div>
      </section>

      <section class="section section-alt reveal">
        <div class="container">
          <span class="section-label text-center">Hygiene</span>
          <h2 class="text-center mb-8">WASH Project Initiatives</h2>
          <div class="grid-3">
            <div class="card">
              <span class="location-chip"><i data-lucide="map-pin"></i> Ezhil Nagar</span>
              <h3>Community WASH</h3>
              <p>Water, Sanitation, and Hygiene awareness drives for over 500 local families.</p>
            </div>
            <div class="card delay-100">
              <span class="location-chip"><i data-lucide="map-pin"></i> Okkiyam Thuraipakkam</span>
              <h3>School Programs</h3>
              <p>Direct intervention teaching essential hygiene practices to the younger generation.</p>
            </div>
            <div class="card delay-200">
              <span class="location-chip"><i data-lucide="map-pin"></i> Perumbakkam</span>
              <h3>Child Handwashing</h3>
              <p>150 children trained in proper handwashing techniques to prevent communicable diseases.</p>
            </div>
          </div>
        </div>
      </section>

      <section class="section reveal">
        <div class="container grid-2">
          <div class="card">
            <div class="card-icon"><i data-lucide="shield-alert"></i></div>
            <h3>De-Addiction Awareness</h3>
            <p>Community outreach programs aimed at substance abuse prevention and rehabilitation pathways.</p>
            <div class="chip mt-4" style="background: transparent; border: 1px solid var(--color-border);">NAPDDR Department Collaboration</div>
          </div>
          
          <div class="card">
            <div class="card-icon"><i data-lucide="ambulance"></i></div>
            <h3>FRIENDS of 108 — Thozhamai 108</h3>
            <p>A flagship emergency response support initiative ensuring faster community mobilization for 108 ambulance services.</p>
            <p style="font-size: var(--text-sm); margin-top: var(--space-4);">Inaugurated at <strong>Patrician College</strong></p>
          </div>
        </div>
      </section>
    """
  },
  {
    "name": "community.html",
    "title": "Community Development",
    "content": """
      <section class="page-hero reveal">
        <div class="container hero-content">
          <h1>Community Development</h1>
          <p>Empowering Communities: Impactful Initiatives in Action</p>
        </div>
      </section>

      <section class="section reveal">
        <div class="container">
          <span class="section-label text-center">Local Projects</span>
          <h2 class="text-center mb-8">Key Initiatives</h2>
          <div class="grid-3">
            <div class="card">
              <span class="location-chip"><i data-lucide="map-pin"></i> Besant Nagar &rarr; Thiruvanmiyur</span>
              <h3>Bike Rally for Eye Donation</h3>
              <p>A mass mobilization event raising critical awareness for eye pledges across Chennai.</p>
            </div>
            
            <div class="card delay-100">
              <span class="location-chip"><i data-lucide="map-pin"></i> Athipattu Urban Slums</span>
              <h3>Social Cause Wall Paintings</h3>
              <p>Transforming urban spaces into vibrant canvases broadcasting vital social messages.</p>
            </div>
            
            <div class="card delay-200">
              <span class="location-chip"><i data-lucide="map-pin"></i> RK Nagar</span>
              <h3>RWA Training</h3>
              <p>Empowering Residential Welfare Associations to govern effectively and maintain civic standards.</p>
            </div>
            
            <div class="card">
              <span class="location-chip"><i data-lucide="map-pin"></i> Multiple Locations</span>
              <h3>Urban Slum Initiatives</h3>
              <p>Targeted interventions in RK Nagar, Perumbakkam, and Athipattu.</p>
            </div>
            
            <div class="card delay-100">
              <span class="location-chip"><i data-lucide="map-pin"></i> Ezhil Nagar &amp; Perumbakkam</span>
              <h3>Entrepreneur Training</h3>
              <p>Capacity building workshops creating economic independence.</p>
              <p style="font-weight: 600; color: var(--color-primary); margin-top: auto;">100 Entrepreneurs Supported</p>
            </div>
            
            <div class="card delay-200">
              <span class="location-chip"><i data-lucide="map-pin"></i> Kuthambakkam Village</span>
              <h3>Play Area Construction</h3>
              <p>Building safe recreational spaces for children to play and grow.</p>
              <div class="chip mt-4" style="background:transparent; border:1px solid var(--color-border);">CSR: Malladi Drugs</div>
            </div>
          </div>
        </div>
      </section>
    """
  },
  {
    "name": "vocational.html",
    "title": "Vocational Training",
    "content": """
      <section class="page-hero reveal">
        <div class="container hero-content">
          <h1>Vocational Training</h1>
          <p>Building self-reliance through practical, hands-on skills.</p>
        </div>
      </section>

      <section class="section reveal">
        <div class="container">
          <span class="section-label text-center">Core Trades</span>
          <h2 class="text-center mb-8">Our Programs</h2>
          <div class="grid-2">
            <div class="card">
              <div class="card-icon"><i data-lucide="chef-hat"></i></div>
              <h3>Bakery & Life Skills Training</h3>
              <p>Teaching the art of baking combined with essential life skills to foster entrepreneurship and employment in the food industry.</p>
            </div>
            
            <div class="card delay-100">
              <div class="card-icon"><i data-lucide="coffee"></i></div>
              <h3>Hospitality Industry Training</h3>
              <p>Preparing individuals for entry-level and advanced roles within hotels, catering, and service sectors.</p>
            </div>
            
            <div class="card">
              <div class="card-icon"><i data-lucide="droplet"></i></div>
              <h3>RO Water Installation Training</h3>
              <p>Technical training for installing and maintaining reverse osmosis water systems, a highly demanded skill in urban areas.</p>
            </div>
            
            <div class="card delay-100">
              <div class="card-icon"><i data-lucide="zap"></i></div>
              <h3>Electrical and Plumbing Training</h3>
              <p>Core trades training empowering youth with reliable, high-demand skills for the construction and maintenance industries.</p>
            </div>
          </div>
        </div>
      </section>

      <section class="section section-offset reveal text-center">
        <div class="container">
          <span class="section-label text-center">Success</span>
          <h2 style="font-size: var(--text-2xl); font-weight: 700; color: var(--color-text); max-width: 800px; margin: 0 auto;">15 participants successfully transitioned to lives of respect and self-sufficiency</h2>
        </div>
      </section>
    """
  },
  {
    "name": "environment.html",
    "title": "Environment Sustainability",
    "content": """
      <section class="page-hero reveal">
        <div class="container hero-content">
          <h1>Environment Sustainability</h1>
          <p>Protecting our planet for future generations.</p>
        </div>
      </section>

      <section class="section reveal text-center">
        <div class="container">
          <span class="section-label text-center">Achievement</span>
          <h2 class="mb-6"><i data-lucide="award" style="display:inline; margin-right: 8px; color: var(--color-primary);"></i> Guinness World Record</h2>
          <p style="font-size: var(--text-lg); max-width: 800px; margin: 0 auto var(--space-12);">
            "Our Shoulders Foundation is a proud supporting partner of the Guinness World Record for planting approximately 30,000 seedlings with 20,000 participants in a 15-acre land, in collaboration with Sathyabama University."
          </p>
          
          <div class="grid-3 stats-strip" style="background:transparent; border:none; padding-block:0; margin-top: var(--space-8);">
            <div>
              <div class="stat-number counter" data-target="30000">0</div>
              <div class="stat-label">Seedlings</div>
            </div>
            <div>
              <div class="stat-number counter" data-target="20000">0</div>
              <div class="stat-label">Participants</div>
            </div>
            <div>
              <div class="stat-number counter" data-target="15">0</div>
              <div class="stat-label">Acres</div>
            </div>
          </div>
        </div>
      </section>

      <section class="section section-alt reveal">
        <div class="container grid-2" style="align-items: center;">
          <div>
            <span class="section-label">Conservation</span>
            <h2>Water Body Revival</h2>
            <h3 style="color: var(--color-text); font-weight: 600;">Water Alliance Project</h3>
            <p>Water is life. We are dedicated to cleaning, desilting, and reviving local lakes and ponds to restore local ecosystems and improve groundwater tables.</p>
            <div class="chip mt-4" style="background:transparent; border:1px solid var(--color-border);">In collaboration with CII</div>
          </div>
          <div>
            <div class="card text-center" style="border: 1px solid var(--color-primary);">
              <div style="font-size: var(--text-hero); font-weight: 700; color: var(--color-primary);">10</div>
              <p style="font-weight: 600; font-size: var(--text-lg); color: var(--color-text);">Water Bodies Restored</p>
              <p style="font-size: var(--text-sm);">(5 Major Lakes + 5 Ponds)</p>
            </div>
          </div>
        </div>
      </section>
    """
  },
  {
    "name": "farmers.html",
    "title": "Nurturing Farmers",
    "content": """
      <section class="page-hero reveal">
        <div class="container hero-content">
          <h1>Nurturing Farmers</h1>
          <p>Supporting the backbone of our nation.</p>
        </div>
      </section>

      <section class="section reveal">
        <div class="container grid-2">
          <div>
            <span class="section-label">Methodology</span>
            <h2>Our Approach</h2>
            <ul style="list-style: none; padding: 0;">
              <li style="margin-bottom: var(--space-4); display: flex; gap: var(--space-4);">
                <i data-lucide="sprout" style="color: var(--color-primary); flex-shrink: 0;"></i>
                <span>Blending modern agricultural techniques with traditional knowledge.</span>
              </li>
              <li style="margin-bottom: var(--space-4); display: flex; gap: var(--space-4);">
                <i data-lucide="book-open" style="color: var(--color-primary); flex-shrink: 0;"></i>
                <span>Providing sustainable farming training for maximum yield with minimum ecological impact.</span>
              </li>
              <li style="margin-bottom: var(--space-4); display: flex; gap: var(--space-4);">
                <i data-lucide="home" style="color: var(--color-primary); flex-shrink: 0;"></i>
                <span>Resettlement area agricultural support to ensure food security.</span>
              </li>
              <li style="margin-bottom: var(--space-4); display: flex; gap: var(--space-4);">
                <i data-lucide="handshake" style="color: var(--color-primary); flex-shrink: 0;"></i>
                <span>Government collaboration for last-mile support and resource distribution.</span>
              </li>
            </ul>
          </div>
          <div>
            <span class="section-label">Reach</span>
            <h2>Impact Areas</h2>
            <div class="card" style="margin-bottom: var(--space-4);">
              <span class="location-chip"><i data-lucide="map-pin"></i> Tiruvallur District</span>
              <h4 style="margin-bottom: var(--space-2);">Kuthambakkam Village</h4>
              <p style="margin-bottom: var(--space-2);">Supporting 300+ farming families with seeds, tools, and training.</p>
              <div class="chip" style="margin-top: 8px; background: transparent; border: 1px solid var(--color-border);">CSR Initiative</div>
            </div>
            
            <div class="card">
              <span class="location-chip"><i data-lucide="map-pin"></i> Multiple</span>
              <h4 style="margin-bottom: var(--space-2);">Resettlement Areas</h4>
              <p>Establishing local agricultural viability in collaboration with the Tamil Nadu Urban Habitat Development Board.</p>
            </div>
          </div>
        </div>
      </section>
    """
  },
  {
    "name": "volunteer.html",
    "title": "Volunteering",
    "content": """
      <section class="page-hero reveal">
        <div class="container hero-content">
          <h1>The Future Looks Bright</h1>
          <p>Join us and be the change.</p>
        </div>
      </section>

      <section class="section reveal">
        <div class="container">
          <span class="section-label text-center">Get Involved</span>
          <h2 class="text-center mb-12">Why Volunteer?</h2>
          <div class="grid-3">
            <div class="card text-center">
              <div class="card-icon mx-auto" style="margin: 0 auto var(--space-4);"><i data-lucide="briefcase"></i></div>
              <h3>For Professionals</h3>
              <p>Share your industry expertise and mentor the next generation of youth.</p>
            </div>
            <div class="card text-center delay-100">
              <div class="card-icon mx-auto" style="margin: 0 auto var(--space-4);"><i data-lucide="graduation-cap"></i></div>
              <h3>For Students</h3>
              <p>Gain real-world experience, fulfill service hours, and build your resume.</p>
            </div>
            <div class="card text-center delay-200">
              <div class="card-icon mx-auto" style="margin: 0 auto var(--space-4);"><i data-lucide="heart"></i></div>
              <h3>For Community</h3>
              <p>Give back to your neighborhood and help those who need it most.</p>
            </div>
          </div>
        </div>
      </section>

      <section class="section section-alt reveal">
        <div class="container">
          <span class="section-label text-center">Steps</span>
          <h2 class="text-center mb-12">How It Works</h2>
          <div class="timeline">
            <div class="timeline-step">
              <div class="timeline-number">1</div>
              <h4>Register</h4>
            </div>
            <div class="timeline-step">
              <div class="timeline-number">2</div>
              <h4>Select Your Mode</h4>
            </div>
            <div class="timeline-step">
              <div class="timeline-number">3</div>
              <h4>Choose Your Topic</h4>
            </div>
            <div class="timeline-step">
              <div class="timeline-number">4</div>
              <h4>Make an Impact</h4>
            </div>
          </div>
        </div>
      </section>

      <section class="section reveal">
        <div class="container">
          <span class="section-label text-center">Opportunities</span>
          <h2 class="text-center mb-12">Contribution Areas</h2>
          <div class="grid-3 text-center">
            <div class="card"><div class="card-icon" style="margin: 0 auto var(--space-4);"><i data-lucide="laptop"></i></div><h4>IT & Digital Training</h4></div>
            <div class="card"><div class="card-icon" style="margin: 0 auto var(--space-4);"><i data-lucide="stethoscope"></i></div><h4>Health Awareness</h4></div>
            <div class="card"><div class="card-icon" style="margin: 0 auto var(--space-4);"><i data-lucide="users"></i></div><h4>Community Outreach</h4></div>
            <div class="card"><div class="card-icon" style="margin: 0 auto var(--space-4);"><i data-lucide="tree-pine"></i></div><h4>Environmental Drives</h4></div>
            <div class="card"><div class="card-icon" style="margin: 0 auto var(--space-4);"><i data-lucide="message-square"></i></div><h4>Soft Skills & Career</h4></div>
            <div class="card"><div class="card-icon" style="margin: 0 auto var(--space-4);"><i data-lucide="calendar"></i></div><h4>Event Coordination</h4></div>
          </div>
        </div>
      </section>

      <section class="section section-offset reveal">
        <div class="container" style="max-width: 600px;">
          <div class="card text-center" style="border: 1px solid var(--color-primary);">
            <h2 class="mb-4">Ready to Start?</h2>
            <p class="mb-8">Contact us directly to discuss how you can contribute.</p>
            <div style="font-size: var(--text-lg); font-weight: 600; margin-bottom: var(--space-4);">
              <i data-lucide="mail" style="color: var(--color-primary); vertical-align: middle; margin-right: 8px;"></i> ourshoulder@gmail.com
            </div>
            <div style="font-size: var(--text-lg); font-weight: 600;">
              <i data-lucide="phone" style="color: var(--color-primary); vertical-align: middle; margin-right: 8px;"></i> +91 7373118000 / +91 9444334487
            </div>
          </div>
        </div>
      </section>
    """
  },
  {
    "name": "donate.html",
    "title": "Donate",
    "content": """
      <section class="page-hero reveal">
        <div class="container hero-content">
          <h1>Donate</h1>
          <p style="font-style: italic;">"It's Not How Much We Give &mdash; But How Much Love We Put Into Giving"</p>
        </div>
      </section>

      <section class="section reveal">
        <div class="container text-center" style="max-width: 800px; margin: 0 auto;">
          <span class="section-label">Support</span>
          <h2 class="mb-8">Make a Contribution</h2>
          
          <div class="card" style="border: 1px solid var(--color-primary); padding: var(--space-8); background: #fff; box-shadow: 0 10px 30px rgba(232, 119, 34, 0.1);">
            <div style="max-width: 350px; margin: 0 auto var(--space-6);">
              <img src="Our Shoulders QR.png" alt="Donate via UPI" style="width: 100%; border-radius: 12px; border: 1px solid var(--color-border);">
            </div>
            
            <h3 style="margin-bottom: var(--space-2);">Scan to Support</h3>
            <p style="font-weight: 700; font-size: var(--text-lg); margin-bottom: var(--space-6); color: var(--color-text);">UPI ID: ourshoulders@upi</p>
            
            <div class="mb-8" style="display: flex; justify-content: center; gap: var(--space-4); flex-wrap: wrap;">
              <div class="chip" style="font-size: var(--text-xs); background: white; border: 1px solid var(--color-border);"><i data-lucide="check-circle" style="color: var(--color-primary); margin-right: 6px;"></i> Section 12A Exemption</div>
              <div class="chip" style="font-size: var(--text-xs); background: white; border: 1px solid var(--color-border);"><i data-lucide="check-circle" style="color: var(--color-primary); margin-right: 6px;"></i> CSR-1 Certified</div>
              <div class="chip" style="font-size: var(--text-xs); background: white; border: 1px solid var(--color-border);"><i data-lucide="check-circle" style="color: var(--color-primary); margin-right: 6px;"></i> Section 80G — 50% Tax Exemption</div>
            </div>

            <p class="mb-4" style="font-size: var(--text-sm); color: var(--color-text-muted);">Accepted via all major UPI apps:</p>
            <div style="display: flex; justify-content: center; gap: var(--space-6); filter: grayscale(1); opacity: 0.7;">
              <span style="font-size: var(--text-xs); font-weight: 600;">Google Pay</span>
              <span style="font-size: var(--text-xs); font-weight: 600;">PhonePe</span>
              <span style="font-size: var(--text-xs); font-weight: 600;">Paytm</span>
              <span style="font-size: var(--text-xs); font-weight: 600;">BHIM</span>
            </div>
          </div>
          
          <div class="mt-12">
            <h3 class="mb-4">Program-Specific Support</h3>
            <div style="display: flex; flex-wrap: wrap; gap: var(--space-2); justify-content: center;">
              <span class="chip" style="background:var(--color-surface-offset);">Technical Skill Training</span>
              <span class="chip" style="background:var(--color-surface-offset);">Vocational Training</span>
              <span class="chip" style="background:var(--color-surface-offset);">Health & Sanitation</span>
              <span class="chip" style="background:var(--color-surface-offset);">Community Development</span>
              <span class="chip" style="background:var(--color-surface-offset);">Environment</span>
              <span class="chip" style="background:var(--color-surface-offset);">Farmers</span>
            </div>
            <p style="font-size: var(--text-sm); margin-top: var(--space-4); color: var(--color-text-muted);">Please mention the program name in your payment remarks.</p>
          </div>
        </div>
      </section>

      <section class="section section-alt reveal">
        <div class="container" style="max-width: 800px; margin: 0 auto;">
          <div class="text-center mb-10">
            <span class="section-label">Transparency</span>
            <h2>Your Impact</h2>
            <p>Every contribution directly supports our community initiatives.</p>
          </div>
          
          <div class="card" style="padding: 0; overflow: hidden; border: 1px solid var(--color-border);">
            <table class="impact-table" style="margin-bottom: 0;">
              <thead>
                <tr>
                  <th>Amount</th>
                  <th>Impact Details</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight: 600; color: var(--color-primary); white-space: nowrap;">₹500</td>
                  <td>Stationery and materials for one student</td>
                </tr>
                <tr>
                  <td style="font-weight: 600; color: var(--color-primary); white-space: nowrap;">₹1,000</td>
                  <td>Soft skills session for one beneficiary</td>
                </tr>
                <tr>
                  <td style="font-weight: 600; color: var(--color-primary); white-space: nowrap;">₹5,000</td>
                  <td>Full course enrollment for one student</td>
                </tr>
                <tr>
                  <td style="font-weight: 600; color: var(--color-primary); white-space: nowrap;">₹10,000</td>
                  <td>Hygiene kit and health awareness for 10 families</td>
                </tr>
                <tr>
                  <td style="font-weight: 600; color: var(--color-primary); white-space: nowrap;">₹25,000+</td>
                  <td>Support for one entrepreneur's business training</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>
    """
  },
  {
    "name": "contact.html",
    "title": "Contact Us",
    "content": """
      <section class="page-hero reveal">
        <div class="container hero-content">
          <h1>Reach Out</h1>
          <p>We'd Love to Hear from You</p>
        </div>
      </section>

      <section class="section reveal">
        <div class="container grid-2">
          <div>
            <span class="section-label">Connect</span>
            <h2 class="mb-8">Get in Touch</h2>
            <div class="mb-8">
              <h4 style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;"><i data-lucide="map-pin" style="color: var(--color-primary);"></i> Address</h4>
              <p>13, 8th Street, Samayapuram,<br>Karambakkam-Porur,<br>Chennai &ndash; 600 116</p>
            </div>
            
            <div class="mb-8">
              <h4 style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;"><i data-lucide="phone" style="color: var(--color-primary);"></i> Phone</h4>
              <p>+91 7373118000<br>+91 9444334487</p>
            </div>
            
            <div class="mb-8">
              <h4 style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;"><i data-lucide="mail" style="color: var(--color-primary);"></i> Email</h4>
              <p>ourshoulder@gmail.com</p>
            </div>

            <div style="border-radius: 10px; overflow: hidden; height: 300px; background-color: var(--color-surface-offset); border: 1px solid var(--color-border);">
              <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3886.852445695576!2d80.15878411534063!3d13.044458990808204!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a52611a1961dc2d%3A0xcda6b0d91244e69b!2sPorur%2C%20Chennai%2C%20Tamil%20Nadu!5e0!3m2!1sen!2sin!4v1625567843729!5m2!1sen!2sin" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
            </div>
          </div>
          
          <div>
            <div class="card">
              <h2 class="mb-6">Send a Message</h2>
              <form id="contact-form" novalidate>
                <div class="form-group">
                  <label for="name" class="form-label">Name*</label>
                  <input type="text" id="name" name="name" class="form-input" required>
                  <div class="form-error">Please enter your name.</div>
                </div>
                
                <div class="form-group">
                  <label for="email" class="form-label">Email*</label>
                  <input type="email" id="email" name="email" class="form-input" required>
                  <div class="form-error">Please enter a valid email address.</div>
                </div>
                
                <div class="grid-2" style="gap: var(--space-4);">
                  <div class="form-group">
                    <label for="phone" class="form-label">Phone</label>
                    <input type="tel" id="phone" name="phone" class="form-input">
                  </div>
                  <div class="form-group">
                    <label for="subject" class="form-label">Subject</label>
                    <input type="text" id="subject" name="subject" class="form-input">
                  </div>
                </div>
                
                <div class="form-group">
                  <label for="address" class="form-label">Address</label>
                  <input type="text" id="address" name="address" class="form-input">
                </div>
                
                <div class="form-group">
                  <label for="message" class="form-label">Message*</label>
                  <textarea id="message" name="message" class="form-input" required></textarea>
                  <div class="form-error">Please enter a message.</div>
                </div>
                
                <button type="submit" class="btn btn-primary" style="width: 100%;">Submit Message</button>
                <div id="form-success" class="success-message"></div>
              </form>
            </div>
          </div>
        </div>
      </section>
    """
  }
]

for page in pages:
  content = header_html.replace("{title}", page["title"]) + page["content"] + footer_html
  with open(page["name"], "w", encoding="utf-8") as f:
    f.write(content)
  print(f"Created {page['name']}")
