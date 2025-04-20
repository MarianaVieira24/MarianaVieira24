def fechar_conta():
    numero = int(input("Número da mesa: "))
    if numero not in mesas or mesas[numero]['status'] != 'ocupada':
        print("Mesa inválida.")
        return

    total = calcular_conta(numero)
    print(f"\nTotal da mesa {numero}: R$ {total:.2f}")

    # Aplicar taxa ou desconto
    aplicar = input("Aplicar taxa de serviço de 10%? (s/n): ").lower()
    if aplicar == 's':
        taxa = total * 0.10
        total += taxa
        print(f"Taxa de serviço: R$ {taxa:.2f}")

    desconto = input("Deseja aplicar desconto? (s/n): ").lower()
    if desconto == 's':
        valor_desc = float(input("Valor do desconto: R$ "))
        total -= valor_desc
        print(f"Desconto aplicado: R$ {valor_desc:.2f}")

    print(f"Valor final: R$ {total:.2f}")
    
    dividir = input("Dividir conta entre clientes? (s/n): ").lower()
    if dividir == 's':
        clientes = len(mesas[numero]['clientes'])
        if clientes > 0:
            valor_individual = total / clientes
            print(f"Cada cliente paga: R$ {valor_individual:.2f}")
        else:
            print("Nenhum cliente registrado.")

    # Pagamento
    forma = input("Forma de pagamento (dinheiro/cartao): ").lower()
    if forma == "dinheiro":
        pago = float(input("Valor pago: R$ "))
        troco = pago - total
        if troco < 0:
            print("Valor insuficiente.")
            return
        print(f"Troco: R$ {troco:.2f}")
    else:
        print("Pagamento via cartão registrado.")

    # Fechar a mesa
    mesas[numero]['status'] = 'livre'
    mesas[numero]['clientes'] = []
    mesas[numero]['pedidos'] = []
    print("Mesa liberada. Pagamento concluído.")
