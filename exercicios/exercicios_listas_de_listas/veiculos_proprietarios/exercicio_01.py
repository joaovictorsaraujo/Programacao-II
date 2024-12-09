# Crie 2 tabelas nos moldes do que foi discutido em aula (listas internas são as linhas da tabela). A 
# primeira tabela, Veiculos, possui como colunas placa, modelo, marca, cpf do propietario. A
# segunda tabela, Proprietarios, possui como colunas cpf, nome, e-mail, celular do propietario.
def tabela(quant):
    tab = []
    input()
    for i in range(quant - 1): #Monta as listas e põe dentro da lista principal
        row = input()
        lst = row.split(',')
        tab.append(lst)
    return tab

def main():
    tabV = tabela(24)
    tabP = tabela(8)

# Alimente ambas as tabelas por meio de redirecionamento de entrada a partir dos arquivos de
# dados fornecidos pelo Professor. Ao final, construa um relatório de Propritários x Veiculos
# contendo para cada Nome, e-mail de proprietário a lsta de placas, modelo, marca de veículos que
# ele possui.
    car = ''
    for i in tabP:
        cpf = i[0]
        nome = i[1]
        email = i[2]
        print()
        print('Informações do Proprietário:'.upper())
        print(f'Nome: {nome} \n\
E-mail: {email}')
        print()
        print(f'Veículos de {nome}:'.upper())
        for j in tabV:
            if cpf == j[3]:
                placa = j[0]
                modelo = j[2]
                marca = j[1]
                car = car + f'Placa: {placa} \nModelo: {modelo} \nMarca: {marca}'
        print(car)
        car = ''
        print()
        print('-' * 40)
main()

