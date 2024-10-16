import textwrap

def menu():
    menu ="""\n       
      ---------- MENU ----------
      (d)\tDepositar
      (s)\tSacar
      (e)\tExtrato
      (c)\tCriar Conta
      (l)\tListar Contas
      (u)\tCriar Usuário
      (q)\tSair
      :"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):    
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R${valor:.2f}\n"
        print("\nDepósito efetuado com sucesso!")
            
    else:
        print("\nOperação Inválida, o valor digitado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, nSaques, lSaques):
    excedSaldo = valor > saldo
    excedLimite = valor > limite
    excedLSaques = nSaques >= lSaques

    if excedSaldo:
        print("\nA Operação não foi concluída, você não tem saldo suficiente!")
    elif excedLimite:
        print("\nA Operação não foi concluída, o valor de saque excedeu o limite!")
    elif excedLSaques:
        print("\nA Operação não foi concluída, você excedeu o limite de saques diários!")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        nSaques += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\nOperação Inválida, o valor digitado é inválido.")
    
    return saldo, extrato

def exbExtrato(saldo, /, *, extrato):
    print("\n---------- EXTRATO ----------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("-------------------------------")


def criarUsuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário cadastrado com esse CPF!")
        return
    nome = input("Digite o Nome Completo: ")
    dNascimento = input("Digite a Data de Nascimento(dd/mm/aaaa): ")
    endereco = input("Digite o Endereço(logradouro, nro - bairro - cidade/UF estado): ")
    usuarios.append({"nome": nome, "Data_Nascimento": dNascimento, "CPF": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrarUsuario(cpf, usuarios):
    usuariosFiltrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    return usuariosFiltrados[0] if usuariosFiltrados else None

def criarConta(agencia, nConta, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com Sucesso!")
        return {"agencia": agencia, "nConta": nConta, "usuario": usuario}

    print("Usuário Não Encontrado")

def listarContas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['nConta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LSAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    nSaques = 0
    usuarios = []
    contas = []
    nConta = 0

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Digite o Valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Digite o Valor do saque: "))

            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, nSaques=nSaques, lSaques=LSAQUES,)
        
        elif opcao == "e":
            exbExtrato(saldo, extrato=extrato)
        
        elif opcao == "u":
            criarUsuario(usuarios)

        elif opcao == "c":
            conta = criarConta(AGENCIA, nConta, usuarios)
            
            if conta:
                contas.append(conta)
                nConta += 1

        elif opcao == "l":
            listarContas(contas)
        
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor digite novamente a operação desejada.")

main()
