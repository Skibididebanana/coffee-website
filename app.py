from flask import Flask, render_template_string
import os

app = Flask(__name__)

# HTML template for the main page with new hero section and mega menus
MAIN_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Office Coffee Co. - Professional Coffee Solutions</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
        }

        /* Header Navigation */
        .header {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            padding: 15px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(0, 0, 0, 0.1);
        }

        .logo {
            font-size: 1.8rem;
            font-weight: 700;
            color: #2c1810;
            text-decoration: none;
            letter-spacing: -0.5px;
            line-height: 1.2;
        }

        .nav {
            display: flex;
            gap: 30px;
            position: relative;
        }

        .nav-item {
            position: relative;
        }

        .nav a {
            color: #4a4a4a;
            text-decoration: none;
            font-weight: 500;
            font-size: 0.95rem;
            transition: color 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .nav a:hover {
            color: #6b4423;
        }

        .nav-item.active a {
            color: #6b8e5a;
            border-bottom: 2px solid #6b8e5a;
            padding-bottom: 2px;
        }

        .contact-info {
            display: flex;
            align-items: center;
            gap: 15px;
            color: #4a4a4a;
            font-weight: 500;
        }

        .contact-btn {
            background: #6b4423;
            color: white;
            padding: 8px 20px;
            border: none;
            border-radius: 25px;
            font-weight: 500;
            cursor: pointer;
            transition: background 0.3s ease;
        }

        .contact-btn:hover {
            background: #5a3619;
        }

        .contact-side-btn {
            position: fixed;
            right: 0;
            top: 50%;
            transform: translateY(-50%);
            background: #6b8e5a;
            color: white;
            padding: 60px 20px;
            border: none;
            cursor: pointer;
            writing-mode: vertical-lr;
            text-orientation: mixed;
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            z-index: 999;
            transition: background 0.3s ease;
        }

        .contact-side-btn:hover {
            background: #5a7a4a;
        }

        /* Hero Section */
        .hero-section {
            height: 100vh;
            background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800"><rect width="1200" height="800" fill="%23f0f0f0"/><circle cx="300" cy="400" r="60" fill="%23ffffff" opacity="0.8"/><circle cx="900" cy="300" r="40" fill="%23ffffff" opacity="0.6"/><rect x="250" y="350" width="100" height="100" rx="50" fill="%23f5f5f5"/><rect x="850" y="250" width="100" height="100" rx="50" fill="%23f5f5f5"/></svg>');
            background-size: cover;
            background-position: center;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            margin-top: 70px;
        }

        .hero-overlay {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.4);
        }

        .hero-content {
            position: relative;
            z-index: 10;
            text-align: center;
            color: white;
            max-width: 800px;
            padding: 0 40px;
        }

        .hero-title {
            font-size: 4.5rem;
            font-weight: 300;
            margin-bottom: 30px;
            line-height: 1.1;
            letter-spacing: -1px;
        }

        .hero-description {
            font-size: 1.4rem;
            margin-bottom: 40px;
            opacity: 0.95;
            line-height: 1.6;
            font-weight: 300;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }

        .hero-cta {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 18px 40px;
            background: transparent;
            border: 2px solid rgba(255, 255, 255, 0.8);
            color: white;
            text-decoration: none;
            font-weight: 500;
            letter-spacing: 0.5px;
            transition: all 0.3s ease;
            border-radius: 5px;
            text-transform: uppercase;
            font-size: 0.9rem;
        }

        .hero-cta:hover {
            background: rgba(255, 255, 255, 0.15);
            border-color: rgba(255, 255, 255, 1);
        }

        /* Mega Menu Styles */
        .mega-menu {
            position: absolute;
            top: 100%;
            left: 50%;
            transform: translateX(-50%);
            width: 100vw;
            background: white;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            padding: 60px 40px;
            z-index: 999;
        }

        .nav-item:hover .mega-menu {
            opacity: 1;
            visibility: visible;
        }

        .mega-menu-content {
            max-width: 1400px;
            margin: 0 auto;
        }

        /* Machines Mega Menu */
        .machines-menu .mega-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 40px;
        }

        .mega-card {
            text-align: center;
            transition: transform 0.3s ease;
            cursor: pointer;
        }

        .mega-card:hover {
            transform: translateY(-5px);
        }

        .mega-card-image {
            width: 100%;
            height: 200px;
            background-size: cover;
            background-position: center;
            border-radius: 8px;
            margin-bottom: 20px;
        }

        .office-coffee-img {
            background: linear-gradient(45deg, #8b7355 0%, #a68b5b 100%);
        }

        .commercial-img {
            background: linear-gradient(45deg, #5a7a4a 0%, #6b8e5a 100%);
        }

        .filtered-water-img {
            background: linear-gradient(45deg, #4a6b7a 0%, #5a7b8a 100%);
        }

        .mega-card-title {
            font-size: 1.5rem;
            color: #2c1810;
            margin-bottom: 10px;
            font-weight: 400;
        }

        .mega-card-arrow {
            color: #6b8e5a;
            font-size: 1.2rem;
            margin-left: 8px;
        }

        /* Shop Mega Menu */
        .shop-menu .mega-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 40px;
        }

        .coffee-img {
            background: linear-gradient(45deg, #6b4423 0%, #8b5a2b 100%);
        }

        .tea-img {
            background: linear-gradient(45deg, #5a7a4a 0%, #6b8e5a 100%);
        }

        .shop-all-content {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: flex-start;
            padding: 40px;
            height: 200px;
            background: #f8f6f3;
            border-radius: 8px;
        }

        .shop-menu-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
            padding: 12px 0;
            color: #4a4a4a;
            text-decoration: none;
            font-weight: 500;
            border-bottom: 1px solid #e0e0e0;
            transition: color 0.3s ease;
        }

        .shop-menu-item:hover {
            color: #6b4423;
        }

        .shop-menu-item:last-child {
            border-bottom: none;
        }

        /* Coffee Mega Menu */
        .coffee-menu {
            background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 400"><rect width="1400" height="400" fill="%232c1810"/><circle cx="1100" cy="200" r="80" fill="%23f4f1ed" opacity="0.3"/><rect x="1050" y="150" width="100" height="100" rx="50" fill="%236b4423"/></svg>');
            background-size: cover;
            background-position: center;
            color: white;
        }

        .coffee-menu .mega-menu-content {
            text-align: center;
        }

        .coffee-menu .hero-title {
            color: white;
            margin-bottom: 20px;
        }

        .coffee-menu .hero-description {
            color: rgba(255, 255, 255, 0.9);
            margin-bottom: 30px;
        }

        .coffee-menu .hero-cta {
            background: transparent;
            border: 2px solid rgba(255, 255, 255, 0.8);
            color: white;
        }

        /* About Mega Menu */
        .about-menu .mega-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 40px;
        }

        .story-img {
            background: linear-gradient(45deg, #6b4423 0%, #8b5a2b 100%);
        }

        .environment-img {
            background: linear-gradient(45deg, #5a7a4a 0%, #6b8e5a 100%);
        }

        .news-img {
            background: linear-gradient(45deg, #4a6b7a 0%, #5a7b8a 100%);
        }

        /* Trustpilot */
        .trustpilot {
            position: absolute;
            bottom: 40px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
        }

        .trustpilot-logo {
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.4rem;
            font-weight: 600;
        }

        .stars {
            display: flex;
            gap: 3px;
        }

        .star {
            width: 18px;
            height: 18px;
            background: #00b67a;
            clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
        }

        /* Services Section (Scroll Down Section) */
        .services-section {
            min-height: 100vh;
            background: #f8f6f3;
            padding: 80px 40px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .services-container {
            max-width: 1400px;
            width: 100%;
        }

        .services-header {
            text-align: center;
            margin-bottom: 80px;
        }

        .services-title {
            font-size: 3.5rem;
            color: #2c1810;
            margin-bottom: 20px;
            font-weight: 300;
            letter-spacing: -1px;
        }

        .services-subtitle {
            font-size: 1.3rem;
            color: #6b5c47;
            font-weight: 300;
        }

        .services-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 40px;
            max-width: 1200px;
            margin: 0 auto;
        }

        .service-card {
            position: relative;
            overflow: hidden;
            cursor: pointer;
            transition: transform 0.4s ease;
            display: flex;
            align-items: flex-end;
            padding: 50px;
            border-radius: 12px;
            height: 400px;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
        }

        .service-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.15);
        }

        .coffee-card {
            background: linear-gradient(135deg, #f4f1ed 0%, #e8e4df 100%);
        }

        .machines-card {
            background: linear-gradient(135deg, #6b4423 0%, #5a3619 100%);
            color: white;
        }

        .shop-card {
            background: linear-gradient(135deg, #2c1810 0%, #4a3426 100%);
            color: white;
        }

        .card-content {
            position: relative;
            z-index: 10;
        }

        .card-title {
            font-size: 2.5rem;
            margin-bottom: 20px;
            font-weight: 400;
        }

        .coffee-card .card-title {
            color: #2c1810;
        }

        .card-cta {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            text-decoration: none;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-size: 0.9rem;
            transition: all 0.3s ease;
        }

        .coffee-card .card-cta {
            color: #6b4423;
        }

        .machines-card .card-cta,
        .shop-card .card-cta {
            color: rgba(255, 255, 255, 0.9);
        }

        .card-cta:hover {
            transform: translateX(5px);
        }

        .card-cta::after {
            content: '→';
            font-size: 1.3rem;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .header {
                padding: 15px 20px;
                flex-direction: column;
                gap: 15px;
            }

            .nav {
                gap: 20px;
            }

            .mega-menu {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100vh;
                padding: 80px 20px;
                overflow-y: auto;
            }

            .mega-grid {
                grid-template-columns: 1fr !important;
                gap: 30px !important;
            }

            .services-grid {
                grid-template-columns: 1fr;
                gap: 30px;
            }

            .service-card {
                height: 300px;
                padding: 40px;
            }

            .hero-title {
                font-size: 3rem;
            }

            .services-title {
                font-size: 2.5rem;
            }

            .card-title {
                font-size: 2rem;
            }

            .services-section {
                padding: 60px 20px;
            }

            .contact-side-btn {
                display: none;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <a href="/" class="logo">Office<br>Coffee<br>Co.</a>
        <nav class="nav">
            <div class="nav-item">
                <a href="/machines">Machines</a>
                <div class="mega-menu machines-menu">
                    <div class="mega-menu-content">
                        <div class="mega-grid">
                            <div class="mega-card" onclick="location.href='/machines'">
                                <div class="mega-card-image office-coffee-img"></div>
                                <h3 class="mega-card-title">Office Coffee <span class="mega-card-arrow">→</span></h3>
                            </div>
                            <div class="mega-card" onclick="location.href='/machines'">
                                <div class="mega-card-image commercial-img"></div>
                                <h3 class="mega-card-title">Commercial <span class="mega-card-arrow">→</span></h3>
                            </div>
                            <div class="mega-card" onclick="location.href='/machines'">
                                <div class="mega-card-image filtered-water-img"></div>
                                <h3 class="mega-card-title">Filtered Water <span class="mega-card-arrow">→</span></h3>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="nav-item">
                <a href="/shop">Shop</a>
                <div class="mega-menu shop-menu">
                    <div class="mega-menu-content">
                        <div class="mega-grid">
                            <div class="mega-card" onclick="location.href='/coffee'">
                                <div class="mega-card-image coffee-img"></div>
                                <h3 class="mega-card-title">Coffee <span class="mega-card-arrow">→</span></h3>
                            </div>
                            <div class="mega-card" onclick="location.href='/shop'">
                                <div class="mega-card-image tea-img"></div>
                                <h3 class="mega-card-title">Tea <span class="mega-card-arrow">→</span></h3>
                            </div>
                            <div class="mega-card">
                                <div class="shop-all-content">
                                    <h3 class="mega-card-title" style="margin-bottom: 20px; color: #2c1810;">Shop All</h3>
                                    <a href="/shop" class="shop-menu-item">
                                        <span>SUNDRIES</span>
                                        <span>→</span>
                                    </a>
                                    <a href="/shop" class="shop-menu-item">
                                        <span>DISPOSABLES</span>
                                        <span>→</span>
                                    </a>
                                    <a href="/shop" class="shop-menu-item">
                                        <span>EQUIPMENT</span>
                                        <span>→</span>
                                    </a>
                                    <a href="/shop" class="shop-menu-item">
                                        <span>SALE</span>
                                        <span>→</span>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="nav-item">
                <a href="/coffee">Coffee</a>
                <div class="mega-menu coffee-menu">
                    <div class="mega-menu-content">
                        <h1 class="hero-title">Organise a coffee tasting for your colleagues</h1>
                        <p class="hero-description">
                            Host an obligation free coffee morning to sample our delicious blends and reliable machines
                        </p>
                        <a href="/machines" class="hero-cta">Coffee Machines</a>
                    </div>
                </div>
            </div>
            
            <div class="nav-item">
                <a href="/about">About</a>
                <div class="mega-menu about-menu">
                    <div class="mega-menu-content">
                        <div class="mega-grid">
                            <div class="mega-card" onclick="location.href='/about'">
                                <div class="mega-card-image story-img"></div>
                                <h3 class="mega-card-title">Our Story <span class="mega-card-arrow">→</span></h3>
                            </div>
                            <div class="mega-card" onclick="location.href='/about'">
                                <div class="mega-card-image environment-img"></div>
                                <h3 class="mega-card-title">Environment <span class="mega-card-arrow">→</span></h3>
                            </div>
                            <div class="mega-card" onclick="location.href='/about'">
                                <div class="mega-card-image news-img"></div>
                                <h3 class="mega-card-title">News <span class="mega-card-arrow">→</span></h3>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
        <div class="contact-info">
            <span>📞 0203 763 4035</span>
            <button class="contact-btn" onclick="showContactForm()">Get Quote</button>
        </div>
    </div>

    <button class="contact-side-btn" onclick="showContactForm()">CONTACT US</button>

    <div class="main-container">
        <!-- Hero Section -->
        <section class="hero-section">
            <div class="hero-overlay"></div>
            <div class="hero-content">
                <h1 class="hero-title">Delicious coffee for your office</h1>
                <p class="hero-description">
                    At the Office Coffee Company, we specialise in barista-quality machines and ethically 
                    sourced beans, for your workplace.
                </p>
                <a href="/machines" class="hero-cta">Coffee Machines</a>
            </div>
            
            <div class="trustpilot">
                <div class="trustpilot-logo">★ Trustpilot</div>
                <div class="stars">
                    <div class="star"></div>
                    <div class="star"></div>
                    <div class="star"></div>
                    <div class="star"></div>
                    <div class="star"></div>
                </div>
            </div>
        </section>

        <!-- Services Section (Appears on scroll down) -->
        <section class="services-section" id="servicesSection">
            <div class="services-container">
                <div class="services-header">
                    <h2 class="services-title">What are you looking for today?</h2>
                    <p class="services-subtitle">Professional coffee solutions tailored for your business</p>
                </div>

                <div class="services-grid">
                    <div class="service-card coffee-card" onclick="location.href='/coffee'">
                        <div class="card-content">
                            <h3 class="card-title">Our Coffee</h3>
                            <a href="/coffee" class="card-cta">Discover blends</a>
                        </div>
                    </div>

                    <div class="service-card machines-card" onclick="location.href='/machines'">
                        <div class="card-content">
                            <h3 class="card-title">Our Machines</h3>
                            <a href="/machines" class="card-cta">Find equipment</a>
                        </div>
                    </div>

                    <div class="service-card shop-card" onclick="location.href='/shop'">
                        <div class="card-content">
                            <h3 class="card-title">Coffee Shop</h3>
                            <a href="/shop" class="card-cta">Buy supplies</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>

    <script>
        // Contact form function
        function showContactForm() {
            const modal = document.createElement('div');
            modal.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.8);
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 2000;
            `;
            
            modal.innerHTML = `
                <div style="background: white; padding: 40px; border-radius: 12px; max-width: 500px; width: 90%;">
                    <h3 style="margin-bottom: 20px; color: #2c1810;">Get Your Free Quote</h3>
                    <form onsubmit="handleContactSubmit(event)">
                        <input type="text" placeholder="Company Name" required style="width: 100%; padding: 12px; margin-bottom: 15px; border: 1px solid #ddd; border-radius: 6px;">
                        <input type="email" placeholder="Email Address" required style="width: 100%; padding: 12px; margin-bottom: 15px; border: 1px solid #ddd; border-radius: 6px;">
                        <input type="tel" placeholder="Phone Number" style="width: 100%; padding: 12px; margin-bottom: 15px; border: 1px solid #ddd; border-radius: 6px;">
                        <textarea placeholder="Tell us about your requirements..." rows="4" style="width: 100%; padding: 12px; margin-bottom: 20px; border: 1px solid #ddd; border-radius: 6px; resize: vertical;"></textarea>
                        <div style="display: flex; gap: 15px;">
                            <button type="submit" style="flex: 1; padding: 12px; background: #6b4423; color: white; border: none; border-radius: 6px; cursor: pointer;">Send Quote Request</button>
                            <button type="button" onclick="this.closest('div').parentElement.remove()" style="padding: 12px 20px; background: #ccc; color: #333; border: none; border-radius: 6px; cursor: pointer;">Cancel</button>
                        </div>
                    </form>
                </div>
            `;
            
            document.body.appendChild(modal);
        }

        function handleContactSubmit(event) {
            event.preventDefault();
            alert('Thank you! We will contact you within 24 hours with your personalized quote.');
            event.target.closest('div').parentElement.remove();
        }

        // Smooth scroll to services
        function scrollToServices() {
            document.getElementById('servicesSection').scrollIntoView({
                behavior: 'smooth'
            });
        }

        // Handle mega menu interactions
        document.addEventListener('DOMContentLoaded', function() {
            const navItems = document.querySelectorAll('.nav-item');
            
            navItems.forEach(item => {
                const link = item.querySelector('a');
                const menu = item.querySelector('.mega-menu');
                
                if (menu) {
                    let hoverTimeout;
                    
                    item.addEventListener('mouseenter', () => {
                        clearTimeout(hoverTimeout);
                        menu.style.opacity = '1';
                        menu.style.visibility = 'visible';
                    });
                    
                    item.addEventListener('mouseleave', () => {
                        hoverTimeout = setTimeout(() => {
                            menu.style.opacity = '0';
                            menu.style.visibility = 'hidden';
                        }, 100);
                    });
                }
            });
        });
    </script>
</body>
</html>
'''

# Coffee page template (simplified)
COFFEE_PAGE_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Our Coffee - Office Coffee Co.</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #f8f6f3 0%, #e8e4df 100%);
            min-height: 100vh;
        }
        
        .header {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            padding: 20px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
        }
        
        .logo { 
            font-size: 1.8rem; 
            font-weight: 700; 
            color: #2c1810; 
            text-decoration: none; 
            line-height: 1.2;
        }
        
        .container {
            max-width: 1200px;
            margin: 60px auto;
            padding: 0 40px;
        }
        
        .hero {
            text-align: center;
            margin-bottom: 80px;
        }
        
        .hero h1 {
            font-size: 4rem;
            color: #2c1810;
            margin-bottom: 20px;
            font-weight: 300;
            letter-spacing: -1px;
        }
        
        .hero p {
            font-size: 1.3rem;
            color: #6b5c47;
            max-width: 600px;
            margin: 0 auto;
            line-height: 1.6;
        }
        
        .coffee-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 40px;
            margin-bottom: 60px;
        }
        
        .coffee-card {
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        
        .coffee-card:hover { transform: translateY(-5px); }
        
        .coffee-image {
            height: 200px;
            background: linear-gradient(45deg, #6b4423, #8b5a2b);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3rem;
            color: white;
        }
        
        .coffee-content {
            padding: 30px;
        }
        
        .coffee-title {
            font-size: 1.8rem;
            color: #2c1810;
            margin-bottom: 15px;
            font-weight: 500;
        }
        
        .coffee-description {
            color: #6b5c47;
            line-height: 1.6;
            margin-bottom: 20px;
        }
        
        .coffee-price {
            font-size: 1.3rem;
            color: #6b4423;
            font-weight: 600;
        }
        
        .back-link {
            display: inline-block;
            padding: 15px 30px;
            background: #6b4423;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 500;
            transition: background 0.3s ease;
            margin-top: 40px;
        }
        
        .back-link:hover { background: #5a3619; }
        
        @media (max-width: 768px) {
            .hero h1 { font-size: 2.5rem; }
            .container { padding: 0 20px; }
            .coffee-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <div class="header">
        <a href="/" class="logo">Office<br>Coffee<br>Co.</a>
    </div>
    
    <div class="container">
        <div class="hero">
            <h1>Our Premium Coffee</h1>
            <p>Discover our carefully curated selection of premium coffee blends, sourced from the finest coffee farms around the world and roasted to perfection for your office.</p>
        </div>
        
        <div class="coffee-grid">
            <div class="coffee-card">
                <div class="coffee-image">☕</div>
                <div class="coffee-content">
                    <h3 class="coffee-title">Executive Blend</h3>
                    <p class="coffee-description">A rich, full-bodied blend perfect for morning meetings. Notes of dark chocolate and caramel with a smooth finish.</p>
                    <div class="coffee-price">From £24.99/kg</div>
                </div>
            </div>
            
            <div class="coffee-card">
                <div class="coffee-image">🫘</div>
                <div class="coffee-content">
                    <h3 class="coffee-title">Morning Boost</h3>
                    <p class="coffee-description">High-caffeine blend designed to kickstart your day. Bold flavor with hints of nuts and citrus.</p>
                    <div class="coffee-price">From £22.99/kg</div>
                </div>
            </div>
            
            <div class="coffee-card">
                <div class="coffee-image">🌱</div>
                <div class="coffee-content">
                    <h3 class="coffee-title">Eco Friendly</h3>
                    <p class="coffee-description">Sustainably sourced, organic coffee blend. Light and refreshing with floral notes and bright acidity.</p>
                    <div class="coffee-price">From £28.99/kg</div>
                </div>
            </div>
            
            <div class="coffee-card">
                <div class="coffee-image">🔥</div>
                <div class="coffee-content">
                    <h3 class="coffee-title">Afternoon Decaf</h3>
                    <p class="coffee-description">Premium decaffeinated blend that doesn't compromise on taste. Perfect for afternoon coffee breaks.</p>
                    <div class="coffee-price">From £26.99/kg</div>
                </div>
            </div>
        </div>
        
        <div style="text-align: center;">
            <a href="/" class="back-link">← Back to Home</a>
        </div>
    </div>
</body>
</html>
'''

# Machines page template
MACHINES_PAGE_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Our Machines - Office Coffee Co.</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #2c1810 0%, #4a3426 100%);
            min-height: 100vh;
            color: white;
        }
        
        .header {
            background: rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(10px);
            padding: 20px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo { 
            font-size: 1.8rem; 
            font-weight: 700; 
            color: white; 
            text-decoration: none; 
            line-height: 1.2;
        }
        
        .container {
            max-width: 1200px;
            margin: 60px auto;
            padding: 0 40px;
        }
        
        .hero {
            text-align: center;
            margin-bottom: 80px;
        }
        
        .hero h1 {
            font-size: 4rem;
            margin-bottom: 20px;
            font-weight: 300;
            letter-spacing: -1px;
        }
        
        .hero p {
            font-size: 1.3rem;
            opacity: 0.9;
            max-width: 600px;
            margin: 0 auto;
            line-height: 1.6;
        }
        
        .machines-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 40px;
            margin-bottom: 60px;
        }
        
        .machine-card {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            overflow: hidden;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: transform 0.3s ease;
        }
        
        .machine-card:hover { transform: translateY(-5px); }
        
        .machine-image {
            height: 200px;
            background: rgba(255, 255, 255, 0.2);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3rem;
        }
        
        .machine-content {
            padding: 30px;
        }
        
        .machine-title {
            font-size: 1.8rem;
            margin-bottom: 15px;
            font-weight: 500;
        }
        
        .machine-description {
            opacity: 0.9;
            line-height: 1.6;
            margin-bottom: 20px;
        }
        
        .machine-features {
            list-style: none;
            margin-bottom: 20px;
        }
        
        .machine-features li {
            padding: 5px 0;
            opacity: 0.8;
        }
        
        .machine-features li::before {
            content: '✓ ';
            color: #4CAF50;
            font-weight: bold;
        }
        
        .machine-price {
            font-size: 1.3rem;
            color: #4CAF50;
            font-weight: 600;
        }
        
        .back-link {
            display: inline-block;
            padding: 15px 30px;
            background: rgba(255, 255, 255, 0.2);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 500;
            transition: background 0.3s ease;
            margin-top: 40px;
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
        
        .back-link:hover { background: rgba(255, 255, 255, 0.3); }
        
        @media (max-width: 768px) {
            .hero h1 { font-size: 2.5rem; }
            .container { padding: 0 20px; }
            .machines-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <div class="header">
        <a href="/" class="logo">Office<br>Coffee<br>Co.</a>
    </div>
    
    <div class="container">
        <div class="hero">
            <h1>Professional Coffee Machines</h1>
            <p>State-of-the-art coffee machines designed for office environments. Reliable, efficient, and easy to use for teams of any size.</p>
        </div>
        
        <div class="machines-grid">
            <div class="machine-card">
                <div class="machine-image">⚙️</div>
                <div class="machine-content">
                    <h3 class="machine-title">Office Pro 2000</h3>
                    <p class="machine-description">Perfect for small to medium offices. Makes up to 200 cups per day with consistent quality.</p>
                    <ul class="machine-features">
                        <li>Bean-to-cup technology</li>
                        <li>Touch screen interface</li>
                        <li>Self-cleaning function</li>
                        <li>Energy efficient</li>
                    </ul>
                    <div class="machine-price">From £45/month</div>
                </div>
            </div>
            
            <div class="machine-card">
                <div class="machine-image">🏢</div>
                <div class="machine-content">
                    <h3 class="machine-title">Corporate Elite</h3>
                    <p class="machine-description">Heavy-duty machine for large offices. Handles 500+ cups daily with multiple drink options.</p>
                    <ul class="machine-features">
                        <li>Multiple coffee varieties</li>
                        <li>Hot chocolate & tea options</li>
                        <li>Advanced grinder system</li>
                        <li>Remote monitoring</li>
                    </ul>
                    <div class="machine-price">From £89/month</div>
                </div>
            </div>
            
            <div class="machine-card">
                <div class="machine-image">☕</div>
                <div class="machine-content">
                    <h3 class="machine-title">Compact Express</h3>
                    <p class="machine-description">Space-saving solution for smaller teams. Great coffee quality in a compact design.</p>
                    <ul class="machine-features">
                        <li>Small footprint</li>
                        <li>Quick brewing</li>
                        <li>Easy maintenance</li>
                        <li>Affordable option</li>
                    </ul>
                    <div class="machine-price">From £29/month</div>
                </div>
            </div>
            
            <div class="machine-card">
                <div class="machine-image">🌟</div>
                <div class="machine-content">
                    <h3 class="machine-title">Premium Series</h3>
                    <p class="machine-description">Top-of-the-line machine with barista-quality results. Perfect for executive floors.</p>
                    <ul class="machine-features">
                        <li>Barista-quality espresso</li>
                        <li>Milk frothing system</li>
                        <li>Premium materials</li>
                        <li>White glove service</li>
                    </ul>
                    <div class="machine-price">From £125/month</div>
                </div>
            </div>
        </div>
        
        <div style="text-align: center;">
            <a href="/" class="back-link">← Back to Home</a>
        </div>
    </div>
</body>
</html>
'''

# Shop page template
SHOP_PAGE_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coffee Shop - Office Coffee Co.</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f8f6f3;
            min-height: 100vh;
        }
        
        .header {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            padding: 20px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
        }
        
        .logo { 
            font-size: 1.8rem; 
            font-weight: 700; 
            color: #2c1810; 
            text-decoration: none; 
            line-height: 1.2;
        }
        
        .container {
            max-width: 1200px;
            margin: 60px auto;
            padding: 0 40px;
        }
        
        .hero {
            text-align: center;
            margin-bottom: 80px;
        }
        
        .hero h1 {
            font-size: 4rem;
            color: #2c1810;
            margin-bottom: 20px;
            font-weight: 300;
            letter-spacing: -1px;
        }
        
        .hero p {
            font-size: 1.3rem;
            color: #6b5c47;
            max-width: 600px;
            margin: 0 auto;
            line-height: 1.6;
        }
        
        .categories {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-bottom: 60px;
        }
        
        .category-card {
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
            cursor: pointer;
        }
        
        .category-card:hover { transform: translateY(-5px); }
        
        .category-image {
            height: 180px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3rem;
            color: white;
        }
        
        .coffee-supplies { background: linear-gradient(45deg, #6b4423, #8b5a2b); }
        .accessories { background: linear-gradient(45deg, #2c1810, #4a3426); }
        .maintenance { background: linear-gradient(45deg, #5a7a4a, #6b8e5a); }
        
        .category-content {
            padding: 30px;
        }
        
        .category-title {
            font-size: 1.8rem;
            color: #2c1810;
            margin-bottom: 15px;
            font-weight: 500;
        }
        
        .category-description {
            color: #6b5c47;
            line-height: 1.6;
            margin-bottom: 20px;
        }
        
        .category-items {
            list-style: none;
        }
        
        .category-items li {
            padding: 8px 0;
            color: #6b5c47;
            border-bottom: 1px solid #f0f0f0;
        }
        
        .category-items li:last-child {
            border-bottom: none;
        }
        
        .back-link {
            display: inline-block;
            padding: 15px 30px;
            background: #6b4423;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 500;
            transition: background 0.3s ease;
            margin-top: 40px;
        }
        
        .back-link:hover { background: #5a3619; }
        
        @media (max-width: 768px) {
            .hero h1 { font-size: 2.5rem; }
            .container { padding: 0 20px; }
            .categories { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <div class="header">
        <a href="/" class="logo">Office<br>Coffee<br>Co.</a>
    </div>
    
    <div class="container">
        <div class="hero">
            <h1>Coffee Shop</h1>
            <p>Everything you need to maintain your perfect office coffee experience. From premium supplies to essential accessories.</p>
        </div>
        
        <div class="categories">
            <div class="category-card">
                <div class="category-image coffee-supplies">☕</div>
                <div class="category-content">
                    <h3 class="category-title">Coffee & Supplies</h3>
                    <p class="category-description">Premium coffee beans, filters, and essential supplies for your machines.</p>
                    <ul class="category-items">
                        <li>Coffee Beans (Various Blends)</li>
                        <li>Paper Filters</li>
                        <li>Cleaning Tablets</li>
                        <li>Descaling Solution</li>
                        <li>Milk Powder</li>
                    </ul>
                </div>
            </div>
            
            <div class="category-card">
                <div class="category-image accessories">🔧</div>
                <div class="category-content">
                    <h3 class="category-title">Accessories</h3>
                    <p class="category-description">Professional accessories to enhance your coffee experience.</p>
                    <ul class="category-items">
                        <li>Branded Coffee Cups</li>
                        <li>Stirrers & Napkins</li>
                        <li>Sugar & Sweeteners</li>
                        <li>Cup Dispensers</li>
                        <li>Waste Bins</li>
                    </ul>
                </div>
            </div>
            
            <div class="category-card">
                <div class="category-image maintenance">🛠️</div>
                <div class="category-content">
                    <h3 class="category-title">Maintenance</h3>
                    <p class="category-description">Keep your machines running smoothly with our maintenance packages.</p>
                    <ul class="category-items">
                        <li>Monthly Service Plans</li>
                        <li>Emergency Repairs</li>
                        <li>Replacement Parts</li>
                        <li>Technical Support</li>
                        <li>Training Sessions</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <div style="text-align: center;">
            <a href="/" class="back-link">← Back to Home</a>
        </div>
    </div>
</body>
</html>
'''

# About page template
ABOUT_PAGE_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us - Office Coffee Co.</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #f8f6f3 0%, #e8e4df 100%);
            min-height: 100vh;
        }
        
        .header {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            padding: 20px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
        }
        
        .logo { 
            font-size: 1.8rem; 
            font-weight: 700; 
            color: #2c1810; 
            text-decoration: none; 
            line-height: 1.2;
        }
        
        .container {
            max-width: 1000px;
            margin: 60px auto;
            padding: 0 40px;
        }
        
        .hero {
            text-align: center;
            margin-bottom: 80px;
        }
        
        .hero h1 {
            font-size: 4rem;
            color: #2c1810;
            margin-bottom: 20px;
            font-weight: 300;
            letter-spacing: -1px;
        }
        
        .hero p {
            font-size: 1.3rem;
            color: #6b5c47;
            max-width: 700px;
            margin: 0 auto;
            line-height: 1.6;
        }
        
        .content {
            background: white;
            border-radius: 12px;
            padding: 60px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            margin-bottom: 40px;
        }
        
        .content h2 {
            font-size: 2.2rem;
            color: #2c1810;
            margin-bottom: 30px;
            font-weight: 400;
        }
        
        .content p {
            font-size: 1.1rem;
            color: #6b5c47;
            line-height: 1.8;
            margin-bottom: 25px;
        }
        
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 40px;
            margin: 50px 0;
        }
        
        .stat {
            text-align: center;
        }
        
        .stat-number {
            font-size: 3rem;
            color: #6b4423;
            font-weight: 600;
            display: block;
        }
        
        .stat-label {
            color: #6b5c47;
            font-size: 1.1rem;
            margin-top: 10px;
        }
        
        .back-link {
            display: inline-block;
            padding: 15px 30px;
            background: #6b4423;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 500;
            transition: background 0.3s ease;
            margin-top: 40px;
        }
        
        .back-link:hover { background: #5a3619; }
        
        @media (max-width: 768px) {
            .hero h1 { font-size: 2.5rem; }
            .container { padding: 0 20px; }
            .content { padding: 40px 30px; }
        }
    </style>
</head>
<body>
    <div class="header">
        <a href="/" class="logo">Office<br>Coffee<br>Co.</a>
    </div>
    
    <div class="container">
        <div class="hero">
            <h1>About Office Coffee Co.</h1>
            <p>Transforming office coffee culture with premium solutions, exceptional service, and unwavering commitment to quality.</p>
        </div>
        
        <div class="content">
            <h2>Our Story</h2>
            <p>Office Coffee Co. was founded with a simple mission: to bring exceptional coffee experiences to workplaces across the UK. We understand that great coffee fuels great work, and we're passionate about providing businesses with the tools and expertise they need to create the perfect coffee culture.</p>
            
            <p>For over a decade, we've been partnering with companies of all sizes, from small startups to large corporations, helping them discover the perfect coffee solution for their unique needs. Our team of coffee experts works closely with each client to understand their requirements and deliver customized solutions that exceed expectations.</p>
            
            <div class="stats">
                <div class="stat">
                    <span class="stat-number">500+</span>
                    <div class="stat-label">Happy Clients</div>
                </div>
                <div class="stat">
                    <span class="stat-number">10+</span>
                    <div class="stat-label">Years Experience</div>
                </div>
                <div class="stat">
                    <span class="stat-number">1M+</span>
                    <div class="stat-label">Cups Served</div>
                </div>
                <div class="stat">
                    <span class="stat-number">24/7</span>
                    <div class="stat-label">Support Available</div>
                </div>
            </div>
            
            <h2>Why Choose Us?</h2>
            <p>We pride ourselves on offering more than just coffee machines and beans. We provide complete solutions that include installation, training, maintenance, and ongoing support. Our commitment to quality means we source only the finest coffee beans and partner with leading machine manufacturers to ensure reliability and consistency.</p>
            
            <p>Our team understands that every office is different, which is why we offer personalized consultations and tastings to help you find the perfect match for your team's preferences and your business requirements.</p>
        </div>
        
        <div style="text-align: center;">
            <a href="/" class="back-link">← Back to Home</a>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(MAIN_TEMPLATE)

@app.route('/coffee')
def coffee():
    return render_template_string(COFFEE_PAGE_TEMPLATE)

@app.route('/machines')
def machines():
    return render_template_string(MACHINES_PAGE_TEMPLATE)

@app.route('/shop')
def shop():
    return render_template_string(SHOP_PAGE_TEMPLATE)

@app.route('/about')
def about():
    return render_template_string(ABOUT_PAGE_TEMPLATE)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
