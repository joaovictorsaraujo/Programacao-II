def abre_arq(nome_arq):
    arq = open(nome_arq, 'rt')
    linha = arq.readline()
    dic = {}

    while(linha != ''):
        for dezena in linha.split():
            if int(dezena) not in dic:
                dic[int(dezena)] = 1
            else:
                dic[int(dezena)] += 1
        linha = arq.readline()
    arq.close()
    return (dic)

def main():
    cont = abre_arq('4_dados.txt')
    for k in sorted(cont):
        print(f'{str(k)}, {cont[k]}')
main()