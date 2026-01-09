arr = []

for i in range(5):
    arr.append(str(input(f"Ingrese su nombre {i+1}: ")))

for j in range(len(arr)):
    print(arr[j])