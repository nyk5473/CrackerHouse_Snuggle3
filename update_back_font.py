import os

files = [
    'waiting.html', 'sns_event.html', 'inventory.html',
    '최종/waiting.html', '최종/sns_event.html', '최종/inventory.html',
    '최종/KRACKER LAUNDRY.html'
]

old_style = "font-family:var(--font-mono); font-size:12px; color:rgba(255,255,255,0.7); text-decoration:none; letter-spacing:0.1em; transition:var(--tr); display:flex; align-items:center; gap:6px;"
new_style = "font-family:'Noto Sans KR', sans-serif; font-weight:500; font-size:12px; color:rgba(255,255,255,0.7); text-decoration:none; letter-spacing:0.1em; transition:var(--tr); display:flex; align-items:center; gap:6px;"

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_style in content:
            new_content = content.replace(old_style, new_style)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated font in {filepath}")
        else:
            print(f"Style string not found in {filepath}")
