from Produto import Produto

class Perifericos(Produto):
    def __init__(self, entradas, bluetooth, material, id_x, nome, preco, marca, led):
        self.categoria = "Perifericos"
        super().__init__(id_x, nome, preco, marca, led, self.categoria)

        self.__entradas = entradas
        self.__bluetooth = bluetooth
        self.__material = material

    def get_entradas(self):
        return self.__entradas
    
    def get_bluetooth(self):
        return self.__bluetooth

    def get_material(self):
        return self.__material

    def set_entradas(self, entradas):
        self.__entradas = entradas
    
    def set_bluetooth(self, bluetooth):
        self.__bluetooth = bluetooth

    def set_material(self, material):
        self.__material = material