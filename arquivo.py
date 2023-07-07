menu = """
[A] Depositar
[B] Sacar
[C] Extrato
[D] Sair
"""

saldo = 0
extrato = ""
numero_saques = 0
limite_saques = 3
limite = 500

while True:

    opcao = input(menu)

    if opcao == "a":
        valor = float(input("qual valor deseja depositar? "))
        if valor > 0:
            saldo += valor
            extrato += f"depósito: R$ {valor:.2f}\n"
        else:
            print("o depósito falhou, escolha um valor válido.")
    
    elif opcao == "b":
        valor = float(input("Digite o valor do saque: R$"))
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
        else:
            print("operação falhou.")

    elif opcao == "c":
        print("\n=========extrato========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo R${saldo:.2f}")
        print("===========================")
    
    elif opcao == "d":
        break 

    else:
        print("operação inválida, por favor selecione uma nova opção.")


"""nesse código é possível fazer depósitos, sacar até 3x qualquer valor que 
não ultrapasse 500.00 e registrar as ações."""