import os, json

audio_dir = r'D:\资海春\Zhaic\音频资产'
files = sorted([f for f in os.listdir(audio_dir) if f.endswith('.mp3') and '(1)' not in f])

# Build audio list with friendly labels
items = []
for f in files:
    name = f.replace('.mp3','')
    items.append({'file': f, 'label': name})

# Generate HTML block
audio_items = ''
for it in items:
    audio_items += f'''      <div class="aud">
        <div class="ic"><svg viewBox="0 0 24 24"><path d="M12 14a3 3 0 003-3V5a3 3 0 00-6 0v6a3 3 0 003 3zm5-3a5 5 0 01-10 0H5a7 7 0 006 6.92V21h2v-3.08A7 7 0 0019 11h-2z"/></svg></div>
        <div class="info"><b>{it['label']}</b></div>
        <audio controls preload="none" src="assets/deploy_assets/audio/{it['file']}"></audio>
      </div>
'''

# Read deploy.html
with open(r'D:\资海春\resume-website\deploy.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the audio-row section
import re
# Find and replace the aud-row div
old_pattern = r'<div class="aud-row" style="margin-top:28px">.*?</div>\s*</div>\s*<div style="margin-top'
# Simpler: find from <div class="aud-row" to the closing that matches
start_marker = '<div class="aud-row" style="margin-top:28px">'
end_marker = '</div>\n    </div>\n  </section>'

si = html.find(start_marker)
if si == -1:
    print("ERROR: start marker not found")
else:
    # Find the matching end - look for </section> after si
    ei = html.find('</section>', si)
    # Go back to find the </div> before </section>
    block = html[si:ei]
    new_block = f'<div class="aud-grid" style="margin-top:28px;display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px">\n{audio_items}    </div>\n  '
    html = html[:si] + new_block + html[ei:]
    
    with open(r'D:\资海春\resume-website\deploy.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated audio section with {len(items)} files")
