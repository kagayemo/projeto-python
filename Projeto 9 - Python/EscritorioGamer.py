from Produto import Produto

class EscritorioGamer(Produto):
    def __init__(self, largura, altura, cor, id_x, nome, preco, marca, led):
        self.categoria = "Escritorio"
        super().__init__(id_x, nome, preco, marca, led, self.categoria)

        self.__largura = largura
        self.__altura = altura
        self.__cor = cor 

    def get_largura(self):
        return self.__largura
    
    def get_altura(self):
        return self.__altura

    def get_cor(self):
        return self.__cor

    def set_largura(self, largura):
        self.__largura = largura
    
    def set_altura(self, altura):
        self.__altura = altura

    def set_cor(self, cor):
        self.__cor = cor