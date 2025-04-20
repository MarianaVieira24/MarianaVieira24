def calcular_conta(mesa_num):
    if mesa_num not in mesas or mesas[mesa_num]['status'] != 'ocupada':
        print("Mesa não encontrada ou está livre.")
        return 0

    total = 0
    for pedido in mesas[mesa_num]['pedidos']:
        for item in pedido['itens']:
            total += cardapio[item]['preco']
    return total
