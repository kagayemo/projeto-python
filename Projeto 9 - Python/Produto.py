class Produto:
    def __init__(self, id_x, nome, preco, marca, led, categoria):
        self.__id = id_x
        self.__nome = nome
        self.__preco = preco
        self.__marca = marca
        self.__led = led
        self.__categoria = categoria
        
    def get_id(self):
        return self.__id    
    def get_nome(self):
        return self.__nome
    def get_preco(self):
        return self.__preco
    def get_marca(self):
        return self.__marca
    def get_led(self):
        return self.__led
    def get_categoria(self):
        return self.__categoria
    
    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        self.__nome = nome
    def set_preco(self, preco):
        self.__preco = preco
    def set_marca(self, marca):
        self.__marca = marca
    def set_led(self, led):
        self.__led = led
    def set_categoria(self, categoria):
        self.__categoria = categoria
        
