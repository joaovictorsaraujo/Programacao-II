def criar_estoque():
    estoque = []
    return estoque

def adicionar_produto(estoque, nome, qtd, preço):
    produto = {'nome': nome, 'quantidade': int(qtd), 'preço': float(preço)}
    estoque.append(produto)
    return estoque

def listar_produtos(estoque):
    lst = []
    for produto in estoque:
        lst.append(produto['nome'])
    return lst

def quant_produto(estoque, nome):
    for produto in estoque:
        if produto['nome'] == nome:
            return produto['quantidade']

def valor_total_estoque(estoque):
    lst = []
    for produto in estoque:
        prod = []
        prod.append(produto['nome'])
        prod.append(produto['quantidade'] * produto['preço'])
        lst.append(prod)
    return lst

def atualizar_quantidade(estoque, nome, nova_quant):
    for produto in estoque:
        if produto['nome'] == nome:
            produto['quantidade'] = nova_quant
    return estoque

def remover_produto(estoque, nome):
    for i in range(len(estoque)):
        if estoque[i]['nome'] == nome:
            x = i
    del estoque[x]    
    return estoque

def main():
    e = criar_estoque()
    print(adicionar_produto(e, 'camarão', '20', '33.3'))
    print(adicionar_produto(e, 'arroz', '30', '25.0'))
    print(listar_produtos(e))
    print(quant_produto(e, 'camarão'))
    print(valor_total_estoque(e))
    print(atualizar_quantidade(e, 'camarão', 25))
    print(remover_produto(e, 'camarão'))
main()