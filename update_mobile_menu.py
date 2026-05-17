import glob
import re

html_files = glob.glob('*.html')

old_css = r""".nav-links\{
    display:flex !important;
    position:fixed;top:56px;left:0;right:0;
    background:var\(--navy\);flex-direction:column;padding:2rem;
    gap:1\.5rem;align-items:flex-start;transform:translateY\(-150%\);
    transition:transform 0\.3s ease;border-top:1px solid rgba\(255,255,255,0\.1\);
    z-index:98;
  \}
  \.nav-links\.active\{transform:translateY\(0\);\}
  \.nav-links li\{width:100%;\}
  \.mega-menu\{display:none !important;\}
  \.nav-tel\{display:none\}"""

new_css = """.nav-links{
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

count = 0
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We use re.sub with carefully escaped old_css. But it's easier to just do string replace if we know the exact string.
    # Let's try exact string replace first.
    exact_old = """  .nav-links{
    display:flex !important;
    position:fixed;top:56px;left:0;right:0;
    background:var(--navy);flex-direction:column;padding:2rem;
    gap:1.5rem;align-items:flex-start;transform:translateY(-150%);
    transition:transform 0.3s ease;border-top:1px solid rgba(255,255,255,0.1);
    z-index:98;
  }
  .nav-links.active{transform:translateY(0);}
  .nav-links li{width:100%;}
  .mega-menu{display:none !important;}
  .nav-tel{display:none}"""
  
    if exact_old in content:
        new_content = content.replace(exact_old, new_css)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        count += 1
        print(f"Updated {f}")
    else:
        # Fallback to regex if whitespace differs slightly
        new_content, n = re.subn(old_css.replace(' ', r'\s*').replace('\n', r'\s*'), new_css, content)
        if n > 0:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            count += 1
            print(f"Updated {f} (via regex)")

print(f"Total files updated: {count}")
