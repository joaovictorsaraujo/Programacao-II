import os
def contCaracteres(texto):
    dic = {}
    for palavra in texto.split():
        for letra in palavra:
            if letra not in dic:
                dic[letra.lower()] = 1
            else:
                dic[letra.lower()] += 1
    return dic

def main():
    txt = input('Digite o texto: ')
    while(txt != ''):
        resultado = contCaracteres(txt)
        for k in sorted(resultado):
            print(f'{k}, {resultado[k]}')
        txt = input('Digite o texto: ')
        os.system('cls')
main()