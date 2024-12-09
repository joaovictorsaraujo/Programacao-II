#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
def somaDosQuadradosDe(a):
    soma = 0
    for i in a:
        soma += i ** 2
    return soma

def main():
    a = []
    print('Digite 10 números:')
    for i in range(10):
        num = int(input())
        a.append(num)
    print(f'A soma dos quadrados dos números é: {somaDosQuadradosDe(a)}')
main()