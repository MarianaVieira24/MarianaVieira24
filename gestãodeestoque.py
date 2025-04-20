estoque = {}

def cadastrar_produto():
    codigo = input("Código do produto: ")
    if codigo in estoque:
        print("Produto já cadastrado.")
        return
    nome = input("Nome: ")
    quantidade = int(input("Quantidade: "))
    unidade = input("Unidade de medida: ")
    preco = float(input("Preço unitário: "))
    validade = input("Data de validade (dd/mm/aaaa): ")
    estoque[codigo] = {
        'nome': nome,
        'quantidade': quantidade,
        'unidade': unidade,
        'preco': preco,
        'validade': validade
    }
    print("Produto cadastrado com sucesso!")

def listar_estoque():
    print("\n=== ESTOQUE ===")
    for codigo, dados in estoque.items():
        print(f"{codigo} - {dados['nome']} | {dados['quantidade']} {dados['unidade']} | R$ {dados['preco']:.2f} | Vence: {dados['validade']}")

def atualizar_estoque():
    codigo = input("Código do produto a atualizar: ")
    if codigo not in estoque:
        print("Produto não encontrado.")
        return
    quantidade = int(input("Nova quantidade: "))
    estoque[codigo]['quantidade'] = quantidade
    print("Quantidade atualizada com sucesso!")
