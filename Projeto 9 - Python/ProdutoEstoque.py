class ProdutoEstoque():
    def __init__(self):
        self.__quantidade = 0
        self.__quantidade_minima = None 
        self.__produto = None

    def get_quantidade(self): 
        return self.__quantidade
    
    def set_quantidade(self, quantidade, diminuir):
        if diminuir:
            self.__quantidade -= quantidade
        else:
            self.__quantidade += quantidade
        

    def get_quantidade_minima(self):
        return self.__quantidade_minima
    
    def set_quantidade_minima(self, quantidade_minima):
        self.__quantidade_minima = quantidade_minima
    
    def get_produto(self):
        return self.__produto
    
    def set_produto(self, produto):
        self.__produto = produto