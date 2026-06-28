import re
p='d:/ME504Project/Q7Problem1aFIXED.ipynb'
with open(p,encoding='utf-8') as f:
    txt=f.read()

parts = txt.split('</VSCode.Cell>')
ci=0
for part in parts:
    if '<VSCode.Cell' not in part:
        continue
    header, body = part.split('>',1)
    lang_m = re.search(r'language=["\']?(\w+)["\']?', header)
    lang = lang_m.group(1) if lang_m else 'unknown'
    if lang.lower()=='python' and ci<32:
        print('CELL',ci+1,'#count=',body.count('#'))
        print('\n'.join(body.splitlines()[:6]))
        print('----')
    ci+=1
print('Total cells scanned:',ci)
