import os
import re

dir_path = r'c:\Users\TEJAL CHAVAN\.gemini\antigravity\scratch\dermasculptclinic'

new_bar = '''<div class="offer-bar reveal" style="display: flex; justify-content: center; align-items: center;">
  <div class="offer-item" style="border-right: none;">
    <div class="offer-icon">🎁</div>
    <div class="offer-text"><span>First Session</span><strong>50% OFF Consultation</strong></div>
  </div>
</div>'''

for f in os.listdir(dir_path):
    if f.endswith('.html') and f != 'index.html':
        filepath = os.path.join(dir_path, f)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # We can use a regex that matches <div class="offer-bar... and then matches everything until <!-- SEO SECTION -->
        # Because we know the offer bar is immediately followed by <!-- SEO SECTION --> in all these files!
        
        if '<div class="offer-bar"' in content or '<div class="offer-bar reveal"' in content:
            # Let's find the start of the offer bar
            match = re.search(r'<div class="offer-bar[^>]*>', content)
            if match:
                start_idx = match.start()
                
                # Find the start of SEO SECTION
                end_idx = content.find('<!-- SEO SECTION -->', start_idx)
                if end_idx != -1:
                    # Replace the entire block between start_idx and end_idx
                    old_block = content[start_idx:end_idx]
                    
                    new_content = content[:start_idx] + new_bar + '\n\n' + content[end_idx:]
                    
                    if f == 'laser-mole-removal-jayanagar.html':
                        new_content = new_content.replace('Book your free consultation today.', 'Book your 50% OFF consultation today.')
                        
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    print(f'Successfully updated {f}')
                else:
                    print(f'Could not find SEO SECTION in {f}')
