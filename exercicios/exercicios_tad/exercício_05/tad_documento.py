import tad_paragrafo as tP
def load_documento(filename):
    doc = open(filename, 'rt', encoding = 'UTF-8')
    lst = []
    for linha in doc:
        if linha.strip() == '':
            continue
        else:
            lst.append(tP.new_paragrafo(linha.strip()))
    doc.close()
    return lst

def insere_paragrafo(tad_doc, paragrafo, pos):
    paragrafo = tP.new_paragrafo(paragrafo)
    tad_doc.insert(pos, paragrafo)
    return tad_doc

def remove_paragrafo(tad_doc, pos):
    del tad_doc[pos]
    return tad_doc

def print_doc(tad_doc):
    for i in range(len(tad_doc)):
        print(tad_doc[i]['paragrafo'])
        print()

def main():
    tad_doc = load_documento('paragrafo_texto.txt')
    print_doc(tad_doc)
    # print(tad_doc)
main()