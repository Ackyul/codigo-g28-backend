class Auto:

    ruedas = 4
    numero_puertas = 5

    def __init__(self, marca, modelo, hp):
        self.marca = marca
        self.modelo = modelo
        self.hp = hp
        self.color = "rojo"

    def describir_auto(self):
        print(f"El auto tiene la siguientes caracteristicas:\nMarca: {self.marca}\nModelo: {self.modelo}\nHP: {self.hp}\nColor: {self.color}")

auto1 = Auto("a", "b", 12)
print(auto1.modelo, auto1.ruedas)
auto1.describir_auto()
auto2 = Auto("c", "d", 45)
auto2.describir_auto()
auto3 = Auto("e", "f", 324)
auto3.describir_auto()