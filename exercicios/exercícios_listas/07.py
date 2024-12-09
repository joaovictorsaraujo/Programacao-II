#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
def m(num):
    mult = 1
    for i in num:
        mult = mult * i
    return mult

def a(num):
    return sum(num)

def main():
    lst = []
    for i in range(5):
        num = int(input(f'Insira o {i + 1}º número: '))
        lst.append(num)
    print(f'Soma dos números: {a(lst)}')
    print(f'Multiplicação dos números: {m(lst)}')
    print(f'Números: {lst}')
main()