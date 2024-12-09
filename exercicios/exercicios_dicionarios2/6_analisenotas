def analisa_notas(alunos):
    aprovados = []
    for aluno in alunos:
        notas = alunos[aluno]
        if sum(notas) / len(notas) > 7:
            aprovados.append(aluno)
    return aprovados

def main():
    dic = {'João':[10, 7, 8], 'Laysla':[6, 7, 5], 'Carol':[10, 10, 10]}
    resultado = analisa_notas(dic)
    if resultado == '':
        print('Nenhum aluno acima da média de pontos')
    else:
        for i in resultado:
            print(f'O(A) aluno(a) {i} foi aprovado!')
main()