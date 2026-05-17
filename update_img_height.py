import glob
import re

html_files = glob.glob('*.html')
count = 0

for f in html_files:
    if f == 'index.html':
        continue
        
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Replace .service-img-container{height:280px} with .service-img-container{height:auto} .service-img{height:auto; max-height:600px; object-fit:cover}
    
    old_css = r"\.service-img-container\{height:280px\}"
    new_css = ".service-img-container{height:auto} .service-img{height:auto; max-height:500px; object-fit:cover; object-position:center top;}"
    
    if re.search(old_css, content):
        content = re.sub(old_css, new_css, content)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
        count += 1
    else:
        print(f"No match in {f}")

print(f"Total inner pages updated: {count}")
