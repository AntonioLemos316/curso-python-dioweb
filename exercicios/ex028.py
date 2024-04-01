menu = """

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "0":

        deposito = float(input("Informe um valor para depôsitar R$"))
        print(f"Valor de R${deposito:.2f} depôsitado!" if deposito > 0 else "Valor inválido!")
        extrato += f"Depôsito: R${deposito:.2f}\n"
        saldo += deposito 

    elif opcao == "1":

        if saldo <= 0:
            print(f"Você não tem Saldo... \nSaldo atual R${saldo:.2f}")
            continue

        if numero_saques == LIMITE_SAQUES:
            print("Limite de saques excedidos")
            continue

        saque = float(input("Informe um valor para sacar R$"))
        if saque > limite or saque <= 0:
            print(f"Valor inválido")
            continue

        else:
            print(f"Valor sacado R${saque}")
        extrato += f"Saque: R${saque:.2f}\n"
        saldo -= saque
        numero_saques += 1
        
    elif opcao == "2":
        if not extrato:
            print('Não há extrato atualmente')
        else:
            print(extrato)
            print(f'Atualmente seu saldo é: R${saldo:.2f}')

    elif opcao == "3":
        break

    else:
        print("Digite uma opção válida!")

