class Bus:
    def __init__(self, capacidad_total=40):

        self.capacidad_total = capacidad_total
        self.pasajeros_actuales = 0
        self.dinero_recaudado = 0.0
        self.costo_pasaje = 1.50

   
    def subir_pasajeros(self, cantidad):
        asientos_libres = self.asientos_disponibles()
        
        if cantidad <= asientos_libres:
            self.pasajeros_actuales += cantidad
            print(f"Subieron {cantidad} pasajeros con éxito.")
            self.cobrar_pasaje(cantidad)
        else:
            print(f"No hay espacio suficiente. Solo quedan {asientos_libres} asientos y querían subir {cantidad}.")
            if asientos_libres > 0:
                print(f"Subiendo solo a {asientos_libres} pasajeros.")
                self.pasajeros_actuales += asientos_libres
                self.cobrar_pasaje(asientos_libres)

   
    def cobrar_pasaje(self, cantidad):
        monto_cobrado = cantidad * self.costo_pasaje
        self.dinero_recaudado += monto_cobrado
        print(f"Se cobró bs. {monto_cobrado:.2f} por los {cantidad} pasajeros.")

    
    def asientos_disponibles(self):
        return self.capacidad_total - self.pasajeros_actuales

    
    def mostrar_estado(self):
        print(f"\n[Estado Bus] Pasajeros a bordo: {self.pasajeros_actuales}/{self.capacidad_total} | "
              f"Asientos libres: {self.asientos_disponibles()} | "
              f"Total recaudado: bs. {self.dinero_recaudado:.2f}")



print("INSTANCIANDO EL BUS (Capacidad: 30 asientos) ")
mi_bus = Bus(capacidad_total=30)
mi_bus.mostrar_estado()

print(" Intentan subir 15 pasajeros ")
mi_bus.subir_pasajeros(15)

print("Ver asientos disponibles ")
print(f"Asientos libres reportados: {mi_bus.asientos_disponibles()}")
mi_bus.mostrar_estado()

print("Intentan subir 20 pasajeros (Supera la capacidad restante) ")
mi_bus.subir_pasajeros(20)
mi_bus.mostrar_estado()
