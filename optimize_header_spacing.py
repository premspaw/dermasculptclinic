import glob
import re

html_files = glob.glob('*.html')
count = 0

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    modified = False
    
    # 1. Reduce nav padding from 5rem to 2rem
    # Target: padding:0 5rem; or padding:0 5rem
    if 'padding:0 5rem;' in content:
        content = content.replace('padding:0 5rem;', 'padding:0 2rem;')
        modified = True
    elif 'padding: 0 5rem;' in content:
        content = content.replace('padding: 0 5rem;', 'padding: 0 2rem;')
        modified = True
        
    # 2. Reduce nav-links gap from 1.4rem to 1rem
    if 'gap:1.4rem;' in content:
        content = content.replace('gap:1.4rem;', 'gap:1rem;')
        modified = True
    elif 'gap: 1.4rem;' in content:
        content = content.replace('gap: 1.4rem;', 'gap: 1rem;')
        modified = True
        
    # 3. Change breakpoint from 960px to 1024px
    if '@media(max-width:960px)' in content:
        content = content.replace('@media(max-width:960px)', '@media(max-width:1024px)')
        modified = True
    elif '@media (max-width: 960px)' in content:
        content = content.replace('@media (max-width: 960px)', '@media (max-width: 1024px)')
        modified = True
        
    if modified:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Optimized header spacing in {f}")
        count += 1
    else:
        print(f"No changes made in {f}")

print(f"Total optimized files: {count}")
