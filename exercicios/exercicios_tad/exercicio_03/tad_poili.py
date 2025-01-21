def new_poli(poli):
    dic = {}
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

    for n in lista:
        lst = n.split('X')
        if len(lst) == 1:
            dic['1'] = lst[0]
        else:
            dic[lst[1]] = lst[0]
    return dic

def main():
    poli = "-2X4-5X7+44"
    print(new_poli(poli))
main()