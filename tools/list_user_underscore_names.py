import ast, json
from pathlib import Path
p = Path('d:/ME504Project/ME504Code.ipynb')
nb = json.loads(p.read_text(encoding='utf-8'))
ids = {}
for cell in nb['cells']:
    if cell['cell_type'] != 'code':
        continue
    src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
    try:
        tree = ast.parse(src)
    except SyntaxError:
        continue
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            name = node.id
            if '_' in name:
                ids[name] = ids.get(name, 0) + 1
        if isinstance(node, ast.FunctionDef) or isinstance(node, ast.ClassDef):
            name = node.name
            if '_' in name:
                ids[name] = ids.get(name, 0) + 1
        if isinstance(node, ast.arg):
            name = node.arg
            if '_' in name:
                ids[name] = ids.get(name, 0) + 1
    # also assignments to tuple names
print('Assigned user names with underscore:')
for token in sorted(ids):
    print(token, ids[token])
