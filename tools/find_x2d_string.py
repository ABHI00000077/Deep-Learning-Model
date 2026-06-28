from pathlib import Path
p = Path('d:/ME504Project/ME504Code_humaly.ipynb')
text = p.read_text(encoding='utf-8')
for i, line in enumerate(text.splitlines(),1):
    if 'X_2d shape' in line or 'X2d shape' in line:
        print(i, repr(line))
