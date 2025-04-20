cardapio = {}

def cadastrar_item_cardapio():
    nome = input("Nome do prato: ")
    descricao = input("Descrição: ")
    preco = float(input("Preço: "))
    ingredientes = input("Ingredientes (separados por vírgula): ").split(',')
    ingredientes = [i.strip() for i in ingredientes]
    cardapio[nome] = {
        'descricao': descricao,
        'preco': preco,
        'ingredientes': ingredientes
    }
    print("Item adicionado ao cardápio!")

def listar_cardapio():
    print("\n=== CARDÁPIO ===")
    for nome, dados in cardapio.items():
        print(f"{nome} - R$ {dados['preco']:.2f}\n  {dados['descricao']}\n  Ingredientes: {', '.join(dados['ingredientes'])}\n")
