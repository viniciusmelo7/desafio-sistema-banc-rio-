#texto = input("digite um texto: ")
#VOGAIS = "aeiouAEIOU"

#for letra in texto:
 #   if letra.upper() in VOGAIS:
  #      print(letra, end=" ")
        
#else:
 #   print("\nFim do loop")
  #  print("executa no final do texto")
    
    
#for numero in range(1, 11):
 #   print(numero)
    
    
#for numero in range(0,51,5):
 #   print(numero, end=" ")


opcao = 1 
    
while opcao != 0:
    opcao = int(input("[1] sacar \n[2] extrato \n[0] sair \n: "))
    
    if opcao == 1:
        print("sacando")
    elif opcao == 2:
        print("exibindo extrato")
        
    else:
        print("obrigado por usar nosso sistema bancario, volte sempre!")