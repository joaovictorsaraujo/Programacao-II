#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
def media(notas):
    return sum(notas) / 4

def main():
    notas = []
    medias = []
    cont = 0
    for x in range(3):
        for n in range(4):
            nota = float(input(f'Adicione a {n + 1}º nota do aluno {x + 1}: '))
            notas.append(nota)
        resultado = media(notas)
        medias.append(resultado)
        notas = []
    for i in medias:
        if (i >= 7.0):
            cont += 1
    if (cont == 1):
        print(f'{cont} aluno está acima da média')
    elif (cont > 1):
        print(f'{cont} alunos estão acima da média')
    else:
        print(f'Nenhum aluno está acima da média')
main()