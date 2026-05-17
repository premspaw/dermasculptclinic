import glob

html_files = glob.glob('*.html')
count = 0

target_str = '<a href="tel:+919916906661" class="btn-nav btn-call">Call Clinic Now</a>'

for f in html_files:
    if f == 'index.html':
        print(f"Skipping index.html to keep call button on homepage mobile view.")
        continue
        
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if target_str in content:
        content = content.replace(target_str, '')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Removed call button from {f}")
        count += 1
    else:
        # Check with slight spacing variations
        import re
        content_new, n = re.subn(r'<a\s+href="tel:\+919916906661"\s+class="btn-nav\s+btn-call">Call\s+Clinic\s+Now</a>', '', content)
        if n > 0:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content_new)
            print(f"Removed call button from {f} (via regex)")
            count += 1
        else:
            print(f"Call button not found in {f}")

print(f"Total treatment files updated: {count}")
