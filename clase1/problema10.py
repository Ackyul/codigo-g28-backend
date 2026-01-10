def es_primo(num):
    if (num < 2):
        return f"El {num}, no es primo"

    for i in range (2, numero):
        if (num % i == 0):
            return f"El {num}, no es primo"
        else:
            return f"El {num}, es primo"

num = int(input("Ingrese un numero: "))

print(es_primo(num))