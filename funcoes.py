def exibir_mensagem():
    print("Olá! Esta é uma função simples.")
    
def exibir_mensagem2(nome):
    print(f"seja bem vindo, {nome}!")
    
def exibir_mensagem3(nome = "vinicius"):
    print(f"seja bem vindo, {nome}!")
    
exibir_mensagem()
exibir_mensagem2(nome = "vinicius")
exibir_mensagem3()

def somar(a,b):
    return a + b

def subtrair(a, b):
    return a - b 

def expressão(a, b):
    return a * b + 30 - b + 10 

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação é = {resultado}")
    
exibir_resultado(100, 35, somar)
exibir_resultado(100, 35, subtrair)
exibir_resultado(100, 35, expressão)