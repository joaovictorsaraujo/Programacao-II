def tadpessoa(nome, peso, altura, idade):
    pessoa = {'nome':nome, 'peso':peso, 'altura':altura, 'idade':idade}
    return pessoa

def maiorIdade(tadpessoa):
    return tadpessoa['idade'] >= 18

def imc(tadpessoa):
    imc = tadpessoa['peso'] / (tadpessoa['altura'] ** 2)
    return imc

def getNome(tadpessoa):
    return tadpessoa['nome']

def getPeso(tadpessoa):
    return tadpessoa['peso']

def getAltura(tadpessoa):
    return tadpessoa['altura']

def getIdade(tadpessoa):
    return tadpessoa['idade']
