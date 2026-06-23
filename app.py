import os

def exibir_nome_do_programa():
    print("Sabor Express\n")


def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Ativar Restaurante")
    print("4. Sair\n")

def finalizar_app():
    os.system("cls")
    print("Finalizando o APP!\n")


def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opcão: "))
    match opcao_escolhida:
        case 1:
            print("Cadastrar restaurante")    
        case 2:
            print("Listar restaurantes")    
        case 3:
            print("Ativar restaurante")   
        case _:
           finalizar_app() 


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()