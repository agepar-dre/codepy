import inspect
import json
from googletrans import Translator
from json.decoder import JSONDecodeError

def tradutor(text):
    translator = Translator()

    detect = translator.detect(text)

    if detect.lang == 'pt':
        return text
    else:
        result = translator.translate(text, src=detect.lang, dest='pt')
        return result.text

def print_docs(module):
    with open(fr'C:\Users\est.angelo\Documents\codepy10-11\leitura_pros_S1.txt', 'w', encoding="UTF-8") as f:
        for name, obj in inspect.getmembers(module):    
            if name != None:
                f.write('    • ' + name + ': \n')
            if obj.__doc__ != None:
                dcumnt = obj.__doc__
                # f.write(tradutor(dcumnt))
                f.write(dcumnt)
                f.write('\n')
                f.write('_________________________________________________________________________')
                f.write('\n')

if __name__ == "__main__":
    print_docs(__import__("leitura_s1"))