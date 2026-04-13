saldo = 1000
saque = float(input("digite o valor do saque:"))

if saldo >= saque:
    print("saque realizado com sucesso")
else: 
    print("saldo insuficiente para realizar o saque")
    
maior_idade = 18
idade_especial = 12
idade = int(input("informe sua idade: "))    

if idade >= maior_idade:
    print("voce pode tirar a carteira de motorista")
    
elif idade == idade_especial:
    print("voce pode fazer as aulas teoricas da carteira de motorista")
    
else:
    print("voce nao pode tirar a carteira de motorista")