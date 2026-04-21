#menu = """ 

#[d] = depositar
#[s] = sacar
#[e] = extrato
#[l] = consultar limites
#[q] = sair

#=> """

#saldo = 0
#extrato = ""
#numero_saques = 0 
#limite = 500
#LIMITE_SAQUES = 3 

#while True:
    
    #opcao = input(menu).lower().strip()
    
    # ================= DEPÓSITO =================
    #if opcao == "d":
        #try:
            #valor = float(input("Informe o valor de depósito: "))
        #except ValueError:
            #print("Entrada inválida! Digite um número.")
            #continue
        
        #if valor > 0:
            #saldo += valor
            #extrato += f"Depósito: R$ {valor:.2f}\n"
            #print("Depósito realizado com sucesso!")
        #else:
            #print("Operação falhou! Valor inválido.")
    
    
    # ================= SAQUE =================
    #elif opcao == "s":
        #try:
            #valor = float(input("Informe o valor do saque: "))
        #except ValueError:
            #print("Entrada inválida! Digite um número.")
            #continue
        
        #excedeu_saldo = valor > saldo
        #excedeu_limite = valor > limite
        #excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        #if excedeu_saldo:
            #print("Operação falhou! Saldo insuficiente.")
            
        #elif excedeu_limite:
            #print("Operação falhou! Valor excede o limite por saque.")
            
        #elif excedeu_saques:
            #print("Operação falhou! Número máximo de saques excedido.")
        
        #elif valor > 0:
            #saldo -= valor
            #extrato += f"Saque: R$ {valor:.2f}\n"
            #umero_saques += 1
            
            #print("Saque realizado com sucesso!")
            
        #else:
            #print("Operação falhou! Valor inválido.")
    
    
    # ================= LIMITES =================
    #elif opcao == "l":
        #print("\n================ LIMITES ================")
        #print(f"Limite por saque: R$ {limite:.2f}")
        #print(f"Saques restantes: {LIMITE_SAQUES - numero_saques}")
        #print("=========================================\n")
    
    
    # ================= EXTRATO =================
    #elif opcao == "e":
        #print("\n================ EXTRATO ================")
        #if not extrato:
            #print("Não foram realizadas movimentações.")
        #else:
            #print(extrato)
        #print(f"Saldo: R$ {saldo:.2f}")
        #print("=========================================\n")
    
    
    # ================= SAIR =================
    #elif opcao == "q":
        #print("Saindo do sistema...")
        #break
    
    
    # ================= OPÇÃO INVÁLIDA =================
    #else:
        #print("Opção inválida, tente novamente.")
        
 #=========================== FIM DO PROGRAMA ================================       


import textwrap   

def menu():
    menu = """\n
    =================== MENU ========================
    [d]\tdepositar
    [s]\tsacar
    [e]\textrato
    [nc]\tnova conta
    [nu]\tnovo usuário
    [q]\tsair
    [lc]\tlistar contas
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n  Depósito realizado com sucesso!  ")
    else:
        print("\n  Operação falhou! Valor inválido.  ")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques 
    if excedeu_saldo:
        print("\n  Operação falhou! Saldo insuficiente.  ")
        
    elif excedeu_limite:
        print("\n  Operação falhou! Valor excede o limite por saque.  ")
        
    elif excedeu_saques:
        print("\n  Operação falhou! Número máximo de saques excedido.  ")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n  Saque realizado com sucesso!  ")
    else:
        print("\n  Operação falhou! Valor inválido.  ")
        
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato) 
    print(f"Saldo: R$ {saldo:.2f}")
    print("=========================================")
    
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n  Já existe usuário com esse CPF!  ")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("\n  Usuário criado com sucesso!  ")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        print("\n  Conta criada com sucesso!  ")
        return conta
    else:
        print("\n  Usuário não encontrado, fluxo de criação de conta encerrado!  ")
        return None
    

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            agencia:\t{conta['agencia']}
            conta:\t\t{conta['numero_conta']}
            titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main ():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0 
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=500,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta= criar_conta(AGENCIA, numero_conta, usuarios) 
            
            if conta:
                contas.append(conta)
                
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "q":
            print("\n  Obrigado por usar nosso sistema bancário, volte sempre!  ")
            break
            
        else:
            print("\n  Operação inválida, por favor selecione novamente a operação desejada.  ")
            
main()
    