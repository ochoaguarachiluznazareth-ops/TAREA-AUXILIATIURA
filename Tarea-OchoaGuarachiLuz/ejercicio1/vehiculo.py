class Auto:
    def __init__(self, marca, modelo, anio, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
        self.color = "Blanco"

 
    def mostrar_kilometraje(self):
        kilometros = self.kilometraje // 1000
        metros = self.kilometraje % 1000

        print("Kilometraje:", kilometros, "km y", metros, "m")

   
    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        print("Nuevo color:", self.color)

auto1 = Auto("Toyota", "Corolla", 2020, 125650)
auto2 = Auto("Nissan", "Sentra", 2022, 83420)


auto1.cambiar_color("Morado")
auto2.cambiar_color("Negro")


print("\nAuto 1:")
auto1.mostrar_kilometraje()

print("\nAuto 2:")
auto2.mostrar_kilometraje()
