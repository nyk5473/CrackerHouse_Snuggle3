import os
import re

files_std = [
    'waiting.html', 'sns_event.html', 'inventory.html',
    '최종/waiting.html', '최종/sns_event.html', '최종/inventory.html'
]
file_kracker = '최종/KRACKER LAUNDRY.html'

back_pattern = re.compile(r'<a href="#" onclick="history\.back\(\); return false;" style="font-family:\'Noto Sans KR\', sans-serif; font-weight:500; font-size:12px; color:rgba\(255,255,255,0\.7\); text-decoration:none; letter-spacing:0\.1em; transition:var\(--tr\); display:flex; align-items:center; gap:6px;" onmouseover="this\.style\.color=\'#fff\'" onmouseout="this\.style\.color=\'rgba\(255,255,255,0\.7\)\'">\s*<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>\s*뒤로가기\s*</a>', re.IGNORECASE)

std_str = """<a href="index.html" style="font-family:var(--font-mono); font-size:12px; color:rgba(255,255,255,0.7); text-decoration:none; letter-spacing:0.1em; transition:var(--tr);" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='rgba(255,255,255,0.7)'">
      // MAIN HOME
    </a>"""

kracker_str = """<a href="https://nyk5473.github.io/CrackerHouse_Laundry_V2/index.html" style="font-family:var(--font-mono); font-size:12px; color:rgba(255,255,255,0.7); text-decoration:none; letter-spacing:0.1em; transition:var(--tr);" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='rgba(255,255,255,0.7)'">
      // MAIN HOME
    </a>"""

for filepath in files_std:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if back_pattern.search(content):
            new_content = back_pattern.sub(std_str, content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Reverted in {filepath}")

if os.path.exists(file_kracker):
    with open(file_kracker, 'r', encoding='utf-8') as f:
        content = f.read()
    if back_pattern.search(content):
        new_content = back_pattern.sub(kracker_str, content)
        with open(file_kracker, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Reverted in {file_kracker}")
