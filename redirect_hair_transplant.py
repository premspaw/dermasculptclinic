import glob

html_files = glob.glob('*.html')
count = 0

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    modified = False
    
    # Replace href link targets
    if 'href="hair-transplant-jayanagar.html"' in content:
        content = content.replace('href="hair-transplant-jayanagar.html"', 'href="https://dermasculptclinic.in/"')
        modified = True
        
    # Replace onclick actions (like cards)
    if "onclick=\"location.href='hair-transplant-jayanagar.html'\"" in content:
        content = content.replace("onclick=\"location.href='hair-transplant-jayanagar.html'\"", "onclick=\"location.href='https://dermasculptclinic.in/'\"")
        modified = True
        
    if modified:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated hair transplant links in {f}")
        count += 1
    else:
        print(f"No hair transplant links found to update in {f}")

print(f"Successfully redirected hair transplant links in {count} files!")
