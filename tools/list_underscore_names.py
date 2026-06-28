import json, re
from pathlib import Path
p = Path('d:/ME504Project/ME504Code.ipynb')
nb = json.loads(p.read_text(encoding='utf-8'))
ids = {}
for cell in nb['cells']:
    if cell['cell_type'] != 'code':
        continue
    src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
    for match in re.finditer(r'\b[A-Za-z][A-Za-z0-9_]*_[A-Za-z0-9_]*\b', src):
        token = match.group(0)
        ids[token] = ids.get(token, 0) + 1
for token in sorted(ids):
    print(f'{token}: {ids[token]}')
print('--- total', len(ids))
