from Produto import Produto
from ProdutoEstoque import ProdutoEstoque
from Validacao import verificar_strings, verificar_float, validar_led, verificar_quantidade, verificar_inteiro
import os

class CadastroGeral:
    def __init__(self):
        self.__lista_produto = []
        self.__estoque = []
        self.__count_produtos = 0

    def cadastrar_produto(self):
        os.system("cls")
        print("\n\n\033[34;1m=== Cadastrar Produto === \033[m\n\n")
        self.__count_produtos += 1

        id = self.__count_produtos 
        nome = verificar_strings(input("Digite o nome do produto: "), "(\s+)?([a-zA-Z0-9]{3,30}\s?)+", "Digite somente caracteres alfanumericos!")
        preco = verificar_float("Digite o preço do produto: R$")
        marca = verificar_strings(input("Digite a marca do produto: "), "(\s+)?([a-zA-Z0-9]{3,30}\s?)+", "Digite somente caracteres alfanumericos!")
        led = validar_led("Tem led? (S, N): ")
        categoria = verificar_strings(input("Digite a categoria do produto: "), "(\s+)?([a-zA-Z]{3,30}\s?)+", "Digite somente caracteres!")
        produto = Produto(id, nome, preco, marca, led, categoria)

        self.__lista_produto.append(produto)

    def entrar_estoque(self):
        os.system("cls")
        print("\n\n\033[34;1m=== Entrar Produto no Estoque === \033[m\n\n")

        if len(self.__lista_produto) > 0:
            produto_escolhido = self.pesquisar_produto()

            produto_estoque = ProdutoEstoque()
            if len(self.__estoque) > 0:
                jaExiste = False
                for produto in self.__estoque:
                    if produto.get_produto() == produto_escolhido:
                        jaExiste = True   
                        break
                self.pedir_valores_estoque(produto_estoque, produto_escolhido, jaExiste)
            else:
                self.pedir_valores_estoque(produto_estoque, produto_escolhido, False)
        else:
            print("\033[31;1mNão há produtos cadastrados!\033[m")
        

    def pedir_valores_estoque(self, objeto, produto, jaExiste):
        if not jaExiste:
            objeto.set_produto(produto)
            quantidade_minima = verificar_inteiro("Digite a quantidade mínima no estoque: ")
            objeto.set_quantidade_minima(quantidade_minima)
            objeto.set_quantidade(verificar_quantidade(verificar_inteiro("Digite a quantidade que deseja enviar ao estoque: "), quantidade_minima), False)

            self.__estoque.append(objeto)
        else:
            for produto_estoque in self.__estoque:
                if produto_estoque.get_produto() == produto:
                    produto_estoque.set_quantidade(int(input("Digite a quantidade: ")), False)
                    break


    def exibir_produtos(self):
        os.system("cls") 
        print("\033[34;1m=== Lista de Produtos === \033[m\n\n")

        for produto in self.__lista_produto:
            print(f"ID do produto: {produto.get_id()}")
            print(f"Nome do produto: {produto.get_nome()}")
            print(f"Preço: R${produto.get_preco()}")
            print(f"Marca: {produto.get_marca()}")
            print(f"Led: {produto.get_led()}")
            print(f"Categoria: {produto.get_categoria()}")
            
            for quantidade in self.__estoque:
                if produto.get_id() == quantidade.get_produto().get_id():
                    print(f"Quantidade em estoque: {quantidade.get_quantidade()}")
                    print(f"Quantidade mínima: {quantidade.get_quantidade_minima()}")
                    
                    if quantidade.get_quantidade() < quantidade.get_quantidade_minima():
                        print("\033[31;1mESTE PRODUTO PRECISA SER COMPRADO!!\033[m")
                    break   
            print("\n") 
    
    def pesquisar_produto(self):
        while True:
            for produto in self.__lista_produto:
                print(f"Id: {produto.get_id()} \nNome: {produto.get_nome()} \n") 
            
            escolha_usuario = int(input("Digite o ID: "))
            
            produto_escolhido = None
            for produto in self.__lista_produto:
                if produto.get_id() == escolha_usuario:
                    produto_escolhido = produto
                    return produto_escolhido
            print("\033[31;1mDigite um id válido!!\033[m")       
        

    def baixa_estoque(self):
        os.system("cls")
        print("\n\n\033[34;1m=== Baixar Produto em Estoque === \033[m\n\n")
        if len(self.__lista_produto) > 0 and len(self.__estoque) > 0:
            produto_baixa = self.pesquisar_produto()

            quantidade_baixa = verificar_inteiro("Digite a quantidade: ")
            for produto_estoque in self.__estoque: 
                if produto_estoque.get_produto() == produto_baixa:
                    if produto_estoque.get_quantidade() == 0 or (produto_estoque.get_quantidade() - quantidade_baixa <= 0):
                        self.__estoque.remove(produto_estoque)
                        break

                    produto_estoque.set_quantidade(quantidade_baixa, True)
                    
        else:
            print("\033[31;1mNão há produtos cadastrados!\033[m")


    def deletar_produto(self):
        os.system("cls")
        print("\n\n\033[34;1m=== Deletar Produto === \033[m\n\n") 
        if len(self.__lista_produto) > 0:
            produto_escolhido = self.pesquisar_produto()
            self.__lista_produto.remove(produto_escolhido)
            return
        else:
            print("\033[31;1mNão há produtos cadastrados\033[m")
