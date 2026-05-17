import os
import re

dir_path = r'c:\Users\TEJAL CHAVAN\.gemini\antigravity\scratch\dermasculptclinic'

new_bar = '''  <div class="offer-bar reveal" style="display: flex; justify-content: center; align-items: center;">
    <div class="offer-item" style="border-right: none;">
      <div class="offer-icon">🎁</div>
      <div class="offer-text"><span>First Session</span><strong>50% OFF Consultation</strong></div>
    </div>
  </div>'''

# We want to match <div class="offer-bar"> up to its </div>
# The original block has 3 offer-items inside.
# Wait, the best way is to read the file, and do a string replacement if possible, 
# or a regex that matches the whole offer-bar block.
pattern = re.compile(r'<div class="offer-bar.*?</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)

for f in os.listdir(dir_path):
    if f.endswith('.html') and f != 'index.html':
        filepath = os.path.join(dir_path, f)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Check if the file has the offer-bar
        if '<div class="offer-bar"' in content or '<div class="offer-bar' in content:
            new_content = pattern.sub(new_bar, content)
            
            # Special case for meta tag
            if f == 'laser-mole-removal-jayanagar.html':
                new_content = new_content.replace('Book your free consultation today.', 'Book your 50% OFF consultation today.')
                
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f'Updated {f}')
