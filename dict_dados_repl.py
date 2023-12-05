import re

dicio = {}
linhas = []

with open(r'C:\Users\est.angelo\Documents\codepy10-11\DictDados0.txt', 'r', encoding="UTF-8") as f:
    linhas = f.readlines()

for l in linhas:
    l = l.replace('\n', '')

    if l == '------------------------------':
        break
    elif l == 'Dicionario de dados':
        continue

    corte = l.split(': ')
    dicio[corte[0]] = corte[1]

for l in linhas:
    l = l.replace('\n', '')
    replaced = []
    if '=' in l:
        for x,y in dicio.items():
            if re.search(rf"\b{x.upper()}\b", l):
                l = re.sub(rf"\b{x.upper()}\b", y, l)
    
    print(l)
