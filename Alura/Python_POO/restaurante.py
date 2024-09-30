import os

dados_coffee = [{"nome": "Tacos", "categoria": "mexicana", "ativo": False},
                {"nome": "coffee demo", "categoria": "bolos", "ativo": True},
                {"nome": "fogo de chao", "categoria": "rodizio", "ativo": False}]

def nome_programa():
    print("""
    COFFEE DEMO      
    """)             

def exibir_opcoes():

    print("1.Cadastrar Coffee")
    print("2.Listar Coffee")
    print("3.Ativar coffee")
    print("4.Sair\n ")

def exibir_subtitulo(texto):
    os.system("clear")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizando_app():
    exibir_subtitulo("Finalizado App")

def voltar_ao_menu():
    input("\nDigite uma tecla para voltar ao menu: ")
    main()
    
def opçao_invalida():
    print("Erro! Opçao invalida.\n")
    voltar_ao_menu()

def estado_do_coffee():
    exibir_subtitulo("Alterando o estado do restaurante")
    nome_coffee = input("Digite o nome do coffee que deseja alterar o estado: ")            
    coffee_encontrado = False

    for coffee in dados_coffee:
        if nome_coffee == coffee["nome"]:
            coffee_encontrado = True  
            coffee["ativo"] = not coffee["ativo"]
            mensagem = f"O coffee {nome_coffee} foi ativado com sucesso!" if coffee["ativo"] else f"O coffee {nome_coffee} foi destivado com sucesso!"
            print(mensagem)
    if not coffee_encontrado:
        print("O coffee nao foi encontrado!")
    voltar_ao_menu()

def listando_coffee():
    exibir_subtitulo("Listando os cofees")

    print(f"{"nome do coffee".ljust(23)} | {"categoria do coffee".ljust(20)} | status")

    for coffee in dados_coffee:
        nome_coffee = coffee["nome"]
        categoria_coffee = coffee["categoria"]
        ativo_coffee = "Ativado" if coffee["ativo"] else "desativado"
        print(f"-> {nome_coffee.ljust(20)} | {categoria_coffee.ljust(20)} | {ativo_coffee}")

    voltar_ao_menu()


def cadastrar_coffee():
    exibir_subtitulo("Cadastrando novos coffees")

    nome_do_coffee = input("digite o nome do caffe: ")
    categoria_coffee = input(f"Digite a categoria do coffee {nome_do_coffee}: ")
    dic_coffee = {"nome":nome_do_coffee, "categoria":categoria_coffee, "ativo":False} 
    dados_coffee.append(dic_coffee)
    print(f"O {nome_do_coffee} foi cadastrado com sucesso\n")
    voltar_ao_menu()

def opçoes_do_usuario():                        
    try:
        usuario = int(input("Sua escolha: "))

        if usuario == 1:
            cadastrar_coffee()  
        elif usuario == 2:
            listando_coffee()
        elif usuario == 3:  
            estado_do_coffee()
        elif usuario == 4:
            finalizando_app()
        else:
            opçao_invalida()
    except: 
        opçao_invalida()

def main():
    os.system("clear")
    nome_programa()
    exibir_opcoes()
    opçoes_do_usuario()
    opçao_invalida  
if __name__ == "__main__":  
    main()

