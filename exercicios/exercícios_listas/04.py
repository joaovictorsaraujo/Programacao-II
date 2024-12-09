#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
def quantas(txt, nova):
    vogal = ['a', 'e', 'i', 'o', 'u']
    cont = 0
    for c in txt:
        if c.isalpha() and (c in vogal):
            cont += 1
            nova.append(c)
    return cont, nova


def main():
    lst = []
    nova = []
    for i in range(10):
        l = input()
        lst.insert(len(lst))
    print(quantas(lst, nova))
    print(nova)


main()
