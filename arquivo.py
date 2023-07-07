import textwrap

def menu():
    menu = """\n
    ----------MENU----------
    [A]\tDepositar
    [B]\tSacar
    [C]\tExtrato
    [NC]\tNova conta
    [LC]\tListar contas
    [NU]\tNovo usuário
    [D]\tSair
    ==> """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato == f"depósito:\tR$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("Valor informado inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo 
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= limite_saques
    if excedeu_saldo:
        print("Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("seu saque excede o limite.")
    elif excedeu_saque:
        print("número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com successo!")
    else:
        print(" \noperação falhou.")
    return saldo, extrato        

def exibir_extrato(saldo, /, *, extrato):
    print("\n ==========EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else  extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=" *30)

def criar_usuario(usuarios):
    cpf = input("informe o CPF(apenas números): ")
    usuario = filtrar_usuario (cpf, usuario)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("informe o nome completo: ")
    data_nascimento = input("informe a data de nascimento(dd-mm-aaaa): ")
    endereco = print("informe o endereço(logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado! Fluxo de criação de conta cancelado.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_contas']}
            titular:\t{conta['usuario']['nome']}
        """
        print("=" *100)
        print(textwrap.dedent(linha))

def main():
    saldo = 0
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    limite = 500
    agencia = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "a":
            valor = float(input("qual valor deseja depositar? "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "b":
            valor = float(input("Digite o valor do saque: R$"))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = limite_saques,
            )

        elif opcao == "c":
            exibir_extrato(saldo, ectrato = extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(conta) +1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                conta.append(conta)

        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "d":
            break 

        else:
            print("operação inválida, por favor selecione uma nova opção.")

main()