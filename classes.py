class Veiculo:
    def _init_(self, marca, modelo):
        self.marca = marca             # Atributo público
        self._ano = 2020               # Atributo protegido
        self.__quilometragem = 0       # Atributo privado

    def dirigir(self, distancia):
        self.__quilometragem += distancia

    def get_quilometragem(self):
        return self.__quilometragem


class Carro(Veiculo):
    def _init_(self, marca, modelo, tipo_combustivel):
        super()._init_(marca, modelo)
        self.tipo_combustivel = tipo_combustivel  # Atributo público

    def abastecer(self):
        print(f"Abastecendo o carro {self.marca} {self.modelo}.")

    def get_ano(self):
        return self._ano  # Acesso ao atributo protegido
    