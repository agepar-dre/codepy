import pandas as pd
import openpyxl
import re

def sao_todas_strings(lista):
    '''Verifica se todos os elementos em uma lista são strings.'''
    for elemento in lista:
        if not isinstance(elemento, str):
            return False
    return True

def remove_lines(filename, target_line):
    '''Remove linhas específicas de um arquivo de texto.'''
    with open(filename, 'r', encoding="UTF-8") as file:
        lines = file.readlines()

    with open(filename, 'w', encoding="UTF-8") as file:
        i = 0
        while i < len(lines):
            if lines[i].strip() == target_line:
                i += 3  # Pula a linha atual, anterior e posterior
            elif i > 0 and i + 2 < len(lines) and lines[i + 1].strip() == target_line:
                i += 3  # Pula a linha atual, anterior e posterior
            else:
                file.write(lines[i])
                i += 1

def verifica_formula(texto):
    '''Verifica se uma string representa uma fórmula do Excel.'''
    if texto.startswith('='):
        if texto[1].isalpha():
            return True
        else:
            return False
    else:
        return False

def substituir_sheet(texto):
    '''Substitui referências a planilhas por identificadores específicos.'''
    resultado = texto
    for s,n in d_sheets.items():
        if n in texto:
            return texto.replace(n,s)
    return resultado

def substituir_virgula_por_ponto_virgula(texto):
    '''Substitui vírgulas por ponto e vírgula em uma string.'''
    padrao = r'\((.*?)\)'  # Padrão para encontrar o texto entre parênteses
    resultado = re.sub(padrao, lambda match: match.group().replace(',', ';'), texto)
    return resultado

def substituir_ponto_por_virgula(texto):
    '''Substitui pontos por vírgulas em números decimais.'''

    padrao = r'\d+\.\d+'
    resultado = re.sub(padrao, lambda match: match.group().replace('.', ','), texto)
    return resultado

def remove_space(string):
    '''Remove espaços de uma string.'''
    return "".join(string.split())

def remove_num(string):
    '''Remove números de uma string.'''
    return re.sub(r'\d+', '', string)

def int_to_col_letter(n):
    '''Converte um número para uma letra de coluna do Excel.'''
    result = ''
    while n >= 0:
        n, remainder = divmod(n, 26)
        result = chr(remainder + 97) + result
        n -= 1
    return result

def trocar_por_chave(val, dct):
    '''Troca um valor em um dicionário por sua chave correspondente.'''
    for chave, valor in dct.items():
        if valor == val:
            return chave

def extract_lines(filename, target_variable):
    '''Extrai linhas de um arquivo de texto até encontrar um delimitador.'''
    lines_to_extract = []
    extracting = False

    with open(filename, 'r', encoding="UTF-8") as file:
        for line in file:
            if extracting:
                if '------------------------------' in line:
                    break
                lines_to_extract.append(line)
            elif f'Coluna {target_variable}' in line:
                extracting = True

    return lines_to_extract

def gerar_prompt(f):
    '''Gera um prompt para documentação de função Python com base em uma fórmula do Excel.'''

    prompt = 'faça uma função em python para a formula de excel: ' + f + '\n'
    prompt += 'insira uma documentação da função indicando a correspondência de cada variável, preservando os nomes originais escritos na tabela abaixo e usando as letras como atributos, seguindo dicionário de dados abaixo:\n[nome do atributo: significado presente APENAS na documentação]\n'

    for x,y in dict_coluna.items():
        if  x == f[0:f.find('=')] or re.search(f'\W{x.upper()}\W', f):
            prompt += x+ ' : ' + y 
            if re.search(rf'!\s*{x.upper()}', f):
                prompt += '(essa variavel pertence a planilha que vem antes do !)'
            prompt += '\n'
    
    prompt+= '''Exemplo:
    def função(inputs):
	    #Função que calcula a variável x
	    #Inputs
	    #x: coluna x
	    #Outputs
	    #a: coluna a
	    #b: coluna b
	    x = a + b
	    return x
        
        '''

    return prompt


REGEX_VAR = '(?<![\'":])([A-Z]{1,3}[0-9]{1,7})(?![\'":])'

path = r'C:\Users\est.angelo\Documents\codepy10-11\Simulação_calculos_BRR_v6.xlsx'

# Carregar o arquivo Excel
wb = openpyxl.load_workbook(filename=path)
sheet_names = wb.sheetnames
d_sheets = {}
for i in range(1, len(sheet_names)+1):
    k = f'S{i}'
    d_sheets[k] = remove_space(sheet_names[i-1])

a = pd.read_excel(path, header=0, sheet_name=sheet_names[0])
a.columns = a.columns.str.replace('\n', ' ')

name = sheet_names[0]
sheet_ranges = wb[name]
vals = sheet_ranges.values

path_txt = rf"C:\Users\est.angelo\Documents\codepy10-11\DictDados0.txt"

# Criar o DataFrame a partir dos valores e usar a primeira linha como nomes das colunas
df = pd.DataFrame(vals)
df = df.dropna(axis=1, how='all')
df.drop(index=0, axis=0, inplace=True)

df.columns = a.columns

dict_coluna = {}

# Abrir o arquivo de texto para escrita
with open(path_txt, "w", encoding="UTF-8") as f:
    f.write('Dicionario de dados\n')
    colunas_i = []

    for col_name, col_values in df.items():
        colunas_i.append(col_name)

    for idx, c in enumerate(colunas_i):
        letra = int_to_col_letter(idx)
        dict_coluna[letra] = c

    for letra, coluna in dict_coluna.items():
        f.write(f"{letra}: {coluna}\n")
    
    f.write('-' * 30 + '\n') 
    f.write('Formulas:\n')

    # Iterar sobre as colunas e seus valores
    for col_name, col_values in df.items():
        written = set()
        have_l = False
        col_name_print = trocar_por_chave(col_name, dict_coluna)
        f.write(f"Coluna {col_name_print} ({col_name}):\n")

        # Iterar sobre os valores da coluna
        for cell_value in col_values:
            
            if cell_value == None:
                break

            if isinstance(cell_value, str):
                
                cell_value = remove_space(cell_value)
                
                var = re.findall(REGEX_VAR, cell_value)
                
                for v in var:
                    if v in cell_value:
                        cell_value = cell_value.replace(v, remove_num(v))

                cell_value = substituir_ponto_por_virgula(cell_value)
                cell_value = substituir_virgula_por_ponto_virgula(cell_value)
                cell_value = substituir_sheet(cell_value)

                # Usamos uma expressão regular para encontrar o padrão "!$D$5" e capturar o que está antes e depois das aspas
                padrao = r"'(.*?)'!\$(.*?)\$(\d)"
                

                # Encontrar todas as correspondências na string
                correspondencias = re.findall(padrao, cell_value)

                if correspondencias:
                    for correspondencia in list(set(correspondencias)):
                        antes_aspas, depois_var, num_var = correspondencia
                        cell_value = cell_value.replace(f"{depois_var}${num_var}", f'{antes_aspas}_{depois_var}_{num_var}')
                        dict_coluna[f'{antes_aspas}_{depois_var}'] = f'Letra_{depois_var}_de_{antes_aspas}'

                if cell_value not in written and verifica_formula(cell_value):
                    f.write(col_name_print + cell_value)
                    f.write('\n')
                    written.add(cell_value)
                    have_l = True

        if not have_l:
            f.write('Não há fórmulas nesta coluna.\n')
        f.write('-' * 30 + '\n')


remove_lines(path_txt, 'Não há fórmulas nesta coluna.')

for l in extract_lines(path_txt, 'az'):
    print(gerar_prompt(l.strip()))

# Fechar o arquivo de texto
print("Processamento concluído e o resultado foi salvo em 'Teste.txt'.\n\n\n")

