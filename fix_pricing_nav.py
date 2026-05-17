import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Define the complete desktop CSS for Nav and Mega Menu
full_nav_css = """/* NAV */
nav{
  position:fixed;top:0;left:0;right:0;z-index:100;
  height:64px;display:flex;align-items:center;justify-content:space-between;
  padding:0 5rem;background:var(--navy);
}
.nav-brand{display:flex;align-items:center;gap:0.75rem;cursor:pointer}
.nav-logo-mark{width:34px;height:34px;border-radius:50%;background:var(--mint);display:flex;align-items:center;justify-content:center;font-size:0.75rem;font-weight:700;color:var(--navy)}
.nav-name{font-family:'Playfair Display',serif;font-size:1.25rem;color:#fff;font-weight:400}
.nav-name span{color:var(--mint);display:block;font-size:0.82rem;letter-spacing:0.06em;text-transform:uppercase;font-family:'Manrope',sans-serif;font-weight:600;}
.nav-links{display:flex;gap:1.4rem;list-style:none;height:100%;align-items:center}
.nav-links > li{position:static;height:100%;display:flex;align-items:center}
.nav-links a{font-size:0.68rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;color:rgba(255,255,255,0.5);text-decoration:none;transition:color 0.2s}
.nav-links a:hover{color:var(--mint)}
.btn-nav{background:var(--mint);border:none;color:var(--navy);padding:0.5rem 1.3rem;border-radius:4px;font-size:0.75rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;cursor:pointer}

.mobile-nav { display: none; }

/* MEGA MENU */
.has-mega{cursor:pointer}
.has-mega > a::after{
  content:' ▾';font-size:0.55rem;opacity:0.6;margin-left:3px;
}
.mega-menu{
  position:fixed;
  top:64px;
  left:0;right:0;
  background:var(--navy);
  border-top:1px solid rgba(255,255,255,0.07);
  border-bottom:1px solid rgba(255,255,255,0.07);
  padding:2.5rem 5rem;
  display:none;
  z-index:99;
  box-shadow:0 20px 40px rgba(0,0,0,0.35);
  animation:fadeDown 0.2s ease;
}
.mega-inner{
  max-width:1200px;
  margin:0 auto;
  display:flex;
  gap:4rem;
}
@keyframes fadeDown{from{opacity:0;transform:translateY(-8px)}to{opacity:1;transform:translateY(0)}}
.has-mega:hover .mega-menu,
.has-mega:focus-within .mega-menu{
  display:block;
}

.mega-col-title{
  font-size:0.63rem;
  font-weight:800;
  letter-spacing:0.18em;
  text-transform:uppercase;
  color:var(--mint);
  margin-bottom:1.2rem;
  padding-bottom:0.6rem;
  border-bottom:1px solid rgba(255,255,255,0.08);
}
.mega-group{margin-bottom:1.2rem}
.mega-group-label{
  font-size:0.68rem;
  font-weight:700;
  color:rgba(255,255,255,0.35);
  text-transform:uppercase;
  letter-spacing:0.1em;
  margin-bottom:0.4rem;
}
.mega-menu a{
  display:block;
  font-size:0.82rem;
  font-weight:500;
  color:rgba(255,255,255,0.6);
  text-decoration:none;
  padding:0.3rem 0;
  transition:all 0.15s;
  text-transform:none;
  letter-spacing:0;
}
.mega-menu a:hover{
  color:var(--mint);
  padding-left:6px;
}"""

# Replace the incomplete NAV block in pricing.html
content = re.sub(r'/\*\s*NAV\s*\*/.*?\.btn-nav\{[^}]*\}', full_nav_css, content, flags=re.DOTALL)

# 2. Add correct mobile media query styles for .desktop-nav and .mobile-nav
mobile_css_replacement = """  .desktop-nav { display: none !important; }
  .mobile-nav {
    display: none;
    position: fixed; top: 56px; left: 0; right: 0; bottom: 0;
    background: var(--navy); flex-direction: column; padding: 2rem;
    gap: 1.2rem; align-items: flex-start; transform: translateY(-150%);
    transition: transform 0.3s ease; border-top: 1px solid rgba(255,255,255,0.1);
    z-index: 98; overflow-y: auto;
  }
  .mobile-nav.active { transform: translateY(0); display: flex !important; }
  .mobile-nav li { width: 100%; list-style: none; }
  .mobile-nav a {
    display: block; width: 100%;
    font-size: 0.95rem; font-weight: 600; text-transform: uppercase;
    color: #fff; text-decoration: none; padding: 0.5rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    letter-spacing: 0.05em;
  }
  .mobile-nav a:hover { color: var(--mint); }"""

# Locate @media(max-width:960px){ and insert the CSS inside it
# Let's see what is inside @media(max-width:960px) in pricing.html:
# @media(max-width:960px){
#   nav, .page-header, .pricing-section, footer{padding:1.5rem}
#   ...
# }
media_block_start = '@media(max-width:960px){'
new_media_content = media_block_start + '\n' + mobile_css_replacement

content = content.replace(media_block_start, new_media_content)

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("pricing.html CSS successfully repaired!")
