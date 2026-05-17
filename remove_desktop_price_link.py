import glob
import re

html_files = glob.glob('*.html')
count = 0

target_str = """    <li>
      <a href="pricing.html">Price List</a>
    </li>
  </ul>"""

replacement_str = "  </ul>"

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Let's check if the target string exists
    if target_str in content:
        content = content.replace(target_str, replacement_str)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Removed desktop Price List link from {f}")
        count += 1
    else:
        # Fallback to regex in case of slight indent/spacing differences
        content_new, n = re.subn(r'<li>\s*<a href="pricing\.html">Price List</a>\s*</li>\s*</ul>', '  </ul>', content)
        if n > 0:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content_new)
            print(f"Removed desktop Price List link from {f} (via regex)")
            count += 1
        else:
            print(f"Target not found in {f}")

print(f"Total files updated: {count}")
