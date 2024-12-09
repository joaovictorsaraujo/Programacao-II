#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
def main():
    
    lst = []
    par = []
    impar = []

    for i in range (20):
        num = int(input())
        lst.append(num)
    for i in lst:
        if i % 2 == 0:
            par.append(i)
        else:
            impar.append(i)
    
    lst.sort()
    par.sort()
    impar.sort()
    print(lst)
    print(par)
    print(impar)

main()