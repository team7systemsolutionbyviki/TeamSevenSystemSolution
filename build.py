import os

base_dir = r"e:\MY BILLING APP\TeamSevenSystemSolution"

header = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Team Seven System Solution</title>
    <meta name="description" content="Team Seven System Solution provides CCTV, computer, laptop, custom PC, printer, website development, billing software, printing, photo frames, advertising and event solutions.">
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    <!-- FontAwesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <!-- Header Navigation -->
    <header id="header">
        <div class="container navbar">
            <div class="logo">
                <span class="logo-text">TEAM 7</span>
                <span class="logo-sub">SYSTEM SOLUTION</span>
            </div>
            <div class="menu-toggle"><i class="fas fa-bars"></i></div>
            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="services.html">Services</a></li>
                <li><a href="product.html">Products</a></li>
                <li><a href="website.html">Websites</a></li>
                <li><a href="printing.html">Printing</a></li>
                <li><a href="job.html">Job Enquiry</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
            <div class="nav-actions">
                <a href="#" class="btn btn-outline" data-wa-msg="Hi Team Seven System Solution, I have an enquiry.">
                    <i class="fab fa-whatsapp"></i> WhatsApp Enquiry
                </a>
                <a href="contact.html#quote" class="btn btn-primary">Get a Quote</a>
            </div>
        </div>
    </header>
"""

footer = """
    <!-- Footer -->
    <footer id="footer" class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <div class="logo">
                        <span class="logo-text" style="color: var(--text-white);">TEAM 7</span>
                        <span class="logo-sub" style="color: var(--secondary);">SYSTEM SOLUTION</span>
                    </div>
                    <p>Your one-stop destination for complete IT hardware, software, digital services, and printing solutions.</p>
                </div>
                
                <div>
                    <h4 class="footer-title">Quick Links</h4>
                    <ul class="footer-links">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="about.html">About</a></li>
                        <li><a href="services.html">Services</a></li>
                        <li><a href="product.html">Products</a></li>
                        <li><a href="website.html">Websites</a></li>
                        <li><a href="job.html">Job Enquiry</a></li>
                        <li><a href="contact.html">Contact Us</a></li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="footer-title">Our Services</h4>
                    <ul class="footer-links">
                        <li><a href="services.html">CCTV Installation</a></li>
                        <li><a href="services.html">Computer & Laptops</a></li>
                        <li><a href="services.html#custom-pc">Custom PCs</a></li>
                        <li><a href="website.html">Website Development</a></li>
                        <li><a href="services.html#billing">Billing Software</a></li>
                        <li><a href="printing.html">Printing & Design</a></li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="footer-title">Contact</h4>
                    <ul class="footer-links">
                        <li><i class="fas fa-phone-alt" style="margin-right: 8px;"></i> 9360039283</li>
                        <li><i class="fab fa-whatsapp" style="margin-right: 8px;"></i> 9360039283</li>
                    </ul>
                    <a href="contact.html#quote" class="btn btn-outline" style="margin-top: 15px; border-color: rgba(255,255,255,0.2); color: white;">Request Quote</a>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2026 Team Seven System Solution. All Rights Reserved.</p>
            </div>
        </div>
    </footer>

    <!-- Floating WhatsApp Button -->
    <a href="#" class="fab-whatsapp" data-wa-msg="Hi Team Seven System Solution, I would like to enquire about your products/services." title="Chat on WhatsApp">
        <i class="fab fa-whatsapp"></i>
    </a>

    <!-- Custom JS -->
    <script src="js/script.js"></script>
</body>
</html>
"""

def make_page(title, body):
    return header.replace("{title}", title) + body + footer

pages = {}

# 1. HOME
pages["index.html"] = make_page("Home", """
    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="hero-pattern"></div>
        <div class="container hero-content">
            <div class="hero-badge"><i class="fas fa-microchip"></i> Technology & Business Partner</div>
            <h1>Complete IT & Digital Solutions <span>For Your Business</span></h1>
            <p class="hero-subtitle">CCTV • Computers • Laptops • Custom PCs • Websites • Printing • Design • Billing Software & More</p>
            <p>From computer sales and CCTV installation to custom websites, printing, advertising products and business software, Team Seven System Solution provides complete technology and digital solutions.</p>
            <div class="hero-buttons">
                <a href="contact.html#quote" class="btn btn-primary"><i class="fas fa-file-invoice"></i> Get a Free Quote</a>
                <a href="#" class="btn btn-outline-light" data-wa-msg="Hi Team Seven System Solution, I would like to enquire about your products/services."><i class="fab fa-whatsapp"></i> WhatsApp Us</a>
            </div>
        </div>
    </section>
    
    <section class="section">
        <div class="container" style="text-align: center;">
            <div class="section-header">
                <h2>Welcome to Team Seven System Solution</h2>
                <p>We are your one-stop destination for complete IT hardware, software, digital services, and printing solutions.</p>
            </div>
            <div style="margin-top: 40px;">
                <a href="services.html" class="btn btn-outline">Explore All Services <i class="fas fa-arrow-right"></i></a>
            </div>
        </div>
    </section>
""")

# 2. ABOUT
pages["about.html"] = make_page("About Us", """
    <section style="padding: 150px 0 80px; background: var(--bg-gradient); color: white; text-align: center;">
        <div class="container">
            <h1 style="font-size: 3.5rem; margin-bottom: 16px; color: white;">About Us</h1>
            <p style="color: #94a3b8; font-size: 1.125rem;">Your Trusted Technology & Digital Partner</p>
        </div>
    </section>
    
    <section class="section">
        <div class="container">
            <div class="split-section">
                <div>
                    <h2 style="font-size: 2.5rem; margin-bottom: 20px;">Who We Are</h2>
                    <p style="font-size: 1.1rem; color: var(--text-light); margin-bottom: 20px;">Team Seven System Solution is a premier IT hardware and digital services provider. We specialize in providing end-to-end technology solutions ranging from CCTV installations and computer repairs to custom web development and business printing.</p>
                    
                    <h2 style="font-size: 2.5rem; margin-bottom: 20px; margin-top: 40px;">Our Mission</h2>
                    <p style="font-size: 1.1rem; color: var(--text-light); margin-bottom: 20px;">Our goal is to empower businesses and individuals with highly reliable, fast, and modern technology. We pride ourselves on top-notch customer service, affordable pricing, and delivering exactly what our clients need to succeed in the digital world.</p>
                </div>
                <div style="background: rgba(14,165,233,0.1); border-radius: var(--radius-lg); padding: 40px; border: 1px solid rgba(14,165,233,0.2);">
                    <h3 style="margin-bottom: 20px; font-size: 1.5rem;">Why Choose Us?</h3>
                    <ul class="card-list">
                        <li><i class="fas fa-check"></i> Experienced & Professional Team</li>
                        <li><i class="fas fa-check"></i> Comprehensive Solutions Under One Roof</li>
                        <li><i class="fas fa-check"></i> High-Quality Products & Services</li>
                        <li><i class="fas fa-check"></i> 100% Customer Satisfaction Guaranteed</li>
                        <li><i class="fas fa-check"></i> Affordable & Transparent Pricing</li>
                    </ul>
                    <a href="contact.html" class="btn btn-primary" style="margin-top: 20px;">Contact Us</a>
                </div>
            </div>
        </div>
    </section>
""")

# 3. SERVICES
pages["services.html"] = make_page("Services", """
    <section style="padding: 150px 0 80px; background: var(--bg-gradient); color: white; text-align: center;">
        <div class="container">
            <h1 style="font-size: 3.5rem; margin-bottom: 16px; color: white;">Our Services</h1>
            <p style="color: #94a3b8; font-size: 1.125rem;">Professional IT hardware, security, and digital services.</p>
        </div>
    </section>
    
    <section class="section">
        <div class="container">
            <div class="services-grid">
                <!-- CCTV Card -->
                <div class="card">
                    <div class="card-icon"><i class="fas fa-video"></i></div>
                    <h3>CCTV Solutions</h3>
                    <ul class="card-list">
                        <li><i class="fas fa-check"></i> CCTV Camera Sales</li>
                        <li><i class="fas fa-check"></i> CCTV Installation</li>
                        <li><i class="fas fa-check"></i> DVR/NVR Setup</li>
                        <li><i class="fas fa-check"></i> Remote Mobile Viewing</li>
                        <li><i class="fas fa-check"></i> Home & Business Security</li>
                    </ul>
                    <a href="#" class="btn btn-outline btn-block" data-wa-msg="Hi Team Seven System Solution, I need a quotation for CCTV installation. Please contact me.">Get CCTV Quote</a>
                </div>

                <!-- Laptop Card -->
                <div class="card">
                    <div class="card-icon"><i class="fas fa-laptop"></i></div>
                    <h3>Laptop Services</h3>
                    <ul class="card-list">
                        <li><i class="fas fa-check"></i> Laptop Sales</li>
                        <li><i class="fas fa-check"></i> Laptop Repair & Upgrades</li>
                        <li><i class="fas fa-check"></i> SSD & RAM Upgrade</li>
                        <li><i class="fas fa-check"></i> Windows Installation</li>
                        <li><i class="fas fa-check"></i> Data Backup & Recovery</li>
                    </ul>
                    <a href="#" class="btn btn-outline btn-block" data-wa-msg="Hi Team Seven System Solution, I am looking for a laptop. Please send available options and pricing.">Laptop Enquiry</a>
                </div>

                <!-- PC Card -->
                <div class="card">
                    <div class="card-icon"><i class="fas fa-desktop"></i></div>
                    <h3>Computer Services</h3>
                    <ul class="card-list">
                        <li><i class="fas fa-check"></i> Desktop PC Sales</li>
                        <li><i class="fas fa-check"></i> Computer Repair</li>
                        <li><i class="fas fa-check"></i> Office PC Setup</li>
                        <li><i class="fas fa-check"></i> Hardware Installation</li>
                        <li><i class="fas fa-check"></i> System Maintenance</li>
                    </ul>
                    <a href="#" class="btn btn-outline btn-block" data-wa-msg="Hi Team Seven System Solution, I need a quotation for a Computer/Desktop. Please contact me.">PC Enquiry</a>
                </div>

                <!-- Printer Card -->
                <div class="card">
                    <div class="card-icon"><i class="fas fa-print"></i></div>
                    <h3>Printer Services</h3>
                    <ul class="card-list">
                        <li><i class="fas fa-check"></i> Printer Sales & Setup</li>
                        <li><i class="fas fa-check"></i> Printer Repair</li>
                        <li><i class="fas fa-check"></i> Toner Refill</li>
                        <li><i class="fas fa-check"></i> Cartridge Services</li>
                        <li><i class="fas fa-check"></i> Network Printer Setup</li>
                    </ul>
                    <a href="#" class="btn btn-outline btn-block" data-wa-msg="Hi Team Seven System Solution, I have an enquiry regarding printers/toners.">Printer Enquiry</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Custom PC Section -->
    <section id="custom-pc" class="section custom-pc-section">
        <div class="container custom-pc-grid">
            <div class="pc-content">
                <h2>Build Your Custom PC</h2>
                <p>From high-performance gaming rigs to reliable office workstations, we build Custom PCs strictly according to your budget and processing requirements.</p>
                
                <div class="pc-features">
                    <div class="pc-feature"><i class="fas fa-gamepad"></i> <span>Gaming PC</span></div>
                    <div class="pc-feature"><i class="fas fa-briefcase"></i> <span>Office PC</span></div>
                    <div class="pc-feature"><i class="fas fa-video"></i> <span>Editing PC</span></div>
                    <div class="pc-feature"><i class="fas fa-code"></i> <span>AI/Dev PC</span></div>
                </div>
                
                <a href="#" class="btn btn-primary" data-wa-msg="Hi Team Seven System Solution, I need a quotation for a Custom PC. Please contact me for configuration.">
                    <i class="fas fa-tools"></i> Request Custom PC Quote
                </a>
            </div>
            <div class="pc-visual">
                <div class="pc-placeholder">
                    <i class="fas fa-memory"></i>
                </div>
            </div>
        </div>
    </section>

    <!-- Billing Software -->
    <section id="billing" class="section section-alt">
        <div class="container split-section">
            <div class="split-visual">
                <img src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&q=80&w=600&h=400" alt="Billing Software" style="width: 100%; border-radius: var(--radius-lg); box-shadow: var(--shadow-lg);">
            </div>
            <div class="split-content">
                <h2>Billing & Business Software</h2>
                <p>Simple billing and business management solutions for shops and businesses. Manage inventory, sales, and customers effortlessly.</p>
                
                <div class="feature-grid">
                    <div class="feature-grid-item"><i class="fas fa-receipt"></i> POS Software</div>
                    <div class="feature-grid-item"><i class="fas fa-boxes"></i> Inventory Management</div>
                    <div class="feature-grid-item"><i class="fas fa-file-invoice-dollar"></i> GST Reports</div>
                    <div class="feature-grid-item"><i class="fas fa-users"></i> Customer Ledger</div>
                    <div class="feature-grid-item"><i class="fas fa-barcode"></i> Barcode Support</div>
                    <div class="feature-grid-item"><i class="fab fa-whatsapp"></i> WhatsApp Bill Sharing</div>
                </div>
                
                <a href="#" class="btn btn-primary" data-wa-msg="Hi Team Seven System Solution, I am interested in billing/POS software. Please contact me.">Billing Software Enquiry</a>
            </div>
        </div>
    </section>
""")

# 4. PRODUCTS
pages["product.html"] = make_page("Products", """
    <section style="padding: 150px 0 80px; background: var(--bg-gradient); color: white; text-align: center;">
        <div class="container">
            <h1 style="font-size: 3.5rem; margin-bottom: 16px; color: white;">Our Products</h1>
            <p style="color: #94a3b8; font-size: 1.125rem;">Browse our extensive range of hardware and accessories.</p>
        </div>
    </section>
    
    <section class="section">
        <div class="container">
            <div class="products-grid">
                <a href="#" class="product-category" data-wa-msg="Hi Team Seven System Solution, I need information about Desktop Computers.">
                    <i class="fas fa-desktop"></i>
                    <h4>Computers</h4>
                    <span style="font-size: 0.8rem; color: var(--text-light);">Desktops, Custom, Office</span>
                </a>
                <a href="#" class="product-category" data-wa-msg="Hi Team Seven System Solution, I need information about Laptops.">
                    <i class="fas fa-laptop"></i>
                    <h4>Laptops</h4>
                    <span style="font-size: 0.8rem; color: var(--text-light);">Business, Student, Refurbished</span>
                </a>
                <a href="#" class="product-category" data-wa-msg="Hi Team Seven System Solution, I need information about CCTV Cameras & Accessories.">
                    <i class="fas fa-camera"></i>
                    <h4>CCTV</h4>
                    <span style="font-size: 0.8rem; color: var(--text-light);">Cameras, DVR, NVR, Cables</span>
                </a>
                <a href="#" class="product-category" data-wa-msg="Hi Team Seven System Solution, I need information about Printers & Toners.">
                    <i class="fas fa-print"></i>
                    <h4>Printers</h4>
                    <span style="font-size: 0.8rem; color: var(--text-light);">Laser, Inkjet, Thermal, Toner</span>
                </a>
                <a href="#" class="product-category" data-wa-msg="Hi Team Seven System Solution, I need information about Computer Accessories.">
                    <i class="fas fa-keyboard"></i>
                    <h4>Accessories</h4>
                    <span style="font-size: 0.8rem; color: var(--text-light);">Keyboard, Mouse, Cables</span>
                </a>
                <a href="#" class="product-category" data-wa-msg="Hi Team Seven System Solution, I need information about PC Components (RAM/SSD).">
                    <i class="fas fa-memory"></i>
                    <h4>Components</h4>
                    <span style="font-size: 0.8rem; color: var(--text-light);">RAM, SSD, Hard Disk, Motherboards</span>
                </a>
            </div>
        </div>
    </section>
""")

# 5. WEBSITE
pages["website.html"] = make_page("Website Development", """
    <section style="padding: 150px 0 80px; background: var(--bg-gradient); color: white; text-align: center;">
        <div class="container">
            <h1 style="font-size: 3.5rem; margin-bottom: 16px; color: white;">Website Development</h1>
            <p style="color: #94a3b8; font-size: 1.125rem;">From simple portfolio websites to complete business websites and hosting solutions.</p>
        </div>
    </section>
    
    <section class="section">
        <div class="container">
            <div class="pricing-grid">
                <!-- Portfolio -->
                <div class="price-card">
                    <h3>Portfolio Website</h3>
                    <div class="price" id="price-portfolio">Loading...</div>
                    <p>Perfect for Professionals, Freelancers & Students</p>
                    <ul class="card-list" style="text-align: left; margin-bottom: 30px;">
                        <li><i class="fas fa-check"></i> Single Page Layout</li>
                        <li><i class="fas fa-check"></i> Mobile Responsive</li>
                        <li><i class="fas fa-check"></i> Contact Form</li>
                        <li><i class="fas fa-check"></i> Social Media Links</li>
                    </ul>
                    <a href="#" class="btn btn-outline btn-block" data-wa-msg="Hi Team Seven System Solution, I am interested in the Portfolio Website package.">Select Package</a>
                </div>

                <!-- Static Business -->
                <div class="price-card popular">
                    <div class="popular-badge">Most Popular</div>
                    <h3>Static Business Website</h3>
                    <div class="price" id="price-static">Loading...</div>
                    <p>Ideal for Shops, Agencies & Service Businesses</p>
                    <ul class="card-list" style="text-align: left; margin-bottom: 30px;">
                        <li><i class="fas fa-check"></i> Multi-page Website</li>
                        <li><i class="fas fa-check"></i> Product/Service Catalog</li>
                        <li><i class="fas fa-check"></i> WhatsApp Integration</li>
                        <li><i class="fas fa-check"></i> Google Maps & SEO Basics</li>
                    </ul>
                    <a href="#" class="btn btn-primary btn-block" data-wa-msg="Hi Team Seven System Solution, I am interested in the Static Business Website package.">Select Package</a>
                </div>

                <!-- Full Custom -->
                <div class="price-card">
                    <h3>Custom / Hosting</h3>
                    <div class="price" id="price-custom" style="font-size: 1.8rem;">Loading...</div>
                    <p>Complete Domain + Hosting + Website solutions</p>
                    <ul class="card-list" style="text-align: left; margin-bottom: 30px;">
                        <li><i class="fas fa-check"></i> Custom Requirements</li>
                        <li><i class="fas fa-check"></i> Domain Registration</li>
                        <li><i class="fas fa-check"></i> Cloud Hosting Setup</li>
                        <li><i class="fas fa-check"></i> Business Emails</li>
                    </ul>
                    <a href="#" class="btn btn-outline btn-block" data-wa-msg="Hi Team Seven System Solution, I need a website. Please contact me regarding website development and pricing.">Get Custom Quote</a>
                </div>
            </div>
        </div>
    </section>
""")

# 6. PRINTING
pages["printing.html"] = make_page("Printing & Advertising", """
    <section style="padding: 150px 0 80px; background: var(--bg-gradient); color: white; text-align: center;">
        <div class="container">
            <h1 style="font-size: 3.5rem; margin-bottom: 16px; color: white;">Printing, Design & Advertising</h1>
            <p style="color: #94a3b8; font-size: 1.125rem;">Creative design and high-quality printing services to promote your business effectively.</p>
        </div>
    </section>
    
    <section class="section">
        <div class="container">
            <div class="services-grid" style="grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));">
                <div class="card">
                    <div class="card-icon"><i class="fas fa-print"></i></div>
                    <h3>Printing Services</h3>
                    <p style="color: var(--text-light); margin-bottom: 16px; font-size: 0.9rem;">Visiting Cards, Flyers, Brochures, ID Cards, Bill Books, Certificates, Stickers.</p>
                    <a href="#" class="btn btn-outline btn-block" data-wa-msg="Hi Team Seven System Solution, I need a quotation for printing services.">Enquire Now</a>
                </div>
                
                <div class="card">
                    <div class="card-icon"><i class="fas fa-ad"></i></div>
                    <h3>Advertising</h3>
                    <p style="color: var(--text-light); margin-bottom: 16px; font-size: 0.9rem;">Flex Boards, Banners, Shop Boards, Vinyl Stickers, Promotional Materials.</p>
                    <a href="#" class="btn btn-outline btn-block" data-wa-msg="Hi Team Seven System Solution, I need a quotation for advertising materials/boards.">Enquire Now</a>
                </div>
                
                <div class="card">
                    <div class="card-icon"><i class="fas fa-image"></i></div>
                    <h3>Photo Frames</h3>
                    <p style="color: var(--text-light); margin-bottom: 16px; font-size: 0.9rem;">Custom Photo Frames, Photo Printing, Wedding Invitations, Digital Invitations.</p>
                    <a href="#" class="btn btn-outline btn-block" data-wa-msg="Hi Team Seven System Solution, I am enquiring about Photo Frames/Invitations.">Enquire Now</a>
                </div>
                
                <div class="card">
                    <div class="card-icon"><i class="fas fa-calendar-alt"></i></div>
                    <h3>Event Solutions</h3>
                    <p style="color: var(--text-light); margin-bottom: 16px; font-size: 0.9rem;">Event Websites, Registration Systems, Posters, Banners, Digital Support.</p>
                    <a href="#" class="btn btn-outline btn-block" data-wa-msg="Hi Team Seven System Solution, I need digital/print support for an Event.">Enquire Now</a>
                </div>
            </div>
        </div>
    </section>
""")

# 7. JOB ENQUIRY
pages["job.html"] = make_page("Job Enquiry", """
    <section style="padding: 150px 0 80px; background: var(--bg-gradient); color: white; text-align: center;">
        <div class="container">
            <h1 style="font-size: 3.5rem; margin-bottom: 16px; color: white;">Join Team Seven System Solution</h1>
            <p style="color: #94a3b8; font-size: 1.125rem;">We are always interested in connecting with talented professionals.</p>
        </div>
    </section>
    
    <section class="section">
        <div class="container">
            <div class="form-container">
                <form id="job-form">
                    <div class="form-grid">
                        <div class="form-group">
                            <label for="j-name">Full Name</label>
                            <input type="text" id="j-name" class="form-control" required placeholder="Your name">
                        </div>
                        <div class="form-group">
                            <label for="j-mobile">Mobile Number</label>
                            <input type="tel" id="j-mobile" class="form-control" required placeholder="Your contact number">
                        </div>
                        <div class="form-group">
                            <label for="j-email">Email Address</label>
                            <input type="email" id="j-email" class="form-control" placeholder="Optional">
                        </div>
                        <div class="form-group">
                            <label for="j-position">Position Interested In</label>
                            <select id="j-position" class="form-control" required>
                                <option value="">Select Position...</option>
                                <option value="Computer Technician">Computer Technician</option>
                                <option value="Laptop Technician">Laptop Technician</option>
                                <option value="CCTV Technician">CCTV Technician</option>
                                <option value="Printer Technician">Printer Technician</option>
                                <option value="Web Developer">Web Developer</option>
                                <option value="Graphic Designer">Graphic Designer</option>
                                <option value="Sales Executive">Sales Executive</option>
                                <option value="IT Support">IT Support</option>
                                <option value="Other">Other</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="j-exp">Experience</label>
                            <select id="j-exp" class="form-control" required>
                                <option value="Fresher">Fresher (0 Years)</option>
                                <option value="1-2 Years">1-2 Years</option>
                                <option value="3-5 Years">3-5 Years</option>
                                <option value="5+ Years">5+ Years</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="j-location">Your Location</label>
                            <input type="text" id="j-location" class="form-control" required placeholder="Where do you live?">
                        </div>
                        <div class="form-group full-width">
                            <label for="j-skills">Core Skills</label>
                            <input type="text" id="j-skills" class="form-control" required placeholder="E.g. Hardware assembling, HTML/CSS, Photoshop">
                        </div>
                        <div class="form-group full-width">
                            <label for="j-intro">Short Introduction</label>
                            <textarea id="j-intro" class="form-control" required placeholder="Tell us briefly about yourself..."></textarea>
                        </div>
                        <div class="form-group full-width" style="margin-top: 10px;">
                            <button type="submit" class="btn btn-outline btn-block" style="font-size: 1.1rem; padding: 14px;"><i class="fab fa-whatsapp"></i> Send Job Application</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </section>
""")

# 8. CONTACT
pages["contact.html"] = make_page("Contact Us", """
    <section style="padding: 150px 0 80px; background: var(--bg-gradient); color: white; text-align: center;">
        <div class="container">
            <h1 style="font-size: 3.5rem; margin-bottom: 16px; color: white;">Contact Us</h1>
            <p style="color: #94a3b8; font-size: 1.125rem;">Get in touch for quotations, enquiries, and support.</p>
        </div>
    </section>
    
    <section id="quote" class="section">
        <div class="container">
            <div class="section-header">
                <h2>Request a Free Quote</h2>
                <p>Fill out the form below and we will get back to you with a personalized quotation via WhatsApp.</p>
            </div>
            
            <div class="form-container">
                <form id="quote-form">
                    <div class="form-grid">
                        <div class="form-group">
                            <label for="q-name">Your Name</label>
                            <input type="text" id="q-name" class="form-control" required placeholder="Enter your name">
                        </div>
                        <div class="form-group">
                            <label for="q-mobile">Mobile Number</label>
                            <input type="tel" id="q-mobile" class="form-control" required placeholder="Enter WhatsApp number">
                        </div>
                        <div class="form-group">
                            <label for="q-service">Service / Product</label>
                            <select id="q-service" class="form-control" required>
                                <option value="">Select Service...</option>
                                <option value="CCTV">CCTV Setup / Purchase</option>
                                <option value="Laptop">Laptop Sales / Service</option>
                                <option value="Desktop PC">Desktop PC</option>
                                <option value="Custom PC">Custom Built PC</option>
                                <option value="Printer">Printer / Toner</option>
                                <option value="Website - Portfolio">Portfolio Website</option>
                                <option value="Website - Static">Static Business Website</option>
                                <option value="Website - Custom">Custom/Hosting Website</option>
                                <option value="Billing Software">Billing & POS Software</option>
                                <option value="Printing">Printing Services</option>
                                <option value="Advertising">Advertising & Flex</option>
                                <option value="Event Management">Event Management Solutions</option>
                                <option value="Other">Other</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="q-budget">Estimated Budget</label>
                            <input type="text" id="q-budget" class="form-control" placeholder="E.g. ₹10,000 or Not sure">
                        </div>
                        <div class="form-group full-width">
                            <label for="q-requirement">Specific Requirement</label>
                            <textarea id="q-requirement" class="form-control" required placeholder="Describe what you need..."></textarea>
                        </div>
                        <div class="form-group">
                            <label for="q-location">Location / Area</label>
                            <input type="text" id="q-location" class="form-control" required placeholder="Your city/area">
                        </div>
                        <div class="form-group">
                            <label for="q-contact">Preferred Contact Method</label>
                            <select id="q-contact" class="form-control">
                                <option value="WhatsApp">WhatsApp Message</option>
                                <option value="Phone Call">Phone Call</option>
                            </select>
                        </div>
                        <div class="form-group full-width" style="margin-top: 10px;">
                            <button type="submit" class="btn btn-primary btn-block" style="font-size: 1.1rem; padding: 14px;"><i class="fab fa-whatsapp"></i> Send Quote Request via WhatsApp</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </section>
    
    <section class="section section-alt">
        <div class="container">
            <div class="contact-grid">
                <div class="contact-info-card">
                    <h3>Contact Information</h3>
                    <div class="contact-details">
                        <div class="contact-item">
                            <div class="contact-icon"><i class="fas fa-building"></i></div>
                            <div>
                                <h4 style="color: var(--text-white); margin-bottom: 5px;">TEAM SEVEN SYSTEM SOLUTION</h4>
                                <p style="color: rgba(255,255,255,0.8); font-size: 0.95rem;">Complete IT, Digital, Printing & Business Solutions.</p>
                            </div>
                        </div>
                        <div class="contact-item">
                            <div class="contact-icon"><i class="fas fa-phone-alt"></i></div>
                            <div>
                                <h4 style="color: var(--text-white); margin-bottom: 5px;">Call Us</h4>
                                <p style="color: rgba(255,255,255,0.8); font-size: 1.1rem; font-weight: 600;">9360039283</p>
                            </div>
                        </div>
                        <div class="contact-item">
                            <div class="contact-icon"><i class="fab fa-whatsapp"></i></div>
                            <div>
                                <h4 style="color: var(--text-white); margin-bottom: 5px;">WhatsApp</h4>
                                <p style="color: rgba(255,255,255,0.8); font-size: 1.1rem; font-weight: 600;">9360039283</p>
                            </div>
                        </div>
                    </div>
                    
                    <div style="display: flex; gap: 15px; margin-top: 20px;">
                        <button class="btn btn-primary" data-call style="flex: 1;"><i class="fas fa-phone"></i> Call Now</button>
                        <button class="btn btn-outline-light" data-wa-msg="Hi Team Seven System Solution, I have an enquiry." style="flex: 1;"><i class="fab fa-whatsapp"></i> WhatsApp</button>
                    </div>
                </div>
                
                <div class="contact-map">
                    <div class="map-placeholder">
                        <i class="fas fa-map-marker-alt"></i>
                        <h4 style="color: var(--text-main); margin-bottom: 8px;">Find Our Store</h4>
                        <p style="text-align: center; max-width: 80%;">Google Maps integration can be easily placed here by embedding an iframe code.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
""")

for file_name, content in pages.items():
    with open(os.path.join(base_dir, file_name), "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(pages)} pages successfully.")
