import os

print("Sabor Express\n")

print("1. Cadastrar Restaurante")
print("2. Listar Restaurante")
print("3. Ativar Restaurante")
print("4. Sair\n")


opcao_escolhida = int(input("Escolha uma opcão: "))

def finalizar_app():
    os.system("cls")
    print("Encerrando o Programa\n")




if opcao_escolhida == 1 :
    print("Cadastrar restaurante")    
elif opcao_escolhida == 2 :
    print("Listar restaurantes")    
elif opcao_escolhida == 3 :
    print("Ativar restaurante")
else:
    finalizar_app()