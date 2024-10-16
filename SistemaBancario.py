menu = """       Menu
      
      (d) Depositar
      (s) Sacar
      (e) Extrato
      (q) Sair
      """


saldo = 0
limite = 500
extrato = ""
nSaques = 0
lSaques = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Digite o valor que deseja depositar:"))
    
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R${valor:.2f}\n"
            print("Depósito efetuado com sucesso!")
            
        else:
            print("Operação Inválida, o valor digitado é inválido.")
            

    elif opcao == "s":
        valor = float(input("Digite o valor que deseja sacar:"))

        excedSaldo = valor > saldo
        excedLimite = valor > limite
        excedLSaques = nSaques >= lSaques

        if excedSaldo:
            print("A Operação não foi concluída, você não tem saldo suficiente!")
        elif excedLimite:
            print("A Operação não foi concluída, o valor de saque excedeu o limite!")
        elif excedLSaques:
            print("A Operação não foi concluída, você excedeu o limite de saques diários!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            nSaques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação Inválida, o valor digitado é inválido.")

    elif opcao == "e":
        print("\n---------- EXTRATO ----------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-------------------------------")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor digite novamente a operação desejada.")