from Produto import Produto

class Hardware(Produto):
    def __init__(self, portas, armazenamento, consumo, id_x, nome, preco, marca, led):
        self.categoria = "Hardware"
        super().__init__(id_x, nome, preco, marca, led, self.categoria)

        self.__portas = portas
        self.__armazenamento = armazenamento
        self.__consumo = consumo
        
    def get_portas(self):
        return self.__portas
    
    def get_armazenamento(self):
        return self.__armazenamento

    def get_consumo(self):
        return self.__consumo
    
    def set_portas(self, portas):
        self.__portas = portas
    
    def set_armazenamento(self, armazenamento):
        self.__armazenamento = armazenamento

    def set_consumo(self, consumo):
        self.__consumo = consumo
        
