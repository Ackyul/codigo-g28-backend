class CuentaBancaria:
    def __init__(self, titular, saldo, pin, email, dni):
        self.titular = titular
        self._saldo = saldo
        self._email = email
        self._dni = dni
        self.__pin = pin

    def depositar(self, monto):
        if (monto > 0):
            self._saldo += monto

    def retirar(self, pin, monto):
        if (pin != self.__pin):
            print("Clave incorrecta")
            return 

        if (monto <= self._saldo):
            self._saldo -= monto
            print(f"Se retiro S/ {monto}")
        else:
            print("Saldo insuficiente")

    def ver_saldo(self):
        print(f"Tu saldo es: {self._saldo}")

cuenta_bancaria = CuentaBancaria("Yoshua", 1000, 1234, "yoshua@gmail.com", "4444444")
cuenta_bancaria.depositar(1500)
cuenta_bancaria.ver_saldo()
cuenta_bancaria.retirar(1234, 2000)
cuenta_bancaria.ver_saldo()