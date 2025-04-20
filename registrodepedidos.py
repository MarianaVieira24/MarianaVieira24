def registrar_pedido():
    numero = int(input("Número da mesa: "))
    if numero not in mesas or mesas[numero]['status'] == 'livre':
        print("Mesa inválida ou sem clientes.")
        return
    itens = []
    while True:
        listar_cardapio()
        item = input("Digite o nome do prato (ou 'fim' para concluir): ")
        if item == 'fim':
            break
        if item not in cardapio:
            print("Item não encontrado no cardápio.")
        else:
            itens.append(item)

    pedido = {'mesa': numero, 'itens': itens, 'status': 'recebido'}
    pedidos.append(pedido)
    mesas[numero]['pedidos'].append(pedido)
    print("Pedido registrado e enviado à cozinha.")

def listar_pedidos():
    print("\n=== PEDIDOS ===")
    for i, pedido in enumerate(pedidos):
        print(f"{i+1}. Mesa {pedido['mesa']} | Itens: {', '.join(pedido['itens'])} | Status: {pedido['status']}")

def atualizar_status_pedido():
    listar_pedidos()
    i = int(input("Número do pedido a atualizar: ")) - 1
    if i < 0 or i >= len(pedidos):
        print("Pedido inválido.")
        return
    print("1. Em preparo\n2. Pronto para servir")
    opcao = input("Novo status: ")
    if opcao == '1':
        pedidos[i]['status'] = 'em preparo'
    elif opcao == '2':
        pedidos[i]['status'] = 'pronto'
    else:
        print("Opção inválida.")
