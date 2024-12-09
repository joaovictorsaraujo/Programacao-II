def remove_none(dic): #01
    lst = []
    for k in dic.keys():
        if dic[k] == None:
            lst.append(k)
    for k in lst:
        del dic[k]
    return dic

def filtra_dic(dic): #02
    lst = []
    dic1 = {}
    for k in dic:
        if dic[k] > 170:
            lst.append(k)
    for k in lst:
        dic1[k] = dic[k]
    return dic1

def converte_ls(l1, l2, l3): #03
    lst1 = []
    for i in range(len(l2)):
        dic0 = {}
        dic0[l2[i]] = l3[i]
        lst1.append(dic0)
    lst2 = []
    for i in range(len(l1)):
        dic = {}
        dic[l1[i]] = lst1[i]
        lst2.append(dic)
    return lst2

def filtra_altura(dic): #04
    dic2 = {}
    for k in dic:
        if dic[k][0] > 1.75 and dic[k][1] > 70:
            dic2[k] = dic[k]

    if dic2 == {}:
        return 'A busca não obteve resultados'
    else:
        return dic2

def agrupa(lst): #05
    dic = {}
    for i in lst:
        l = [i[1]]
        if i[0] not in dic:
            dic[i[0]] = l
        else:
            l = dic[i[0]]
            l.append(i[1])
            dic[i[0]] = l
    return dic

def reparte(dic): #06
    for k in dic:
        l = len(dic[k])

    lst = []
    for i in range(l):
        d = {}
        for k in dic:
            d[k] = dic[k][i]
        lst.append(d)
    return lst

def remove(lst, val): #07
    rem = []
    for d in range(len(lst)):
        for k in lst[d]:
            if lst[d][k] == val:
                rem.append(d)
    for i in rem:
        del lst[i]
    return lst

def guarda(nome_arq): #08
    arq = open(nome_arq, 'rt')
    dic = {}
    linha = arq.readline()

    while linha != '':
        lst = list(linha.split())
        chave = lst[0].strip(',')
        valor = int(lst[1])
        if chave not in dic:
            dic[chave] = [valor]
        else:
            dic[chave].append(valor)
        linha = arq.readline()
    arq.close()
    return dic

def extrai_val(lst, key): #09
    val = []
    for dic in lst:
        for k in dic:
            if k == key:
                val.append(dic[k])
    return val

def comprimento(dic): #10
    d = {}
    for k in dic:
        val = dic[k]
        d[val] = len(val)
    return d

def converte_lst(dic): #11
    lista = []
    for k in dic:
        lst = []
        lst.append(k)
        lst.append(dic[k])
        lista.append(lst)
    return lista

def filtra_num(dic): #12

    for key in dic:
        lst = []
        for num in dic[key]:
            if num % 2 == 0:
                lst.append(num)
        dic[key] = lst
    return dic

def cartesiano(d): #13
    lst = []
    for k in d:
        for l in d:
            dic = {}
            dic[k] = d[k]
            if dic[k] == d[l]:
                continue
            else:
                dic[l] = d[l]
            if dic not in lst:
                lst.append(dic)
    return lst

def maiores_dic(dic, n): #14
    lst = []
    for k in dic: #Cria uma lista com todos os valores do dicionário
        if dic[k] in lst:
            continue
        lst.append(dic[k])
    lst = sorted(lst, reverse = True) #Ordena a lista em ordem decrescente

    nova = []
    for i in range(n): #Pega as chaves que possuem os n maiores valores do dicionário
        for k in dic:
            if dic[k] == lst[i]:
                nova.append(k)
                break
    return nova

def menores_lst(dic): #15
    b = False
    lst = []
    for k in dic:
        if b == False: #Define o primeiro valor da lista como menor tamanho
            m = len(dic[k])
            b = True
        elif len(dic[k]) < m: #Se o próximo valor tiver um tamanho menor, adiciona a chave na lista 
            lst.append(k)
        m = len(dic[k])
    return lst

def frequencia(dic): #16
    d = {}
    for k in dic.values():
        if k not in d: #Adiciona o valor como chave do dicionário
            d[k] = 1
        else: #Soma a quantidade de vezes que o valor aparece
            d[k] = d[k]+ 1
    return d

def extrai_val(lst): #17
    lst_valores = []
    for dic in lst:
        lst = []
        for val in dic.values(): #Cria uma lista com os valores dos dicionários
            lst.append(val)
        lst_valores.append(lst) #Adiciona a lista de valores dentro da lista principal
    id_nome = []
    for lista in lst_valores:
        lst = [lista[0], lista[1]]
        id_nome.append(lst)

    nome_turma = []
    for lista in lst_valores:
        lst = [lista[1], lista[2]]
        nome_turma.append(lst)

    return lst_valores, id_nome, nome_turma

def converte(lst): #18
    dic = {}
    for l in lst:
        dic[l[0]] = [l[1], l[2]]
    return dic

def verifica(lst, chave, valor): #19
    r = False
    for dic in lst:
        for k in dic:
            if k == chave and dic[k] == valor:
                r = True
    return r

def combina(dic1, dic2): #20
    dic3 = {}
    for k in dic1:
        if k not in dic3:
            dic3[k] = [dic1[k]]
        else:
            dic3[k].append(dic1[k])
    for l in dic2:
        if l not in dic3:
            dic3[l] = [dic2[l]]
        else:
            dic3[l].append(dic2[l])
    return dic3

def tamanho(txt): #21
    dic = {}
    for palavra in txt.split():
        if len(palavra) not in dic:
            dic[len(palavra)] = [palavra]
        else:
            dic[len(palavra)].append(palavra)
    return dic

def associados_key(lista, chave): #22
    lst = []
    for dic in lista:
        for k in dic:
            if k == chave:
                lst.append(dic[k])
    return lst

def associados_max_min(dic): #23
    tpl = ()
    b = True
    for k in dic:
        if b == True:
            max, min = dic[k], dic[k]
            maximo, minimo = k, k
            b = False
        if max < dic[k]:
            max = dic[k]
            maximo = k
        if min > dic[k]:
            min = dic[k]
            minimo = k
    tpl = (maximo, minimo)
    return tpl

def main():
    dic = {'Teodoro': 19, 'Rosane': 22, 'Mateus': 21, 'Elizabete': 20}
    print(associados_max_min(dic))
main()