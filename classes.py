class Veiculo:
    def _init_(self, marca, modelo):
        self.marca = marca             
        self._ano = 2020               
        self.__quilometragem = 0       

    def dirigir(self, distancia):
        self.__quilometragem += distancia

    def get_quilometragem(self):
        return self.__quilometragem


class Carro(Veiculo):
    def _init_(self, marca, modelo, tipo_combustivel):
        super()._init_(marca, modelo)
        self.tipo_combustivel = tipo_combustivel  

    def abastecer(self):
        print(f"Abastecendo o carro {self.marca} {self.modelo}.")

    def get_ano(self):
        return self._ano  
    
