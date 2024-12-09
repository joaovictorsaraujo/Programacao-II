#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
def media(list):
    return sum(list) / 4

def main():
    notas = []
    for i in range(4):
        nota = float(input('Adicione sua nota: '))
        notas.append(nota)
    for i in range(len(notas)):
        print(f'Nota {i + 1}: {notas[i]}')
    print(f'Média: {media(notas)}')
main()