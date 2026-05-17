import glob
import re

html_files = glob.glob('*.html')

# Clean flat menu HTML for all pages
nav_html = """<nav>
  <div class="nav-brand" onclick="location.href='index.html'" style="cursor:pointer; display:flex; align-items:center; gap:0.5rem; white-space:nowrap;">
    <div class="nav-logo-mark"><img src="https://assets.cdn.filesafe.space/pdoJMu1QFXjGcesXGXoj/media/69eb4b63a48992f68928da0b.png" alt="Dermasculpt Logo" style="height:35px; width:auto;"></div>
    <div class="nav-name" style="font-size:1.6rem;">Dermasculpt <span>Hair &amp; Skin Clinic</span></div>
  </div>
  
  <!-- DESKTOP NAV WITH MEGA MENU -->
  <ul class="nav-links desktop-nav">
    <li class="has-mega">
      <a href="index.html#hair">Hair Treatments</a>
      <div class="mega-menu">
        <div class="mega-inner">
          <div class="mega-col">
            <div class="mega-col-title">💇 Hair Treatments</div>
            <div class="mega-group">
              <div class="mega-group-label">Hair Loss Solutions</div>
              <a href="hair-transplant-jayanagar.html">Hair Transplant (FUE/FUT)</a>
              <a href="prp-gfc-hair-loss-jayanagar.html">PRP (Platelet-Rich Plasma)</a>
              <a href="prp-gfc-hair-loss-jayanagar.html">GFC (Growth Factor Concentrate)</a>
            </div>
            <div class="mega-group">
              <div class="mega-group-label">Hair Removal</div>
              <a href="laser-hair-removal-jayanagar.html">Laser Hair Reduction</a>
            </div>
          </div>
          <div class="mega-branding">
            <h4>Best Hair Clinic<br>in Bangalore</h4>
            <p>You're making the right choice</p>
          </div>
        </div>
      </div>
    </li>
    <li class="has-mega">
      <a href="index.html#skin">Skin Texture & Acne</a>
      <div class="mega-menu">
        <div class="mega-inner">
          <div class="mega-col">
            <div class="mega-col-title">🧴 Skin Texture & Acne</div>
            <div class="mega-group">
              <div class="mega-group-label">Active Concerns</div>
              <a href="pimples-acne-treatment-jayanagar.html">Pimples and Acne</a>
            </div>
            <div class="mega-group">
              <div class="mega-group-label">Scar Revision</div>
              <a href="scars-treatment-jayanagar.html">Pimple Scars</a>
              <a href="scars-treatment-jayanagar.html">Accident & Surgical Scars</a>
            </div>
            <div class="mega-group">
              <div class="mega-group-label">Growth Removal</div>
              <a href="laser-mole-removal-jayanagar.html">Laser Mole Removal</a>
              <a href="wart-removal-jayanagar.html">Wart Removal</a>
            </div>
          </div>
          <div class="mega-branding">
            <h4>Best Skin Clinic<br>in Bangalore</h4>
            <p>You're making the right choice</p>
          </div>
        </div>
      </div>
    </li>
    <li class="has-mega">
      <a href="index.html#pigmentation">Pigmentation & Brightening</a>
      <div class="mega-menu">
        <div class="mega-inner">
          <div class="mega-col">
            <div class="mega-col-title">✨ Pigmentation & Brightening</div>
            <div class="mega-group">
              <div class="mega-group-label">Complexion</div>
              <a href="skin-lightening-jayanagar.html">Skin Lightening</a>
              <a href="pigmentation-treatment-jayanagar.html">Laser Toning</a>
            </div>
            <div class="mega-group">
              <div class="mega-group-label">Chemical Peels</div>
              <a href="pigmentation-treatment-jayanagar.html">AHA Peels</a>
              <a href="pigmentation-treatment-jayanagar.html">Yellow Peels</a>
              <a href="pigmentation-treatment-jayanagar.html">Carbon Peel</a>
            </div>
            <div class="mega-group">
              <div class="mega-group-label">Ink Removal</div>
              <a href="laser-tattoo-removal-jayanagar.html">Laser Tattoo Removal</a>
            </div>
          </div>
          <div class="mega-branding">
            <h4>Best Brightening Clinic<br>in Bangalore</h4>
            <p>You're making the right choice</p>
          </div>
        </div>
      </div>
    </li>
    <li class="has-mega">
      <a href="index.html#anti-aging">Anti-Ageing & Aesthetics</a>
      <div class="mega-menu">
        <div class="mega-inner">
          <div class="mega-col">
            <div class="mega-col-title">💉 Anti-Ageing & Aesthetics</div>
            <div class="mega-group">
              <div class="mega-group-label">Injectables</div>
              <a href="botox-dermal-fillers-jayanagar.html">Botox</a>
              <a href="botox-dermal-fillers-jayanagar.html">Dermal Fillers</a>
            </div>
            <div class="mega-group">
              <div class="mega-group-label">Skin Tightening</div>
              <a href="index.html#morpheus">Morpheus (Microneedling RF)</a>
            </div>
          </div>
          <div class="mega-branding">
            <h4>Best Aesthetics Clinic<br>in Bangalore</h4>
            <p>You're making the right choice</p>
          </div>
        </div>
      </div>
    </li>
    <li>
      <a href="pricing.html">Price List</a>
    </li>
  </ul>

  <!-- MOBILE NAV (NORMAL FLAT MENU) -->
  <ul class="mobile-nav">
    <li><a href="index.html">Home</a></li>
    <li><a href="hair-transplant-jayanagar.html">Hair Transplant</a></li>
    <li><a href="prp-gfc-hair-loss-jayanagar.html">PRP &amp; GFC Hair Loss</a></li>
    <li><a href="laser-hair-removal-jayanagar.html">Laser Hair Reduction</a></li>
    <li><a href="pimples-acne-treatment-jayanagar.html">Pimples &amp; Acne</a></li>
    <li><a href="scars-treatment-jayanagar.html">Scar Treatment</a></li>
    <li><a href="skin-lightening-jayanagar.html">Skin Lightening</a></li>
    <li><a href="botox-dermal-fillers-jayanagar.html">Botox &amp; Fillers</a></li>
    <li><a href="pricing.html" style="color:var(--mint); font-weight:700;">💰 Price List</a></li>
  </ul>

  <div class="nav-right" style="display:flex;align-items:center">
    <button class="btn-nav btn-book" onclick="window.open('https://link.dermasculptclinic.in/widget/booking/lrZCmPiflNmoq0yuPjp9', 'bookingPopup', 'width=600,height=800,left='+(screen.width/2-300)+',top='+(screen.height/2-400))">Book Now</button>
    <div class="menu-toggle" onclick="document.querySelector('.mobile-nav').classList.toggle('active')">
      <span></span><span></span><span></span>
    </div>
  </div>
</nav>"""

# We also want to keep the call button on index.html's mobile view as requested before.
# Let's define the homepage nav separately.
nav_html_index = nav_html.replace(
    '<!-- MOBILE NAV (NORMAL FLAT MENU) -->',
    '<!-- MOBILE NAV (NORMAL FLAT MENU) -->\n    <a href="tel:+919916906661" class="btn-nav btn-call" style="margin-right:1rem;">Call Clinic Now</a>'
)

# New CSS for mobile nav
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

count = 0
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Update <nav>...</nav>
    if f == 'index.html':
        content = re.sub(r'<nav>.*?</nav>', nav_html_index, content, flags=re.DOTALL)
    else:
        content = re.sub(r'<nav>.*?</nav>', nav_html, content, flags=re.DOTALL)
        
    # 2. Add .mobile-nav { display: none; } to the desktop styling
    if '.mobile-nav{display:none;}' not in content.replace(' ', '') and '.mobile-nav { display: none; }' not in content:
        # insert right before /* MEGA MENU */ or inside styling
        content = content.replace('/* MEGA MENU */', '.mobile-nav { display: none; }\n\n/* MEGA MENU */')
        
    # 3. Replace the mobile nav styles inside @media
    # Find the block inside @media(max-width:960px){ ... }
    # Since we previously wrote the complex menu styling, let's target that.
    target_pattern = r'\.nav-links\{\s*display:flex\s*!important;\s*position:fixed;top:56px;left:0;right:0;bottom:0;.*?\.nav-tel\{display:none\}'
    content, num_subs = re.subn(target_pattern, mobile_css_replacement, content, flags=re.DOTALL)
    
    if num_subs == 0:
        # Fallback to general block find
        target_pattern_fallback = r'\.nav-links\{\s*display:flex\s*!important;\s*position:fixed;top:56px;left:0;right:0;bottom:0;.*?\.mega-group a\{.*?\}'
        content, num_subs = re.subn(target_pattern_fallback, mobile_css_replacement, content, flags=re.DOTALL)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print(f"Updated {f}")
    count += 1

print(f"Successfully simplified mobile navigation on {count} pages!")
