print(" CALCULADORA ")

while True:
    print("\nEscolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = input("Digite o número da operação: ")

    if opcao == "5":
        print("Encerrando calculadora...")
        break

    elif opcao in ["1", "2", "3", "4"]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = num1 + num2
            print("Resultado:", resultado)

        elif opcao == "2":
            resultado = num1 - num2
            print("Resultado:", resultado)

        elif opcao == "3":
            resultado = num1 * num2
            print("Resultado:", resultado)

        elif opcao == "4":
            if num2 != 0:
                resultado = num1 / num2
                print("Resultado:", resultado)
            else:
                print("Erro: divisão por zero")

    else:
        print("Opção inválida!")