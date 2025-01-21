def new_poli(poli):
    dic = {}
    termo = ''
    lista = []
    
    # for i in poli:
    #     lst.append(i)


    for char in poli:
        if char == '-':
            lista.append(termo)
            termo = char
            continue
        if char == '+':
            lista.append(termo)
            termo = ''
            continue
        termo = termo + char
    lista.append(termo)
    if lista[0] == '':
        del lista[0]
    return lista

def main():
    poli = "-2X4-5X7+44"
    print(new_poli(poli))
main()