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
    lista.append(termo)
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

def main():
    poli = "-2X4-5X7-3X-X5+44"
    print(new_poli(poli))
main()
