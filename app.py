import os

restaurantes = [{'nome':'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome':'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome':'Cantina', 'categoria': 'Italiano', 'ativo': False}];

def exibir_nome_do_programa():
    '''
    Exibir o nome do programa
    '''
    print("Sabor Express\n")


def exibir_opcoes():
    '''
    Exibe as opções disponíveis no menu principal
    '''
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Alternar estado do Restaurante")
    print("4. Sair\n")

def finalizar_app():
    '''
    Exibe mensagem de finalizando o app
    '''
    exibir_subtitulo("Finalizando APP!")

def voltar_ao_menu_principal():
    '''
    Solicita um tecla para voltar ao menu principal

    Outputs:
    - Retorna ao menu principal
    '''
    input("\nDigite uma tecla para voltar ao menu principal: ")    
    main()

def opcao_invalida():
    '''
    Exibe a mensagem inválida e retorna para o menu principal

    Outputs:
    - Retorna ao menu principal

    '''
    print("Opção inválida!\n")
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    '''
    Exibe um subtítulo personalizado na tela

    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)

    print()

def cadastrar_novo_restaurante():
    '''
    Essa funçao é responsavel por cadastrar os novos restaurantes

    Inputs:
    - Nome do restaurante
    - Categoria

    Outpus:
    - Adicionar um nome restaurante a lista de restaurantes
    '''
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria_do_restaurante = input(f"Digite a categoria do restaurante {nome_do_restaurante} que deseja cadastrar: ")
    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria_do_restaurante, 'ativo':False}

    restaurantes.append(dados_do_restaurante)

    print(f"O restaurante {nome_do_restaurante} | {categoria_do_restaurante} | foi cadastrado com sucesso!")
    voltar_ao_menu_principal()


def alternar_estado_do_restaurante():
    '''
    Altera o estado do restaurante ativado/destivado

    Outpus:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alternando estado do restaurante')

    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O Restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O Restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')



    voltar_ao_menu_principal()

def listar_restaurantes():
    '''
    Lista os restaurantes que estão da lista

    Outputs:
    - Exibe lista de restaurantes na tela
    '''
    exibir_subtitulo("Listando os restaurantes")


    print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | {'Status'}')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else "Desativado"

        print(f" - {nome_restaurante.ljust(20) } | {categoria.ljust(20)} | {ativo}")
        
    voltar_ao_menu_principal()

def escolher_opcao():
    '''
    Solicita e executa a opção escolhida pelo usuário

    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input("Escolha uma opcão: "))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()  
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_do_restaurante()
            case 4:
                finalizar_app() 
            case _:
                opcao_invalida()
    except:
       opcao_invalida()
  

def main():
    '''
    Função principal que inicia o programa
    '''
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()

