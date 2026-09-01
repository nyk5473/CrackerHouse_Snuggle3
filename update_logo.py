import os

files = ['waiting.html', 'sns_event.html', 'inventory.html', 'CrackerHouse_Snuggle3/waiting.html']

for f in files:
    if not os.path.exists(f):
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Replace nav-brand href
    content = content.replace(
        '<a href="index.html" class="nav-brand">',
        '<a href="#" onclick="resetToGate(); return false;" class="nav-brand">'
    )
    
    # 2. Replace resetToGate function
    old_func = "function resetToGate() {\n      window.location.href = 'index.html';\n    }"
    new_func = "function resetToGate() {\n      sessionStorage.removeItem('kracker_user_role');\n      window.location.href = window.location.pathname;\n    }"
    
    if old_func in content:
        content = content.replace(old_func, new_func)
    else:
        # Try looser matching
        import re
        content = re.sub(
            r'function\s+resetToGate\(\)\s*\{\s*window\.location\.href\s*=\s*[\'"]index\.html[\'"];\s*\}',
            "function resetToGate() {\\n      sessionStorage.removeItem('kracker_user_role');\\n      window.location.href = window.location.pathname;\\n    }",
            content
        )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated {f}")

