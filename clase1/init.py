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

for i in range (10):
    print(i)


for j in range (5,11):
    print(j)

frutas = ["manzana", "pera", "fresa"]
mixto = [1,19.4, True, "Hola", [1,2]]
print(frutas)
print(mixto[2])
print(mixto[-1])
print(mixto[-2])

frutas.append("uva")
frutas.insert(2,"kiwi")
frutas.insert(10,"arandanos")
frutas.remove("pera")
print(frutas)

def saludar():
    print("Hola mundo!!")

saludar()

def saludar_persona(nombre):
    print(f"Hola, {nombre}!!")

saludar_persona("Yoshua")

def sumar(n1,n2):
    return n1 + n2

print(sumar(1,10))