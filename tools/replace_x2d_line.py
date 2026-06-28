from pathlib import Path
p = Path('d:/ME504Project/ME504Code_humaly.ipynb')
text = p.read_text(encoding='utf-8')
old = '    "print(f\\"\\\\nX_2d shape: {x2d.shape}\\")\\n",'
new = '    "print(f\\"\\\\nX2d shape: {x2d.shape}\\")\\n",'
if old not in text:
    print('old not found')
else:
    p.write_text(text.replace(old, new), encoding='utf-8')
    print('updated')
