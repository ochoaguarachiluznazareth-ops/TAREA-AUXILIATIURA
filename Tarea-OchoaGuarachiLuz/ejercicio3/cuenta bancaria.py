class CuentaBancaria:
   
    def __init__(self, titular, nroCuenta, saldo):
        self.titular = titular
        self.nroCuenta = nroCuenta
        self.saldo = saldo

    
    def depositar(self, monto):
        if monto <= 0:
            print("Error: El monto a depositar debe ser mayor que 0.")
        else:
            self.saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: bs. {self.saldo}")

    def retirar(self, monto):
        if monto > self.saldo:
            print(f"Error: Fondos insuficientes. Intenta retirar bs. {monto}")
        elif monto <= 0:
            print("Error: El monto a retirar debe ser mayor que 0.")
        else:
            self.saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: bs. {self.saldo}")

    def mostrar_datos(self):
        print("\n--- DATOS DE LA CUENTA ---")
        print(f"Titular: {self.titular}")
        print(f"Número de Cuenta: {self.nroCuenta}")
        print(f"Saldo Actual: bs. {self.saldo}")
        print("--------------------------")

cuenta = CuentaBancaria("Luz Ochoa", "12345678", 500.0)
cuenta.mostrar_datos()
cuenta.depositar(200)
cuenta.depositar(-50)
cuenta.retirar(100)
cuenta.retirar(1000)
cuenta.mostrar_datos()
