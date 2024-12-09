def geraMat(mat):  #quant_linhas, quant_colunas, menor num aleatório, maior num aleatório
    import random
    matriz = []

    for j in range(mat[0]):
        linha = []
        for i in range(mat[1]):
            x = random.randrange(mat[2], mat[3])
            linha.append(x)
        matriz.append(linha)
    return matriz

def extrai(mat):  #matriz, linha inicial, coluna inicial, quant_linhas, quant_colunas

    mat1 = mat[0]
    lin = mat[1]
    col = mat[2]
    pos = col
    qlin = mat[3]
    qcol = mat[4]
    nova = []
    matriz = []

    for i in range(qlin):
        for j in range(qcol):
            nova.append(mat1[lin][pos])
            pos += 1
        matriz.append(nova)
        lin += 1
        pos = col
        nova = []
    return matriz

def insere(mat):  # matP, posL, posC, matI
    mPrincipal = mat[0]
    posL = mat[1]
    posC = mat[2]
    mInserida = mat[3]

    # Copiando a matriz principal para evitar modificar o original
    matriz = [linha[:] for linha in mPrincipal]

    # Inserindo a matriz `mInserida` a partir da posição (`posL`, `posC`)
    for i in range(len(mInserida)):
        for j in range(len(mInserida[i])):
            if posL + i < len(matriz) and posC + j < len(matriz[0]):
                matriz[posL + i][posC + j] = mInserida[i][j]

    return matriz

def deslocaEsc(mat):

    matriz = []
    for i in range(len(mat)):
        deslocada = []
        for j in range(len(mat[i])):
            if j > 0:
                deslocada.append(mat[i][j])
        if len(deslocada) > 0:
            deslocada.append(0)
            matriz.append(deslocada)
    return matriz

def deslocaDir(mat):

    matriz = []
    for i in range(len(mat)):
        deslocada = []
        for j in range(len(mat[i]) - 1):
            if j == 0:
                deslocada.append(0)
            deslocada.append(mat[i][j])
        matriz.append(deslocada)
    return matriz

def rotDir(mat):

    last = []
    linha = []
    matriz = []
    for i in (mat):
        last.append(i[len(mat) - 1])

    for j in range(len(mat)):
        for k in range(len(mat[j]) - 1):
            if k == 0:
                linha.append(last[j])
            linha.append(mat[j][k])
        matriz.append(linha)
        linha = []
    return matriz

def rotEsq(mat):

    first = []
    matriz = []
    for i in (mat):
        first.append(i[0])

    for j in range(len(mat)):
        linha = []
        for k in range(len(mat[j]) + 1):
            if k == len(mat):
                linha.append(first[j])
            elif k > 0:
                linha.append(mat[j][k])
        matriz.append(linha)
    return matriz

def vizinhos(mat): #matriz, posL, posC
    matriz = mat[0]
    lin = mat[1]
    col = mat[2]
    vizinhos = []
    posL = lin - 1
    posC = col - 1

    for l in range(len(matriz) - 1):
        for c in range(len(matriz[l]) - 1):
            if posC == c:
                vizinhos.append(matriz[posL][posC])
            posC += 1
        posL += 1
        posC = col - 1
    # del(vizinhos[4])
    return vizinhos

def loadmat(nome_arq):  #arquivo com a matriz

    arq = open(nome_arq, 'rt')  #abre o arquivo
    lista = []

    con = arq.readline()
    lst = []
    mat = []

    while con != '':  #transforma as linhas do arquivo em listas
        lista.append(con.split())
        con = arq.readline()

    for linha in lista:  #transforma o conteudo da lista em int (matriz)
        for j in linha:
            lst.append(int(j))
        mat.append(lst)
        lst = []

    arq.close  #fecha o arquivo
    return mat

def salvamat(mat, nome_arquivo):  #matriz, arquivo para guardar a matriz

    arq = open(nome_arquivo, 'wt')  #abre o arquivo
    txt = ''

    for linha in mat:  #transforma a matriz em texto
        for n in linha:
            n = str(n)
            txt += n
            if n == '':
                break
            txt += ' '
        txt += '\n'

    arq.write(txt)
    arq.close  #fecha o arquivo]

def main():  #testador

    lst = []
    for i in range(4):  #testa geraMat
        n = int(input())
        lst.append(n)
    matriz = geraMat(lst)
    print(matriz)
    # salvamat(matriz, 'mat.txt')

    # lst2 = []
    # lst2.append(matriz)  #testa extrai
    # for i in range(4):
    #     pos = int(input())
    #     lst2.append(pos)
    # matrizEx = extrai(lst2)
    # print(matrizEx)
    # salvamat(matrizEx, 'mat.txt')

    # matrizT = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    # m = []
    # m.append(matriz)
    # for i in range(2):
    #     x = int(input())S
    #     m.append(x)
    # m.append(matrizT)
    # print(m)
    # print(insere(m))

    lst3 = []
    lst3.append(matriz)
    for i in range(2):  #testa geraMat
        n = int(input())
        lst3.append(n)
    lista = vizinhos(lst3)
    print(lista)

main()