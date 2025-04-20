def menu_principal():
    while True:
        print("\n==== MENU PRINCIPAL ====")
        print("1. Gestão de Estoque")
        print("2. Gestão do Cardápio")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_estoque()
        elif opcao == "2":
            menu_cardapio()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

def menu_estoque():
    while True:
        print("\n-- Gestão de Estoque --")
        print("1. Cadastrar Produto")
        print("2. Listar Estoque")
        print("3. Atualizar Estoque")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_estoque()
        elif opcao == "3":
            atualizar_estoque()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def menu_cardapio():
    while True:
        print("\n-- Gestão do Cardápio --")
        print("1. Cadastrar Item")
        print("2. Listar Cardápio")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_item_cardapio()
        elif opcao == "2":
            listar_cardapio()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
