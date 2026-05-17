import glob
import re

html_files = glob.glob('*.html')
count = 0

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Define canonical URL
    if f == 'index.html':
        canonical_url = 'https://www.dermasculptclinic.com/'
    else:
        canonical_url = f"https://www.dermasculptclinic.com/{f}"
        
    canonical_tag = f'\n<link rel="canonical" href="{canonical_url}">'
    
    # Let's check if the file already has a canonical tag to avoid duplicates
    if 'rel="canonical"' in content:
        print(f"Skipping {f} (already has canonical tag)")
        continue
        
    # We will insert the canonical tag right after the <title> tag
    title_pattern = r'(<title>.*?</title>)'
    if re.search(title_pattern, content):
        content = re.sub(title_pattern, rf'\1{canonical_tag}', content)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Added canonical tag to {f}: {canonical_url}")
        count += 1
    else:
        print(f"Could not find <title> tag in {f}")

print(f"Successfully injected canonical SEO tags into {count} files!")
