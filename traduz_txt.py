from googletrans import Translator

def jumpl(arquivo):
    texto = ''
    with open(arquivo, 'r', encoding='UTF-8') as f:
        texto = f.read()
    
    texto = texto.replace('• ', '\n\n    • ')

    with open(arquivo, 'w', encoding='UTF-8') as f:
        f.write(texto)
        

def traduzir(arquivo, l):
    with open(arquivo, 'w', encoding='UTF-8') as f:
        for text in l:
            text += '\n'

            # Skip empty lines
            if not text.strip():
                continue

            translator = Translator()
            detect = translator.detect(text)

            if detect.lang == 'pt':
                f.write(text)
            else:
                result = translator.translate(text, src=detect.lang, dest='pt')
                f.write(result.text)

def capturar_recortes(arquivo):
    texto = ''
    with open(arquivo, 'r', encoding='UTF-8') as f:
        texto = f.read()

    recortes = texto.split('_________________________________________________________________________')
    return recortes

arquivo = r'C:\Users\est.angelo\Documents\codepy10-11\leitura_pros_S1.txt'
# resultado = capturar_recortes(arquivo)
# traduzir(arquivo, resultado)

jumpl(arquivo)