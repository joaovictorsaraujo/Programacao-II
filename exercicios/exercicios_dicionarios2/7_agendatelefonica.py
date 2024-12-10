import os
def armazena_in_dic(contatos):
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
    agenda[contato] = [nome, email]
    txt = ('\n' + str(contato) + ', ' + str(nome) + ', ' + str(email))
        
    arq = open('7_arquivo.txt', 'a')
    arq.write(txt)
    arq.close()
    return agenda

def printa(agenda):
    print("Lista telefônica: ")
    print(f"{'Contato':<21}{'Nome':<20}{'E-mail'}")
    print()
    for contato in agenda:
        print(f'{contato:<20}{agenda[contato][0]:<20}{agenda[contato][1]}')

def main():
    arquivo = '7_arquivo.txt'
    contatos = armazena_in_dic(arquivo)
    printa(contatos)
    print('Adicionar contato: 1, Remover contato: 2, Buscar contato: 3')
    acao = int(input(('O que deseja fazer? ')))

    while acao != '':
        os.system('cls')
        if acao == 1:
            cont = input('Digite um contato: ')
            while cont != '':
                name = input('Digite o nome: ')
                email = input('Digite o e-mail: ')
                contatos = adicionar(cont, name, email, contatos)
                cont = input('Digite outro contato ou aperte enter para sair: ')
        os.system('cls')
        printa(contatos)
        print()
        acao = input('O que deseja fazer agora? ')
main()