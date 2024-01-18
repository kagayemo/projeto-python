from Produto import Produto
from ProdutoEstoque import ProdutoEstoque
from Validacao import verificar_strings, verificar_float, validar_led, verificar_quantidade, verificar_inteiro, validar_categoria
from EscritorioGamer import EscritorioGamer
from Hardware import Hardware
from Perifericos import Perifericos
import os
from time import sleep

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
        categoria = self.selecionar_categoria()

        if categoria == 1:
            self.cadastrar_escritorio(id, nome, preco, marca, led)
        elif categoria == 2:
            self.cadastrar_hardware(id, nome, preco, marca, led)
        else:
            self.cadastrar_perifericos(id, nome, preco, marca, led)

    def selecionar_categoria(self):
        categorias = ["Escritorio", "Hardware", "Perifericos"]
        print()
        for categoria in categorias:
            print(f"[{categorias.index(categoria)+1}] - {categoria}")
        print()

        categoria_escolhida = validar_categoria()

        return categoria_escolhida

    def cadastrar_hardware(self, *valores):
        portas = verificar_float("Digite a quantidade de portas: ")
        consumo_energia = verificar_float("Digite o consumo de energia: ")
        armazenamento = verificar_float("Digite o armazenamento do produto: ")

        hardware = Hardware(portas, consumo_energia, armazenamento, *valores)
        self.__lista_produto.append(hardware)

    def cadastrar_perifericos(self, *valores):
        entradas = verificar_strings(input("Digite a entrada do periférico: "), "(\s+)?([a-zA-Z0-9]{3,30}\s?)+", "Digite somente caracteres alfanumericos!")
        bluetooth = validar_led("Possuí bluetooth? (S, N): ")
        material = verificar_strings(input("Digite o material do produto: "),"(\s+)?([a-zA-Z0-9]{3,30}\s?)+", "Digite somente caracteres alfanumericos!")
        
        item_periferico = Perifericos(entradas, bluetooth, material, *valores)
        self.__lista_produto.append(item_periferico)

    def cadastrar_escritorio(self, *valores):
        largura = verificar_float("Digite a largura do produto: ")
        altura = verificar_float("Digite a altura do produto: ")
        cor = verificar_strings(input("Digite a cor do produto: "),"(\s+)?([a-zA-Z0-9]{3,30}\s?)+", "Digite somente caracteres alfanumericos!")
        
        item_escritorio = EscritorioGamer(largura, altura, cor, *valores)
        self.__lista_produto.append(item_escritorio) 

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
        if len(self.__lista_produto) > 0:
            for produto in self.__lista_produto:
                print(f"ID: {produto.get_id()}")
                print(f"Nome: {produto.get_nome()}")
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

                if produto.get_categoria() == "Hardware":
                    print(f"Portas: {produto.get_portas()}")
                    print(f"Armazenamento: {produto.get_armazenamento()}")
                    print(f"Consumo: {produto.get_consumo()}")

                elif produto.get_categoria() == "Perifericos":
                    print(f"Entradas: {produto.get_entradas()}")
                    print(f"Bluetooth: {produto.get_bluetooth()}")
                    print(f"Material: {produto.get_material()}")
                    
                elif produto.get_categoria() == "Escritorio":
                    print(f"Largura: {produto.get_largura()}")
                    print(f"Altura: {produto.get_altura()}")
                    print(f"Cor: {produto.get_cor()}")

                print("\n")
        else:
            print("\033[31;1mNão há produtos cadastrados!\033[m") 
    
    def pesquisar_produto(self):
        while True:
            for produto in self.__lista_produto:
                print(f"Id: {produto.get_id()} \nNome: {produto.get_nome()} \n") 
            
             
            escolha_usuario = verificar_inteiro("Digite o ID: ")

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
       

    def editar_produto(self):
        produto_escolhido = self.pesquisar_produto()
        
        self.exibir_produtos()
        
        
        opcao = True
        while opcao:
            selecionar_edicao = verificar_strings(input("\nDigite o que você deseja alterar por extenso: \n").upper().replace('Ç', 'C'), "(\s+)?([a-zA-Z]{3,30}\s?)+", "Digite somente caracteres de texto: ")
            opcao = False
            if selecionar_edicao == "NOME":
                produto_escolhido.set_nome(verificar_strings(input("Digite o novo nome: "), "(\s+)?([a-zA-Z0-9]{3,30}\s?)+", "Digite somente caracteres alfanumericos: "))

            elif selecionar_edicao == "PRECO":
                produto_escolhido.set_preco(verificar_float("Digite o novo preço: "))

            elif selecionar_edicao == "MARCA":
                produto_escolhido.set_marca(verificar_strings(input("Digite a nova marca: "), "(\s+)?([a-zA-Z0-9]{3,30}\s?)+", "Digite somente caracteres alfanumericos: "))

            elif selecionar_edicao == "LED":
                produto_escolhido.set_led(validar_led("Tem led? "))

            #######################################

            elif produto_escolhido.get_categoria() == "Hardware" and selecionar_edicao == "PORTAS":
                produto_escolhido.set_portas(verificar_inteiro("Digite as portas: "))

            elif produto_escolhido.get_categoria() == "Hardware" and selecionar_edicao == "ARMAZENAMENTO":
                produto_escolhido.set_armazenamento(verificar_float("Digite o novo armazenamento: "))

            elif produto_escolhido.get_categoria() == "Hardware" and selecionar_edicao == "CONSUMO":
                produto_escolhido.set_consumo(verificar_float("Digite o novo consumo: "))

            #######################################

            elif produto_escolhido.get_categoria() == "Escritorio" and selecionar_edicao == "LARGURA":
                produto_escolhido.set_largura(verificar_float("Digite a nova largura: "))

            elif produto_escolhido.get_categoria() == "Escritorio" and selecionar_edicao == "ALTURA":
                produto_escolhido.set_altura(verificar_float("Digite a nova altura: "))

            elif produto_escolhido.get_categoria() == "Escritorio" and selecionar_edicao == "COR":
                produto_escolhido.set_cor(verificar_strings(input("Digite a nova cor: "), "(\s+)?([a-zA-Z]{3,30}\s?)+", "Digite somente caracteres de texto: "))

            #######################################

            elif produto_escolhido.get_categoria() == "Perifericos" and selecionar_edicao == "ENTRADAS":
                produto_escolhido.set_entradas(verificar_strings(input("Digite a nova entrada: "), "(\s+)?([a-zA-Z0-9]{3,30}\s?)+", "Digite somente caracteres alfanumericos: "))

            elif produto_escolhido.get_categoria() == "Perifericos" and selecionar_edicao == "BLUETOOTH":
                produto_escolhido.set_bluetooth(validar_led("Bluetooth (S ou N): "))

            elif produto_escolhido.get_categoria() == "Perifericos" and selecionar_edicao == "MATERIAL":
                produto_escolhido.set_material(verificar_strings(input("Digite o novo material: "), "(\s+)?([a-zA-Z]{3,30}\s?)+", "Digite somente caracteres alfanumericos: ")) 

            else:
                print("\033[31;1mERRO! Digite uma opção válida.\033[m")
                opcao = True
    
                
        

