import json
import ast
from pathlib import Path
p = Path('d:/ME504Project/ME504Code_humaly.ipynb')
nb = json.loads(p.read_text(encoding='utf-8'))
errors = []
for i, cell in enumerate(nb['cells'], 1):
    if cell['cell_type'] != 'code':
        continue
    src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
    try:
        ast.parse(src)
    except SyntaxError as e:
        errors.append((i, e.lineno, e.offset, e.text.strip() if e.text else '', e.msg))
print('Checked', sum(1 for c in nb['cells'] if c['cell_type']=='code'), 'code cells')
if errors:
    print('Syntax errors found:')
    for cell_i, lineno, offset, text, msg in errors:
        print(f'Cell {cell_i}: line {lineno}, col {offset}: {msg}')
        print('  ', text)
else:
    print('No syntax errors detected in code cells.')
