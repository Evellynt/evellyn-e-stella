from classes import Carro

def teste_veiculos():
    carro = Carro("Toyota", "Corolla", "Gasolina")
    carro.dirigir(150)
    print(f"Marca: {carro.marca}, Modelo: {carro.modelo}, Tipo: {carro.tipo_combustivel}")
    print(f"Quilometragem: {carro.get_quilometragem()} km")
    print(f"Ano do veículo: {carro.get_ano()}")
    carro.abastecer()
    
if __name__ == "_main_":
    teste_veiculos()
    
