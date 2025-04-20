def menu_pagamentos():
    while True:
        print("\n-- Gestão de Pagamento --")
        print("1. Fechar Conta")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            fechar_conta()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
