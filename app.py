import streamlit as st

# Set page configuration
st.set_page_config(page_title="Stunning Website", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    /* Custom Navigation Bar */
    .navbar {
        background-color: black;
        padding: 10px;
        border-radius: 10px;
    }
    .navbar a {
        color: white;
        padding: 14px 20px;
        text-decoration: none;
        font-size: 18px;
    }
    .navbar a:hover {
        background-color: #45a049;
        color: white;
        border-radius: 5px;
    }
    /* Hero Section */
    .hero {
        position: relative;
        background-image: url('https://thumbs.dreamstime.com/b/fairy-tale-landscape-wonderful-illustration-roses-castle-48313207.jpg');
        background-size: cover;
        text-align: center;
        padding: 100px 20px;
        border-radius: 10px;
    }
    .hero::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
        border-radius: 10px;
    }
    .hero h1, .hero p {
        position: relative;
        z-index: 1;
        color: white;
    }
    .hero h1 {
        font-size: 72px;
        margin-bottom: 10px;
    }
    .hero p {
        font-size: 24px;
    }
    /* Services Section */
    .services {
        display: flex;
        justify-content: center;
        gap: 30px;
        padding: 50px 0;
    }
    .card {
        background-color: #f1f1f1;
        padding: 20px;
        width: 300px;
        text-align: center;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        overflow: hidden;
    }
    .card img {
        width: 100%;
        height: auto;
        border-radius: 10px 10px 0 0;
    }
    .card h3 {
        color: #333;
        margin: 15px 0;
    }
    .card p {
        color: #777;
        padding: 0 10px;
    }
    .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }
    /* Footer */
    footer {
        background-color: black;
        color: white;
        padding: 40px 20px;
        border-radius: 10px;
        margin-top: 50px;
    }
    .footer-columns {
        display: flex;
        justify-content: space-around;
        text-align: left;
    }
    .footer-column h4 {
        margin-bottom: 15px;
          color: white;
    }
    .footer-column a {
        color: white;
        text-decoration: none;
        display: block;
        margin-bottom: 10px;
        font-size: 16px;
    }
    .footer-column a:hover {
        text-decoration: underline;
    }
    .footer-bottom {
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation bar
st.markdown("""
<nav class="navbar">
    <a href="#home">Home</a>
    <a href="#about">About</a>
    <a href="#services">Services</a>
    <a href="#contact">Contact</a>
</nav>
""", unsafe_allow_html=True)

# Hero section
st.markdown("""
<div id="home" class="hero">
    <h1>Welcome to Our Stunning Website</h1>
    <p>Crafted with love and passion for design</p>
</div>
""", unsafe_allow_html=True)

# About section
st.markdown("""
<div id="about" style="padding: 50px 0; text-align: center;">
    <h2>About Us</h2>
    <p>We specialize in creating visually stunning and highly functional websites that captivate your audience and deliver results.</p>
</div>
""", unsafe_allow_html=True)

# Services section
st.markdown("""
<div id="services" class="services">
    <div class="card">
        <img src="https://media.licdn.com/dms/image/v2/C4D1BAQHL2C6UD_m3WA/company-background_10000/company-background_10000/0/1630993173464/it_services_india_cover?e=2147483647&v=beta&t=zmqoqiPmrBOw2nV0dMhGHeGWoPIuFZJEa9O4BkyGQps" alt="Web Design">
        <h3>Web Design</h3>
        <p>Creating beautiful, user-friendly designs that keep visitors engaged.</p>
    </div>
    <div class="card">
        <img src="https://www.khanzadaitservicesest.com/img/Software-IT-Services-PNG-Picture.png" alt="Web Development">
        <h3>Web Development</h3>
        <p>Building fast, responsive websites with the latest technologies.</p>
    </div>
    <div class="card">
        <img src="https://quasa.io/storage/images/news/yUJWI6j3EVtTC2Y72ozNHuPNfL8nYxxQQq4V3eLS.jpg" alt="SEO Optimization">
        <h3>SEO Optimization</h3>
        <p>Improving your website's visibility on search engines.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Contact section
st.markdown("""
<div id="contact" style="padding: 50px 0; text-align: center;">
    <h2>Contact Us</h2>
    <p>Email: contact@stunningwebsite.com</p>
    <p>Phone: (123) 456-7890</p>
</div>
""", unsafe_allow_html=True)

# Footer section
st.markdown("""
<footer>
    <div class="footer-columns">
        <div class="footer-column">
            <h4>About</h4>
            <a href="#about">Who We Are</a>
            <a href="#services">What We Do</a>
            <a href="#contact">Contact Us</a>
        </div>
        <div class="footer-column">
            <h4>Services</h4>
            <a href="#services">Web Design</a>
            <a href="#services">Web Development</a>
            <a href="#services">SEO Optimization</a>
        </div>
        <div class="footer-column">
            <h4>Follow Us</h4>
            <a href="#">Facebook</a>
            <a href="#">Twitter</a>
            <a href="#">LinkedIn</a>
        </div>
    </div>
    <div class="footer-bottom">
        <p>&copy; 2024 Stunning Website. All rights reserved.</p>
    </div>
</footer>
""", unsafe_allow_html=True)

# import streamlit as st

# st.title("Hello, Streamlit!")
# st.write("This is a simple Streamlit app.")

# number = st.slider("Pick a number", 0, 100)
# st.write(f"The square of {number} is {number ** 2}.")
