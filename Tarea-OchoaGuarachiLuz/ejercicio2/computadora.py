class Computadora:
    def __init__(self, marca, procesador, ram, almacenamiento):
        self.marca = marca
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento


    def comparar_ram(self, X):
        return self.ram == X

    def mostrar_datos(self):
        print("Marca:", self.marca)
        print("Procesador:", self.procesador)
        print("RAM:", self.ram, "GB")
        print("Almacenamiento:", self.almacenamiento, "GB")


computadora1 = Computadora("HP", "Intel Core i5", 8, 512)
computadora2 = Computadora(
    marca="Lenovo",
    procesador="AMD Ryzen 5",
    ram=16,
    almacenamiento=1000
)
X = 8

if computadora1.comparar_ram(X):
    print("La RAM de la computadora 1 es igual a", X, "GB")
else:
    print("La RAM de la computadora 1 no es igual a", X, "GB")


print("\nComputadora con mayor almacenamiento:")

if computadora1.almacenamiento > computadora2.almacenamiento:
    computadora1.mostrar_datos()
else:
    computadora2.mostrar_datos()
