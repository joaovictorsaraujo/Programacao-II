def remove_acentos(txt):
    d = {'áàãâ':'a','éèê':'e','íìî':'i','óòõô':'o','úùû':'u','ç':'c',\
         'ÁÀÃÂ':'A','ÉÈÊ':'E','ÍÌÎ':'I','ÓÒÕÔ':'O','ÚÙÛ':'U','Ç':'C'}
    sem_acento = ''

    for letra in txt:
        for k in d:
            if letra in k:
                letra = d.get(k)
                break
        sem_acento += letra
    return sem_acento

def main():
    texto = input('Digite o texto: ')
    while(texto != ''):
        print(remove_acentos(texto))
        texto = input('Digite o texto: ')
main()