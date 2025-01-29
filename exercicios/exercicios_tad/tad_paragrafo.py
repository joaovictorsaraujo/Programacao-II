def new_paragrafo(txt):
    return {'paragrafo': str(txt)}

def print_para(tad_paragrafo):
    print(tad_paragrafo['paragrafo'])

def lista_palavras(tad_paragrafo):
    lst = tad_paragrafo['paragrafo'].strip().split()
    return lst

def cont_palavras(tad_paragrafo):
    lst = lista_palavras(tad_paragrafo)
    return len(lst)

def maior_palavra(tad_paragrafo):
    lst = lista_palavras(tad_paragrafo)
    maior = 0
    for palavra in lst:
        if len(palavra) > maior:
            maior = len(palavra)
            maiorP = palavra
    return maiorP

def menor_palavra(tad_paragrafo):
    lst = lista_palavras(tad_paragrafo)
    menor = len(lst[1])
    for palavra in lst:
        if len(palavra) < menor:
            menor = len(palavra)
            menorP = palavra
    return menorP

def freq_palavras(tad_paragrafo):
    freq = {}
    lst = lista_palavras(tad_paragrafo)
    for palavra in lst:
        if palavra not in freq:
            freq[palavra] = 1
        else:
            freq[palavra] += 1
    return freq

# def main():
#     par = new_paragrafo('Vivemos em um mundo cada vez mais conectado, onde as telas de nossos dispositivos estão presentes em quase todas as situações do dia a dia. Se por um lado a tecnologia traz conveniência e aproxima as pessoas, por outro, ela também nos sobrecarrega com informações constantes, mensagens e notificações que, muitas vezes, dificultam a concentração e o descanso mental.')
#     print_para(par)
#     print(cont_palavras(par))
#     print(maior_palavra(par))
#     print(menor_palavra(par))
#     print(lista_palavras(par))
#     print(freq_palavras(par))
# main()