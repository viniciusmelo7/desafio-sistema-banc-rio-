nome = "VInicIus"
print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "    olá seja bem vindo!    "
print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"

print("####" +menu + "####")
print(menu.center(20))
print(menu.center(20, "#"))
print("-".join(menu))
####################PARTE 2 DA AULA####################################

nome = "Vinicius"
idade = 20
profissao = "desenvolvedor backend"
linguagem = "python"

dados = {"nome": "Vinicius", "idade": 20}

print("nome: %s idade: %d" % (nome, idade))
print("nome: {} idade: {} ".format(nome,idade))
print("nome: {1} idade: {0}" .format(idade, nome))
print("nome: {name} idade: {age}" .format(age=idade,name=nome))
print("nome: {nome} idade: {idade}" .format(idade=idade,nome=nome))
print("nome: {nome} idade: {idade}" .format(**dados))
