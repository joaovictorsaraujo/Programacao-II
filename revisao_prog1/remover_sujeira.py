def textolimpo(texto):

    limpo = ''
    cont = 0

    for i in texto:
        anterior = texto[cont - 1]
        proxima = texto[cont + 1]
        if(i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') or (i == ' '):
            limpo += i
        elif(i == '-'):
            if (anterior >= 'a' and i <= 'z') and (proxima >= 'A' and i <= 'Z'):
                limpo += '-'
            else:
                limpo += ' '
        cont += 1

    return limpo

def main():

    textosujo = input()
    print(textolimpo(textosujo))

if __name__=="__main__":
    main()