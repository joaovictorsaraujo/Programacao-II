import exercicios.exercicios_tad.exercicio_01.tadpessoa as td
def abre_arq(nome_arq):
    arq = open(nome_arq, 'rt')
    pessoa = arq.readline()
    
    lista =[]
    while pessoa != '':
        pessoa = pessoa.strip().split(', ')
        lista.append(td.tadpessoa(pessoa[0], int(pessoa[2]), float(pessoa[3]), int(pessoa[1])))
        pessoa = arq.readline()
    return lista

def main():
    tadpessoa = abre_arq("dados.txt")
    print(f"{'Nome:':<16}{'Idade:':<19}{'Peso:':<18}{'Altura:':<19}{'IMC:'}")
    for pessoa in tadpessoa:
        if td.getIdade(pessoa):
            print(f"{td.getNome(pessoa):<18}{td.getIdade(pessoa):<17}{td.getPeso(pessoa)}{'kg':<17}{td.getAltura(pessoa):<18}{td.imc(pessoa):.1f}")
main()
