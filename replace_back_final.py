import os

files = ['최종/waiting.html', '최종/sns_event.html', '최종/inventory.html']

old_str = """    <a href="index.html" style="font-family:var(--font-mono); font-size:12px; color:rgba(255,255,255,0.7); text-decoration:none; letter-spacing:0.1em; transition:var(--tr);" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='rgba(255,255,255,0.7)'">
      // MAIN HOME
    </a>"""

new_str = """    <a href="#" onclick="history.back(); return false;" style="font-family:var(--font-mono); font-size:12px; color:rgba(255,255,255,0.7); text-decoration:none; letter-spacing:0.1em; transition:var(--tr); display:flex; align-items:center; gap:6px;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='rgba(255,255,255,0.7)'">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
      뒤로가기
    </a>"""

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_str in content:
            new_content = content.replace(old_str, new_str)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Replaced in {filepath}")
        else:
            print(f"Pattern not found in {filepath}")
