# ###
# # 01 - Bucles (while)
# # Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
# ###

# from os import system
# if system("clear") != 0: system("cls")

# print("\n Bucle while:")

# # Bucle con una simple condición
# contador = 0

# while contador <= 5:
#   print(contador)
#   contador += 1 # es super importante para evitar un bucle infinito

# # utilizando la palabra break, para romper el bucle
# print("\n Bucle while con break:")
# contador = 0

# while True:
#   print(contador)
#   contador += 1
#   if contador == 5:
#     break # sale del bucle

# # continue, que lo hace es saltar esa iteración en concreto
# # y continuar con el bucle
# print("\n Bucle con continue")
# contador = 0
# while contador < 10:
#   contador += 1

#   if contador % 2 == 0:
#     continue

#   print(contador)

# # else, esta condición cuando se ejecuta?
# print("\n Bucle while con else:")
# contador = 0
# while contador < 5:
#   print(contador)
#   contador += 1
# else:
#   print("El bucle ha terminado")

# # else, esta condición cuando se ejecuta?
# print("\n Bucle while con else:")
# contador = 0
# while contador < 5:
#   print(contador)
#   contador += 1
# else:
#   print("El bucle ha terminado")

# # pedirle al usuario un número que tiene
# # que ser positivo si no, no le dejamos en paz
# numero = -1
# while numero < 0:
#   numero = int(input("Escribe un número positivo: "))
#   if numero < 0:
#     print("El número debe ser positivo. Intenta otra vez, majo o maja.")

# print(f"El número que has introducido es {numero}")

# numero = -1
# while numero < 0:
#   try:
#     numero = int(input("Escribe un número positivo: "))
#     if numero < 0:
#       print("El número debe ser positivo. Intenta otra vez, majo o maja.")
#   except:
#     print("Lo que introduces debe ser un número, que si no peta!")

# print(f"El número que has introducido es {numero}")

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

# contador = 10

# while contador >0:
#     print(contador)
#     contador -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

# contador = 0
# suma = 0

# while contador <= 20:
#     contador += 1
#     if contador % 2 == 0:
#         suma += contador

# print(suma)


# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

# numero = int(input("Introduce un número: "))
# contador = 0
# resultado = 1

# while contador < numero:
#     try:
#         contador += 1
#         resultado *= contador   
#     except:
#         print("Introduce un número válido")
# print(f"{numero} = {resultado}")


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

# contraseña = ""

# while len(contraseña) < 8:
#     contraseña = input("Introduce una contraseña de al menos 8 caractéres: ")
#     if len(contraseña) < 8:
#         print("La contraseña debe contener al menos 8 caractéres.")

# print("Contraseña válida")


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

# numero = int(input("Introduce un número del 1 al 10: "))
# contador = 0
# resultado = 0

# print(f"Tabla del {numero}:")
# while contador <= 10:
#     resultado = contador * numero
#     print(f"{numero} X {contador} = {resultado}")
#     contador +=1


# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

n = int(input("Introduce un número entero positivo N: "))

number = 2
while number <= n:
  check = True
  divisor = 2
  while divisor * divisor <= number:
    if number % divisor == 0:
      check = False
      break
    divisor += 1
  if check:
    print(number)

  number += 1