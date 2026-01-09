# 📚 Primera Clase de Python - Resumen

Bienvenido al repositorio del **Grupo 28**. Este documento resume todos los conceptos fundamentales de Python vistos en nuestra primera clase.

---

## 📋 Contenido

1. [Variables y Tipos de Datos](#variables-y-tipos-de-datos)
2. [Entrada de Datos](#entrada-de-datos)
3. [Condicionales](#condicionales)
4. [Bucles](#bucles)
5. [Listas](#listas)
6. [Funciones](#funciones)
7. [Ejercicios Prácticos](#ejercicios-prácticos)

---

## 🔤 Variables y Tipos de Datos

En Python trabajamos con diferentes tipos de datos:

```python
nombre = "Yoshua"              # String (cadena de texto)
edad = 25                      # Integer (número entero)
saldo = 1500.50               # Float (número decimal)
es_mayor_edad = True          # Boolean (verdadero/falso)
```

### Tipos de datos principales:

- **`str`**: Cadenas de texto
- **`int`**: Números enteros
- **`float`**: Números decimales
- **`bool`**: Valores booleanos (True/False)

---

## 📥 Entrada de Datos

Para recibir información del usuario utilizamos la función `input()`:

```python
edad = int(input("Ingrese su edad: "))
saldo = float(input("Ingrese su saldo: "))
nombre = input("Ingrese su nombre: ")
```

> **Nota**: `input()` siempre retorna un string, por lo que debemos convertirlo con `int()` o `float()` según necesitemos.

---

## 🔀 Condicionales

Las estructuras condicionales nos permiten tomar decisiones en el código:

```python
if edad >= 18:
    mensaje = "Es mayor de edad"
else:
    mensaje = "Es menor de edad"
```

### Operadores de comparación:

- `==` igual a
- `!=` diferente de
- `>` mayor que
- `<` menor que
- `>=` mayor o igual que
- `<=` menor o igual que

---

## 🔁 Bucles

### Bucle `for` con `range()`

El bucle `for` nos permite repetir acciones:

```python
# Imprimir números del 0 al 9
for i in range(10):
    print(i)

# Imprimir números del 5 al 10
for j in range(5, 11):
    print(j)

# Imprimir números pares del 2 al 20
for i in range(2, 21, 2):
    print(i)
```

**Sintaxis de `range()`:**

- `range(n)`: del 0 hasta n-1
- `range(inicio, fin)`: desde inicio hasta fin-1
- `range(inicio, fin, paso)`: desde inicio hasta fin-1, con incrementos de "paso"

---

## 📝 Listas

Las listas son colecciones ordenadas de elementos:

```python
frutas = ["manzana", "pera", "fresa"]
mixto = [1, 19.4, True, "Hola", [1, 2]]
```

### Acceso a elementos:

```python
print(frutas[0])      # Primer elemento: "manzana"
print(mixto[-1])      # Último elemento: [1, 2]
print(mixto[-2])      # Penúltimo elemento: "Hola"
```

### Métodos de listas:

```python
frutas.append("uva")           # Agregar al final
frutas.insert(2, "kiwi")       # Insertar en posición específica
frutas.remove("pera")          # Eliminar elemento específico
len(frutas)                    # Obtener longitud de la lista
```

### Funciones útiles:

```python
numeros = [5, 2, 8, 1, 9]
max(numeros)    # Obtener el valor máximo
min(numeros)    # Obtener el valor mínimo
```

---

## ⚙️ Funciones

Las funciones nos permiten reutilizar código:

### Función sin parámetros:

```python
def saludar():
    print("Hola mundo!!")

saludar()
```

### Función con parámetros:

```python
def saludar_persona(nombre):
    print(f"Hola, {nombre}!!")

saludar_persona("Yoshua")
```

### Función con retorno:

```python
def sumar(n1, n2):
    return n1 + n2

resultado = sumar(1, 10)
print(resultado)  # 11
```

---

## 💡 Ejercicios Prácticos

### 📌 Problema 1: Calculadora Básica

**Archivo:** [`problema1.py`](problema1.py)

Programa que realiza operaciones aritméticas básicas (suma, resta, multiplicación, división) con validación de división por cero.

---

### 📌 Problema 2: Tabla de Multiplicar

**Archivo:** [`problema2.py`](problema2.py)

Genera la tabla de multiplicar de un número ingresado por el usuario (del 1 al 10).

---

### 📌 Problema 3: Números Pares

**Archivo:** [`problema3.py`](problema3.py)

Imprime todos los números pares del 2 al 20 usando `range()` con paso de 2.

---

### 📌 Problema 4: Suma de Números

**Archivo:** [`problema4.py`](problema4.py)

Calcula la suma de los primeros 100 números naturales (1 al 100).

---

### 📌 Problema 5: Lista de Nombres

**Archivo:** [`problema5.py`](problema5.py)

Solicita 5 nombres al usuario, los almacena en una lista y luego los imprime.

---

### 📌 Problema 6: Promedio de Notas

**Archivo:** [`problema6.py`](problema6.py)

Calcula el promedio de 6 notas y determina si el estudiante está aprobado (≥14) o reprobado.

---

### 📌 Problema 7: Máximo y Mínimo

**Archivo:** [`problema7.py`](problema7.py)

Solicita 8 números y encuentra el valor máximo y mínimo usando las funciones `max()` y `min()`.

---

### 📌 Problema 8: Área de Rectángulo

**Archivo:** [`problema8.py`](problema8.py)

Función que calcula el área de un rectángulo dados la base y la altura.

---

### 📌 Problema 9: Contador de Vocales

**Archivo:** [`problema9.py`](problema9.py)

Función que cuenta cuántas vocales hay en un texto dado (mayúsculas y minúsculas).

---

### 📌 Problema 10: Número Primo

**Archivo:** [`problema10.py`](problema10.py)

Función que determina si un número es primo o no.

---

## 🎯 Conceptos Clave Aprendidos

✅ Variables y tipos de datos básicos  
✅ Conversión de tipos (`int()`, `float()`, `str()`)  
✅ Entrada y salida de datos (`input()`, `print()`)  
✅ Estructuras condicionales (`if`, `else`)  
✅ Bucles `for` y función `range()`  
✅ Listas y sus métodos principales  
✅ Definición y uso de funciones  
✅ Parámetros y valores de retorno  
✅ F-strings para formateo de texto  
✅ Operadores aritméticos y de comparación

---

## 📖 Recursos Adicionales

- [Documentación oficial de Python](https://docs.python.org/es/3/)
- [Tutorial de Python en español](https://docs.python.org/es/3/tutorial/)

---

**Grupo 28 - Backend con Python** 🐍
