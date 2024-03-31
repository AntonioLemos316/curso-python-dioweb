while True:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibir o extrato...")
    elif opcao == 0:
        break

print("Obrigado por utilizar nosso Sistema")