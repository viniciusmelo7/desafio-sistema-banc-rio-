menu = """ 

[d] = depositar
[s] = sacar
[e] = extrato
[l] = consultar limites
[q] = sair

=> """

saldo = 0
extrato = ""
numero_saques = 0 
limite = 500
LIMITE_SAQUES = 3 

while True:
    
    opcao = input(menu).lower().strip()
    
    # ================= DEPÓSITO =================
    if opcao == "d":
        try:
            valor = float(input("Informe o valor de depósito: "))
        except ValueError:
            print("Entrada inválida! Digite um número.")
            continue
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! Valor inválido.")
    
    
    # ================= SAQUE =================
    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))
        except ValueError:
            print("Entrada inválida! Digite um número.")
            continue
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
            
        elif excedeu_limite:
            print("Operação falhou! Valor excede o limite por saque.")
            
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
            print("Saque realizado com sucesso!")
            
        else:
            print("Operação falhou! Valor inválido.")
    
    
    # ================= LIMITES =================
    elif opcao == "l":
        print("\n================ LIMITES ================")
        print(f"Limite por saque: R$ {limite:.2f}")
        print(f"Saques restantes: {LIMITE_SAQUES - numero_saques}")
        print("=========================================\n")
    
    
    # ================= EXTRATO =================
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("=========================================\n")
    
    
    # ================= SAIR =================
    elif opcao == "q":
        print("Saindo do sistema...")
        break
    
    
    # ================= OPÇÃO INVÁLIDA =================
    else:
        print("Opção inválida, tente novamente.")