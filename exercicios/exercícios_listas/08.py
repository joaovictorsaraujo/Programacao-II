#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
def main():
    dados = []
    for i in range(5):
        idade = int(input(f'Insira a idade de alguém: '))
        altura = float(input(f'Insira sua altura: '))
        dados.append(idade)
        dados.append(altura)
    cont = len(dados) - 1

    for i in range(len(dados)):
        if type(dados[i - 1]) == float:
            print(f'Altura: {dados[cont]}')
        else:
            print(f'Idade: {dados[cont]}')
        cont -= 1
main()
