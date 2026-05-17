import glob

html_files = glob.glob('*.html')
count = 0

target_str = '<a href="tel:+919916906661" class="btn-nav btn-call">Call Clinic Now</a>'

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if target_str in content:
        # Replace the target string and clean up any trailing/leading extra space
        content = content.replace(target_str, '')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Removed call button from {f}")
        count += 1
    else:
        print(f"Call button not found in {f}")

print(f"Total files updated: {count}")
