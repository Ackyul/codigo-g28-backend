lista = []

for i in range(8):
    lista.append(int(input(f"Ingrese número {i+1}: ")))

print(max(lista))
print(min(lista))