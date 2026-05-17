import glob
import re

# Read index.html to extract the nav HTML
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract <nav>...</nav>
nav_match = re.search(r'(<nav>.*?</nav>)', index_content, re.DOTALL)
if not nav_match:
    print("Could not find <nav> in index.html")
    exit(1)
nav_html = nav_match.group(1)

# The missing menu-toggle CSS
menu_toggle_css = """
.menu-toggle{display:none;flex-direction:column;gap:5px;cursor:pointer;margin-left:1.5rem;}
.menu-toggle span{width:24px;height:2px;background:#fff;transition:0.3s;}
"""

# The mobile nav CSS
mobile_nav_css = """  nav{padding:0 1rem; height:56px;}
  .nav-brand{gap:0.4rem}
  .nav-logo-mark{width:32px;height:32px;}
  .nav-name{font-size:1.1rem !important;}
  .nav-name span{font-size:0.75rem !important;}
  .menu-toggle{display:flex;}
  .nav-links{
    display:flex !important;
    position:fixed;top:56px;left:0;right:0;bottom:0;
    background:var(--navy);flex-direction:column;padding:1.5rem 2rem 5rem 2rem;
    gap:1.5rem;align-items:flex-start;transform:translateY(-150%);
    transition:transform 0.3s ease;border-top:1px solid rgba(255,255,255,0.1);
    z-index:98; overflow-y:auto;
  }
  .nav-links.active{transform:translateY(0);}
  .nav-links li{width:100%;}
  .mega-menu{
    display:block !important; position:static; box-shadow:none; 
    padding:0.5rem 0 0 1rem; background:transparent; 
    opacity:1; visibility:visible; pointer-events:auto; transform:none;
  }
  .mega-inner{grid-template-columns:1fr; padding:0; gap:1rem;}
  .mega-branding{display:none;}
  .mega-group{margin-bottom:0.5rem;}
  .mega-col-title{font-size:0.85rem; margin-bottom:0.4rem; padding-bottom:0.2rem;}
  .mega-group-label{font-size:0.65rem;}
  .mega-group a{font-size:0.8rem; padding:0.3rem 0; color:rgba(255,255,255,0.8);}
  .nav-tel{display:none}"""

html_files = glob.glob('*.html')
count = 0

for f in html_files:
    if f == 'index.html':
        continue
        
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Replace nav HTML
    content = re.sub(r'<nav>.*?</nav>', nav_html, content, flags=re.DOTALL)
    
    # Add menu-toggle CSS before @media(max-width:960px)
    if '.menu-toggle' not in content:
        content = content.replace('@media(max-width:960px){', menu_toggle_css + '\n@media(max-width:960px){')
        
    # Replace the inner page mobile nav CSS
    # Usually it's nav{padding:0 1.5rem} \n  .nav-links{display:none}
    old_mobile_nav = r"nav\{padding:0 1\.5rem\}\s*\.nav-links\{display:none\}"
    if re.search(old_mobile_nav, content):
        content = re.sub(old_mobile_nav, mobile_nav_css, content)
    else:
        # Check if we can find just the nav{...}
        old_mobile_nav2 = r"nav\{padding:[^\}]+\}\s*\.nav-links\{display:[^\}]+\}"
        content = re.sub(old_mobile_nav2, mobile_nav_css, content)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated {f}")
    count += 1

print(f"Total inner pages updated: {count}")
