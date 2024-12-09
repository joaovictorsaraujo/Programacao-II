#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
def intercala(lista1, lista2):
    lista3 = []

    for i in range(len(lista1)):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
    return lista3

def main():
    lista1 = []
    lista2 = []

    for i in range(2):
        for i in range(10):
            num = int(input())
            if len(lista1) != 10:
                lista1.append(num)
            else:
                lista2.append(num)
    print(intercala(lista1, lista2))
main()