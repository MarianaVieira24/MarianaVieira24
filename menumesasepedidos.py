def menu_mesas_pedidos():
    while True:
        print("\n-- Gestão de Mesas e Pedidos --")
        print("1. Cadastrar Mesa")
        print("2. Listar Mesas")
        print("3. Atribuir Clientes à Mesa")
        print("4. Registrar Pedido")
        print("5. Listar Pedidos")
        print("6. Atualizar Status do Pedido")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_mesa()
        elif opcao == "2":
            listar_mesas()
        elif opcao == "3":
            atribuir_clientes()
        elif opcao == "4":
            registrar_pedido()
        elif opcao == "5":
            listar_pedidos()
        elif opcao == "6":
            atualizar_status_pedido()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
