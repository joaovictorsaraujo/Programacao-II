import os
def cadastra_prod(produtos, nome, valor, preço):
    produtos[nome] = [valor, preço]
    return produtos

def main():
    prod = {}
    item = ['nome', 'valor', 'preço']
    info = str
    cadastro = 'Nenhum item informado'
    while info != '':
        cadastrar = [prod]
        for i in range(3):
            info = input(f'Digite o {item[i]}: ')
            cadastrar.append(info)
            if cadastrar[1] == '':
                os.system('cls')
                print(cadastro)
                break
            os.system('cls')
        if cadastrar[1] != '':
            cadastro = cadastra_prod(cadastrar[0], cadastrar[1], cadastrar[2], cadastrar[3])
            print(cadastro)
main()