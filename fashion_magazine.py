import os
from flask import Flask, render_template_string, url_for

app = Flask(__name__)

# --------- sample data ---------
brands = [
    {"name": "GIANG DONNA", "img": "giang1.jpg"},
    {"name": "ARMANI", "img": "armani.jpg"},
    {"name": "GUCCI", "img": "gucci.jpg"},
    {"name": "LOUIS VUITTON", "img": "lv.jpg"},
    {"name": "PRADA", "img": "prada.jpg"},
    {"name": "BALENCIAGA", "img": "balenciaga.jpg"},
]

giang = [
    {"name": "Look 1", "img": "g1.jpg"},
    {"name": "Look 2", "img": "g2.jpg"},
    {"name": "Look 3", "img": "g3.jpg"},
    {"name": "Look 4", "img": "g4.jpg"},
    {"name": "Look 5", "img": "g5.jpg"},
    {"name": "Look 6", "img": "g6.jpg"},
]

# --------- HTML templates ---------
base_html = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{{ title or 'Black Panthers' }}</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body{font-family: "Helvetica Neue", Arial, sans-serif;background:#faf7fb;color:#222}
    .site-header{padding:12px 0;background:#f8e9e6;border-bottom:1px solid #eee}
    .logo{display:flex;align-items:center;gap:12px}
    .circle-logo{width:60px;height:60px;border-radius:50%;background:#2b2b2b;color:#fff;display:flex;align-items:center;justify-content:center;font-size:24px}
    .brand-title{font-size:22px;letter-spacing:2px}
    .nav a{margin-left:14px;color:#3b3b3b;text-decoration:none}
    .signup-card{background:#fff;border-radius:8px;box-shadow:0 6px 18px rgba(0,0,0,0.06)}
    .menu-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:16px}
    .menu-col{background:#f3eef6;padding:14px;border-radius:6px}
    .card-brand{border:3px solid #333;background:#fff}
    .card-brand img{height:220px;object-fit:cover;width:100%}
    .card-footer{background:#2e2b38;color:#fff;padding:8px;margin-top:6px;font-weight:600}
    @media (max-width:576px){
      .brand-title{font-size:16px}
      .circle-logo{width:44px;height:44px}
      .card-brand img{height:140px}
      .site-header .nav{display:none}
    }
  </style>
</head>
<body>
<header class="site-header">
  <div class="container d-flex align-items-center justify-content-between">
    <div class="logo">
      <div class="circle-logo">🐾</div>
      <div class="brand-title">BLACK PANTHERS</div>
    </div>
    <nav class="nav">
      <a href="{{ url_for('menu') }}">Menu</a>
      <a href="{{ url_for('dresses') }}">Dresses</a>
      <a href="{{ url_for('giang_donna') }}">Giang Donna</a>
    </nav>
  </div>
</header>

<main class="container my-4">
  {{ content|safe }}
</main>

<footer class="text-center py-3">
  Links to happiness
</footer>
</body>
</html>
"""

# --------- routes ---------
@app.route("/")
def index():
    content = """
    <div class="signup-card p-4 text-center">
      <h2>Sign in</h2>
      <div class="mt-3 d-grid gap-2">
        <a class="btn btn-dark btn-lg rounded-pill" href="#">Sign up with Email</a>
        <a class="btn btn-dark btn-lg rounded-pill" href="#">Sign up with Instagram</a>
        <a class="btn btn-dark btn-lg rounded-pill" href="#">Sign up with Facebook</a>
        <a class="btn btn-dark btn-lg rounded-pill" href="#">Sign up with Google</a>
      </div>
    </div>
    """
    return render_template_string(base_html, title="Sign Up", content=content)

@app.route("/menu")
def menu():
    content = """
    <div class="menu-grid">
      <div class="menu-col"><h5>Women</h5><ul><li>Dresses</li><li>Skirts</li></ul></div>
      <div class="menu-col"><h5>Men</h5><ul><li>Pants</li><li>Shoes</li></ul></div>
      <div class="menu-col"><h5>Animals</h5><ul><li>Clothes</li><li>Matching Outfits</li></ul></div>
      <div class="menu-col"><h5>Accessories</h5><ul><li>Bags</li><li>Jewelry</li></ul></div>
    </div>
    """
    return render_template_string(base_html, title="Menu", content=content)

@app.route("/dresses")
def dresses():
    cards = "".join([
        f"""
        <div class='col-6 col-md-4'>
          <div class='card card-brand h-100 text-center'>
            <img src='{url_for('static', filename='img/' + b["img"])}' alt='{b["name"]}'>
            <div class='card-footer'>{b["name"]}</div>
          </div>
        </div>
        """ for b in brands
    ])
    content = f"""
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h2>DRESSES</h2><input class="form-control w-25" placeholder="Search..."/>
    </div>
    <div class="row g-3">{cards}</div>
    <div class="text-center mt-3"><a href="#" class="small">View More</a></div>
    """
    return render_template_string(base_html, title="Dresses", content=content)

@app.route("/giang-donna")
def giang_donna():
    cards = "".join([
        f"""
        <div class='col-6 col-md-4'>
          <div class='card card-brand h-100 text-center'>
            <img src='{url_for('static', filename='img/' + i["img"])}' alt='{i["name"]}'>
            <div class='card-footer'>https://example.com</div>
          </div>
        </div>
        """ for i in giang
    ])
    content = f"""
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h2>GIANG DONNA</h2><input class="form-control w-25" placeholder="Search..."/>
    </div>
    <div class="row g-3">{cards}</div>
    <div class="text-center mt-3"><a href="#" class="small">View More</a></div>
    """
    return render_template_string(base_html, title="Giang Donna", content=content)

# --------- ensure folders ---------
os.makedirs("static/img", exist_ok=True)

if __name__ == "__main__":
    print("Running on http://127.0.0.1:5000")
    app.run(debug=True)
