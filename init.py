nombre = "Yoshua"
edad = int(input("Ingrese su edad: "))
es_mayor_edad = True | False
saldo = float(input("Ingrese su saldo: "))

mensaje = ""

if edad >= 18:
    mensaje = "Es mayor de edad"
else:
    mensaje = "Es menor de edad"

print(nombre)
print(edad, mensaje)
print(es_mayor_edad)
print(saldo)