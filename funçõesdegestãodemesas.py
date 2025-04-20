def cadastrar_mesa():
    numero = int(input("Número da mesa: "))
    if numero in mesas:
        print("Mesa já cadastrada.")
        return
    capacidade = int(input("Capacidade de pessoas: "))
    mesas[numero] = {
        'capacidade': capacidade,
        'status': 'livre',
        'clientes': [],
        'pedidos': []
    }
    print("Mesa cadastrada com sucesso.")

def listar_mesas():
    print("\n=== MESAS ===")
    for numero, dados in mesas.items():
        print(f"Mesa {numero} | Cap: {dados['capacidade']} | Status: {dados['status']}")

def atribuir_clientes():
    numero = int(input("Número da mesa: "))
    if numero not in mesas:
        print("Mesa não encontrada.")
        return
    if mesas[numero]['status'] != 'livre':
        print("Mesa já ocupada.")
        return
    qtd = int(input("Quantidade de clientes: "))
    mesas[numero]['clientes'] = [f"Cliente {i+1}" for i in range(qtd)]
    mesas[numero]['status'] = 'ocupada'
    print("Clientes atribuídos à mesa.")
