import re

filepath = r'최종\KRACKER LAUNDRY.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'<a href="https://nyk5473\.github\.io/[^>]+>\s*// MAIN HOME\s*</a>', re.IGNORECASE)

new_str = """<a href="#" onclick="history.back(); return false;" style="font-family:var(--font-mono); font-size:12px; color:rgba(255,255,255,0.7); text-decoration:none; letter-spacing:0.1em; transition:var(--tr); display:flex; align-items:center; gap:6px;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='rgba(255,255,255,0.7)'">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
      뒤로가기
    </a>"""

if pattern.search(content):
    new_content = pattern.sub(new_str, content)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replaced in KRACKER LAUNDRY.html")
else:
    print("Pattern not found")
