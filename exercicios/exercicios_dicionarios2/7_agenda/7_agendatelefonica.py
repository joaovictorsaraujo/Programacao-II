def armazena(contatos):
    arq = open(contatos, 'rt')
    linha = arq.readline()
    agenda = {}
    
    while(linha != ''):
        lst_linha = list(linha.split())
        if lst_linha[0] not in agenda:
            agenda[lst_linha[0]] = [lst_linha[1], lst_linha[2]]
        linha = arq.readline()
    arq.close()
    return agenda

def main():
    arquivo = '7_arquivo.txt'
    print(armazena(arquivo))
main()