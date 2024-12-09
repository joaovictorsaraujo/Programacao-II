def loadMat(fileName):
    arq = open(fileName, 'rt')
    matriz = []
    
    for linha in arq:
        valores = linha.split()
        matriz.append([int(valor) for valor in valores])
    
    arq.close()
    return matriz

def ts(mat):
    nova = []
    for i in range(len(mat)):
        linha = []
        for j in range(len(mat[i])):
            if j >= i:
                linha.append(mat[i][j])
            else:
                linha.append(0)
        nova.append(linha)
    return nova

def ti(mat):
    nova = []
    for i in range(len(mat)):
        linha = []
        for j in range(len(mat[i])):
            if j <= i:
                linha.append(mat[i][j])
            else:
                linha.append(0)
        nova.append(linha)
    return nova

def printMat(m):
    for i in m:
        print(i)
        
def main():
    matriz = loadMat('q1mat.txt')
    print("Matriz original:")
    printMat(matriz)
    print('-' * 20)
    
    print("Matriz triangular superior:")
    printMat(ts(matriz))
    print('-' * 20)
    
    print("Matriz triangular inferior:")
    printMat(ti(matriz))

main()
