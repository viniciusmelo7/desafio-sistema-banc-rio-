pessoa = {"nome": "vinicius" , "idade": 20}

pessoa["profissao"] = "desenvolvedor backend"

print(pessoa)

dados = {"nome": "vinicius", "idade": 20, "profissao": "desenvolvedor backend"}
print(dados["nome"])

for chave, valor in dados.items():
    print(chave, valor)
    
    
novo_dicionario = {"nome": "cristiano ronaldo", "teste": 41, "b" : "python"}
print(novo_dicionario.keys())
print(novo_dicionario.values())
resultado = "messi" in novo_dicionario
print(resultado)
