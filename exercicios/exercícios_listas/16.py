# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores: 
# $200 - $299, $300 - $399, $400 - $499, $500 - $599, $600 - $699, $700 - $799, $800 - $899, $900 - $999, $1000 em diante
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
def main():
    cont = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    lista = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = 1
    x = int(input('Digite o a venda bruta de um vendedor: '))
    while (x != 0):
        for i in lista:
            sal = 200 + (x * 0.09)
            y = sal // 100
            if y == i:
                cont[i - 2] = cont[i - 2] + 1
            elif y > 10:
                cont[8] = cont[8] + 1
                break
        x = int(input('Digite o a venda bruta de outro vendedor: '))
    print(cont)
    i = 0
    for q in cont:
        if q == 0:
            print(f'Nenhum vendedor no intervalo de R${lista[i]}00,00 - R${lista[i]}99,00')
        elif q == 1:
            print(f'{q} vendedor no intervalo de R${lista[i]}00,00 - R${lista[i]}99,00')
        elif q > 1:
            print(f'{q} vendedores no intervalo de R${lista[i]}00,00 - R${lista[i]}99,00')
        i += 1
main()