def separa_poli(poli):
    termo = ''
    lista = []
    for char in poli:
        if char == '-':
            lista.append(termo.upper())
            termo = char
            continue
        if char == '+':
            lista.append(termo.upper())
            termo = ''
            continue
        termo = termo + char
    lista.append(termo.upper())
    if lista[0] == '':
        del lista[0]
    return lista

def new_poli(poli):
    lst = separa_poli(poli)
    dic = {}
    for n in lst:
        lst = n.split('X')
        if len(lst) == 1:
            lst.append(0)
        if lst[1] == '':
            lst[1] = 1 
        if lst[0] == '':
            lst[0] = 1    
        elif lst[0] == '-':
            lst[0] = '-1'
        dic[int(lst[1])] = int(lst[0])
    return dic

def soma_poli(p1, p2):
    dic = {}
    for i in p1:
        dic[i] = p1[i] + p2.get(i,0)
    return dic

def multiplica_poli(p1, p2):
    dic = {}
    for i in p1:
        for j in p2:
            dic[i + j] = p1[i] * p2[j]
    return dic

def subtrai_poli(p1, p2):
    # pS = {}
    # for h in p2:
    #     pS[h] = p2[h] * (-1)
    # return soma_poli(p1, pS)
    dic = {}
    for i in p1:
        dic[i] = p1[i] - p2.get(i,0)
    return dic

# def main():
#     poli = "-3X2+2X+1"
#     poli2 = "2X2+3X+1"
#     print(new_poli(poli))
#     print(new_poli(poli2))
#     print()
#     print(subtrai_poli(new_poli(poli), new_poli(poli2)))
# main()
