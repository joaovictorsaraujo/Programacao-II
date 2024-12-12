import tadpessoa as td
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
    for pessoa in tadpessoa:
        if td.getIdade(pessoa):
            print(f'Nome: {td.getNome(pessoa)}, Idade: {td.getIdade(pessoa)}, Peso: {td.getPeso(pessoa)}, Altura: {td.getAltura(pessoa)}, IMC: {td.imc(pessoa):.3f}')
main()
