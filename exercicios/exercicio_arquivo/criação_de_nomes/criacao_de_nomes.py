import random
def crialista(lst):
    arq = open(lst, 'rt') #abre o arquivo
    lista = []

    vulgo = arq.readline()
    while vulgo != '':
        lista.append(vulgo.split())
        vulgo = arq.readline()

    arq.close #fecha o arquivo

    return lista

def crianome(nomes, sobrenomes, tam):
    nom = []
    sobU = sobrenomes
    nomesCompletos =[]
    ind = random.randint(0,len(sobU) - 1)

    for i in nomes:
        nom.append(i)
        for j in range(tam - 1):
            nom.append(sobU[ind])
            while(sobU[ind] in nom):
                    ind = random.randint(0,len(sobU) - 1)
        nomesCompletos.append(nom)
        nom = []
    return nomesCompletos

def main():
    lstN = crialista('nomes.txt')
    lstS = crialista('sobrenomes.txt')
    nome_completo = crianome(lstN, lstS, 4)
    nome = ''

    for i in (nome_completo):
        for j in i:
            nome += j[0] + ' '
        print(f'{nome}')
        nome = ''
    
if __name__ == '__main__':
    main()
