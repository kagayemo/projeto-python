from CadastroGeral import CadastroGeral
import os

def menu():
    cadastro_geral = CadastroGeral()
    titulo = "\n\n \033[34;1m== Sistema de Estoque ==\033[m \n\n"
    menuTexto = "[1] Cadastrar produto \n[2] Enviar produto ao estoque \n[3] Mostrar produtos \n[4] Deletar produto \n[5] Dar baixa no estoque \n[6] Sair \n\n========================\n" 
    
    print(titulo)
    print(menuTexto)
    opcaoMenu = int(input("Sua escolha: "))
    while(opcaoMenu != 6):
        if opcaoMenu == 1:
            os.system("cls") 
            cadastro_geral.cadastrar_produto()
        
        elif opcaoMenu == 2:
            os.system("cls")
            cadastro_geral.entrar_estoque()
        
        elif opcaoMenu == 3:
            os.system("cls")
            cadastro_geral.exibir_produtos()
            input("Pressione qualquer tecla para continuar... ")
        
        elif opcaoMenu == 4:
            os.system("cls")  
            cadastro_geral.deletar_produto()

        elif opcaoMenu == 5:
            os.system("cls")  
            cadastro_geral.baixa_estoque()  
    
        os.system("cls")
        print(titulo) 
        print(menuTexto)
        opcaoMenu = int(input("Sua escolha: "))

if __name__ == "__main__":
    menu()