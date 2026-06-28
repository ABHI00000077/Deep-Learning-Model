import json, re, shutil
from pathlib import Path
p=Path('d:/ME504Project/Q7Problem1aFIXED.ipynb')
bak=p.with_suffix('.ipynb.json.bak')
shutil.copy(p,bak)
print('backup:',bak)
nb=json.loads(p.read_text(encoding='utf-8'))

def count_hash(src):
    if isinstance(src,list):
        s=''.join(src)
    else:
        s=src
    return s.count('#')

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

before=[]
after=[]
count=0
for cell in nb.get('cells',[]):
    if cell.get('cell_type')=='code' and count<32:
        b=count_hash(cell.get('source',''))
        before.append(b)
        cell['source']=remove_comments(cell.get('source',''))
        a=count_hash(cell.get('source',''))
        after.append(a)
        count+=1

print('processed code cells:',count)
for i,(b,a) in enumerate(zip(before,after),1):
    print(f'cell {i}: # before={b} after={a}')

p.write_text(json.dumps(nb,indent=1,ensure_ascii=False),encoding='utf-8')
print('written updated notebook')
