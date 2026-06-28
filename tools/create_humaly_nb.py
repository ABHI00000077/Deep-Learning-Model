import json, re, shutil
from pathlib import Path
p=Path('d:/ME504Project/Q7Problem1aFIXED.ipynb')
out=Path('d:/ME504Project/Q7Problem1aFIXED_humaly.ipynb')
shutil.copy(p, p.with_suffix('.ipynb.prehumaly.bak'))
nb=json.loads(p.read_text(encoding='utf-8'))

replacements = {
    'DATA_DIR': 'ddir', 'XLSX_FILE': 'xfl', 'STRESS_DIR': 'sdir', 'CORD_FILE': 'cfil',
    'natural_sort_key': 'nsort', 'df_thickness': 'dft', 'X_raw': 'xraw', 'stress_files': 'sfls',
    'max_stress_list': 'msl', 'y_raw': 'yraw', 'valid_mask': 'vmask', 'X_scaled': 'xscl',
    'scaler_X': 'sclr', 'y_log': 'ylog', 'y_mean': 'ymean', 'y_std': 'ystd', 'y_reg_norm': 'yreg',
    'assign_class': 'asg', 'y_cls': 'ycls', 'class_names': 'cnm', 'BeamDataset': 'BData',
    'make_dataloaders': 'mkdlr', 'GRID_H': 'GH', 'GRID_W': 'GW', 'TARGET': 'TGT', 'X_2d': 'x2d',
    'BeamDataset2D': 'BData2', 'make_dataloaders_2d': 'mkdl2', 'CNN2D': 'C2D', 'model_reg': 'mreg',
    'model_cls': 'mcls', 'preds_reg': 'pr', 'trues_reg': 'tr', 'preds_cls': 'pcls', 'trues_cls': 'tcls'
}
patterns=[(re.compile(r'\b'+re.escape(k)+r'\b'),v) for k,v in replacements.items()]

def remove_comments(src):
    if isinstance(src,list):
        s=''.join(src)
    else:
        s=src
    out=[]
    for line in s.splitlines():
        if re.match(r'^\s*#',line):
            continue
        if '#' in line:
            if (line.count("'")+line.count('"'))%2==0:
                line=line.split('#',1)[0].rstrip()
        out.append(line)
    return '\n'.join(out).splitlines(True)

# process
code_cell_idx=0
before_after=[]
for cell in nb.get('cells',[]):
    if cell.get('cell_type')=='code':
        # count before
        src=cell.get('source','')
        s_before = ''.join(src) if isinstance(src,list) else src
        cnt_before = s_before.count('#')
        if code_cell_idx < 32:
            cell['source']=remove_comments(src)
        # apply replacements
        src2 = ''.join(cell['source']) if isinstance(cell['source'],list) else cell['source']
        for pat,rep in patterns:
            src2 = pat.sub(rep, src2)
        # write back as list of lines
        cell['source'] = [ln+'\n' for ln in src2.splitlines()]
        s_after = ''.join(cell['source'])
        cnt_after = s_after.count('#')
        before_after.append((code_cell_idx+1,cnt_before,cnt_after))
        code_cell_idx += 1

out.write_text(json.dumps(nb,indent=1,ensure_ascii=False),encoding='utf-8')
print('Wrote',out)
for i,b,a in before_after:
    print(f'code cell {i}: # before={b} after={a}')
print('Done')
