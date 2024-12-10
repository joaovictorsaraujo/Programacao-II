def armazena(contatos):
    arq = open(contatos, 'rt')
    linha = arq.readline().strip()
    agenda = {}
    
    while(linha != ''):
        lst_linha = list(linha.split(','))
        if lst_linha[0] not in agenda:
            agenda[lst_linha[0]] = [lst_linha[1], lst_linha[2]]
        linha = arq.readline().strip()
    arq.close()
    return agenda

def adicionar(contato, nome, email, agenda):
    if contato not in agenda:
        agenda[contato] = [nome, email]
    
    arq = open('7_arquivo.txt', 'wt')
    arq.write(agenda)
    arq.close()
    return agenda

def main():
    print('Adicionar contato: 1, Remover contato: 2, Buscar contato: 3')
    arquivo = '7_arquivo.txt'
    contatos = armazena(arquivo)
    acao = int(input(('O que deseja fazer? ')))

    while acao != '':
        if acao == 1:
            cont = input('Digite um contato: ')
            while cont != '':
                name = input('Digite o nome: ')
                email = input('Digite o e-mail: ')
                contatos = adicionar(cont, name, email, contatos)
                cont = input('Digite outro contato: ')
            print(contatos)
            print()
            acao = input('O que deseja fazer agora? ')
main()