arr = []
nota = 0

for i in range(6):
    arr.append(int(input(f"Ingrese su nota número {i+1}: ")))

for suma in range(len(arr)):
    nota += arr[suma]

promedio = nota / len(arr)

print(f"El promedio de las notas es: {promedio}")

if (promedio >= 14):
    print("Esta aprobado")
else:
    print("Esta reprobado")
