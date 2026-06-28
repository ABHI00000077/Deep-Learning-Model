import io
import re
import shutil
from pathlib import Path

nb_path = Path('d:/ME504Project/Q7Problem1aFIXED.ipynb')
backup = nb_path.with_suffix('.ipynb.bak')
shutil.copy(nb_path, backup)
print(f'Backup written to: {backup}')

# mapping: long -> short (<=5 chars)
replacements = {
    'DATA_DIR': 'ddir',
    'XLSX_FILE': 'xfl',
    'STRESS_DIR': 'sdir',
    'CORD_FILE': 'cfil',
    'natural_sort_key': 'nsort',
    'df_thickness': 'dft',
    'X_raw': 'xraw',
    'stress_files': 'sfls',
    'max_stress_list': 'msl',
    'y_raw': 'yraw',
    'valid_mask': 'vmask',
    'X_scaled': 'xscl',
    'scaler_X': 'sclr',
    'y_log': 'ylog',
    'y_mean': 'ymean',
    'y_std': 'ystd',
    'y_reg_norm': 'yreg',
    'assign_class': 'asg',
    'y_cls': 'ycls',
    'class_names': 'cnm',
    'unique': 'uniq',
    'counts': 'cnt',
    'BeamDataset': 'BData',
    'make_dataloaders': 'mkdlr',
    'train_reg': 'trr',
    'val_reg': 'valr',
    'test_reg': 'ter',
    'GRID_H': 'GH',
    'GRID_W': 'GW',
    'TARGET': 'TGT',
    'X_2d_flat': 'x2f',
    'X_2d': 'x2d',
    'BeamDataset2D': 'BData2',
    'make_dataloaders_2d': 'mkdl2',
    'train_reg_2d': 'trr2',
    'val_reg_2d': 'valr2',
    'test_reg_2d': 'ter2',
    'CNN2D': 'C2D',
    'model_reg': 'mreg',
    'optimizer_reg': 'optreg',
    'criterion_reg': 'crreg',
    'scheduler_reg': 'schreg',
    'model_cls': 'mcls',
    'optimizer_cls': 'optcls',
    'criterion_cls': 'crcls',
    'scheduler_cls': 'schcls',
    'preds_reg_norm': 'prn',
    'trues_reg_norm': 'trn',
    'preds_reg': 'pr',
    'trues_reg': 'tr',
    'unique_c': 'uc',
    'counts_c': 'cc',
    'class_weights': 'cw',
    'probs_cls': 'pcls',
    'preds_cls': 'pcls',
    'trues_cls': 'tcls',
}

patterns = [(re.compile(r'\b' + re.escape(k) + r'\b'), v) for k, v in replacements.items()]


# Remove comments from code using a line-based heuristic: drop full-line comments
# and strip inline comments when the line has an even number of quotes.
def remove_comments_from_code(code_str):
    out_lines = []
    for line in code_str.splitlines():
        if re.match(r'^\s*#', line):
            continue
        if '#' in line:
            # if number of single+double quotes is even, safe to strip inline comment
            if (line.count("'") + line.count('"')) % 2 == 0:
                line = line.split('#', 1)[0].rstrip()
        out_lines.append(line)
    return '\n'.join(out_lines)


# New parsing: treat the notebook file as a text document with <VSCode.Cell> blocks.
txt = nb_path.read_text(encoding='utf-8')

# Split into cell blocks
cell_pattern = re.compile(r'(<VSCode.Cell[^>]*language="(?P<lang>[^"]+)"[^>]*>)(?P<body>.*?)(</VSCode.Cell>)', re.S)
pos = 0
new_txt = ''
cell_idx = 0

for m in cell_pattern.finditer(txt):
    pre = txt[pos:m.start()]
    new_txt += pre
    opening = m.group(1)
    lang = m.group('lang')
    body = m.group('body')
    closing = '</VSCode.Cell>'

    # If this is a python code cell and within first 32 cells, remove comments
    if lang.lower() == 'python' and cell_idx < 32:
        body_new = remove_comments_from_code(body)
    else:
        body_new = body

    # Apply global replacements to this body
    for pat, repl in patterns:
        body_new = pat.sub(repl, body_new)

    new_txt += opening + body_new + closing
    pos = m.end()
    cell_idx += 1

new_txt += txt[pos:]

# Write back
nb_path.write_text(new_txt, encoding='utf-8')
print('Notebook updated in-place (text-mode).')
print('Please run the notebook to verify execution; backup kept.')
import io
import json
import re
import shutil
from pathlib import Path

nb_path = Path('d:/ME504Project/Q7Problem1aFIXED.ipynb')
backup = nb_path.with_suffix('.ipynb.bak')
shutil.copy(nb_path, backup)
print(f'Backup written to: {backup}')

with nb_path.open('r', encoding='utf-8') as f:
    nb = json.load(f)

# mapping: long -> short (<=5 chars)
replacements = {
    'DATA_DIR': 'ddir',
    'XLSX_FILE': 'xfl',
    'STRESS_DIR': 'sdir',
    'CORD_FILE': 'cfil',
    'natural_sort_key': 'nsort',
    'df_thickness': 'dft',
    'X_raw': 'xraw',
    'stress_files': 'sfls',
    'max_stress_list': 'msl',
    'y_raw': 'yraw',
    'valid_mask': 'vmask',
    'X_scaled': 'xscl',
    'scaler_X': 'sclr',
    'y_log': 'ylog',
    'y_mean': 'ymean',
    'y_std': 'ystd',
    'y_reg_norm': 'yreg',
    'assign_class': 'asg',
    'y_cls': 'ycls',
    'class_names': 'cnm',
    'unique': 'uniq',
    'counts': 'cnt',
    'BeamDataset': 'BData',
    'make_dataloaders': 'mkdlr',
    'train_reg': 'trr',
    'val_reg': 'valr',
    'test_reg': 'ter',
    'GRID_H': 'GH',
    'GRID_W': 'GW',
    'TARGET': 'TGT',
    'X_2d_flat': 'x2f',
    'X_2d': 'x2d',
    'BeamDataset2D': 'BData2',
    'make_dataloaders_2d': 'mkdl2',
    'train_reg_2d': 'trr2',
    'val_reg_2d': 'valr2',
    'test_reg_2d': 'ter2',
    'CNN2D': 'C2D',
    'model_reg': 'mreg',
    'optimizer_reg': 'optreg',
    'criterion_reg': 'crreg',
    'scheduler_reg': 'schreg',
    'model_cls': 'mcls',
    'optimizer_cls': 'optcls',
    'criterion_cls': 'crcls',
    'scheduler_cls': 'schcls',
    'preds_reg_norm': 'prn',
    'trues_reg_norm': 'trn',
    'preds_reg': 'pr',
    'trues_reg': 'tr',
    'unique_c': 'uc',
    'counts_c': 'cc',
    'class_weights': 'cw',
    'probs_cls': 'pcls',
    'preds_cls': 'pcls',
    'trues_cls': 'tcls',
}

# Build regex patterns for whole-word replacements
patterns = [(re.compile(r'\b' + re.escape(k) + r'\b'), v) for k, v in replacements.items()]

# Helper to remove comments from a code string
def remove_comments_from_code(code_str):
    out_lines = []
    for line in code_str.splitlines():
        stripped = line.lstrip()
        if stripped.startswith('#'):
            continue
        # remove inline comments but avoid removing inside strings crudely
        # This naive approach splits on '#' and takes first part
        if '#' in line:
            parts = line.split('#')
            # attempt to detect quote chars to avoid splitting inside strings
            if line.count("'") % 2 == 0 and line.count('"') % 2 == 0:
                line = parts[0].rstrip()
            else:
                # leave line as-is if quotes odd (safer)
                line = line
        out_lines.append(line)
    return '\n'.join(out_lines)

# Process cells
cells = nb.get('cells', [])
for idx, cell in enumerate(cells):
    # Global variable rename across all cells (source may be list or string)
    src = cell.get('source', '')
    if isinstance(src, list):
        src_text = ''.join(src)
    else:
        src_text = src

    # For first 32 cells (1-based), remove # comments if code cell
    if idx < 32 and cell.get('cell_type') == 'code':
        src_text = remove_comments_from_code(src_text)

    # Apply replacements globally
    for pat, repl in patterns:
        src_text = pat.sub(repl, src_text)

    # Write back preserving list or string type
    if isinstance(cell.get('source', ''), list):
        # split back into lines with newlines
        cell['source'] = [line + '\n' for line in src_text.splitlines()]
    else:
        cell['source'] = src_text

# Write updated notebook
with nb_path.open('w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print('Notebook updated in-place.')
print('Please run the notebook to verify everything executes.')
