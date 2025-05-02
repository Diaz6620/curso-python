###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

from os import system
if system("clear") != 0: system("cls")

# """ Definición de una función

# def nombre_de_la_funcion(parametro1, parametro2, ...):
#   # docstring
#   # cuerpo de la función
#   return valor_de_retorno # opcional

# """

# # Ejemplo de una función para imprimir algo en consola
# def saludar():
#   print("¡Hola!")

# # Ejemplo de una función con parámetro
# def saludar_a(nombre):
#   print(f"¡Hola {nombre}!")

# saludar_a("midudev")
# saludar_a("madeval")
# saludar_a("pheralb")
# saludar_a("felixicaza")
# saludar_a("Carmen Ansio")

# # Funciones con más parámetros
# def sumar(a, b):
#   suma = a + b
#   return suma

# result = sumar(2, 3)
# print(result)

# # Documentar las funciones con docstring
# def restar(a, b):
#   """Resta dos números y devuelve el resultado"""
#   return a - b

# parámetros por defecto
# def multiplicar(a, b = 2):
#   return a * b

# print(multiplicar(2))
# print(multiplicar(2, 3))

# Argumentos por posición
def describir_persona(nombre: str, edad: int, sexo: str):
  print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")

# parámetros son posicionales
describir_persona(1, 25, "gato")
describir_persona("midudev", 25, "gato")
describir_persona("hombre", "madeval", 39)

# Argumentos por clave
# parámetros nombrados
describir_persona(sexo="gato", nombre="midudev", edad=25)
describir_persona(sexo="hombre", nombre="madeval", edad=21) 

# Argumentos de longitud de variable (*args):
def sumar_numeros(*args):
  suma = 0
  for numero in args:
    suma += numero
  return suma

print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2,3 ,4, 5, 6, 7, 8, 9, 10))

# Argumentos de clave-valor variable (**kwargs):
def mostrar_informacion_de(**kwargs):
  for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="midudev", edad=25, sexo="gato")
print("\n")
mostrar_informacion_de(name="madeval", edad=21, country="Uruguay")
print("\n")
mostrar_informacion_de(nick="pheralb", es_sub=True, is_rich=True)
print("\n")
mostrar_informacion_de(super_name="felixicaza", es_modo=True, gatos=40)

# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora

# def tabla_multiplicar(a):
#   """Devuelve la tabla de multiplicar del número indicado"""
#   print(f"La tabla del {a} es:")
#   for i in range(1, 11):
#     print(f"{a} X {i} = {a * i}")

# def conducir():
#   carnet = input("¿Tienes carnet de conducir?\n").lower()
#   edad = int(input("¿Que edad tienes?\n"))
#   if carnet == "si" and edad > 17:
#     print("!Enhorabuena¡ Puedes conducir")
#   else:
#     print("Lo siento, de momento no puedes conducir.")

# conducir()

##########################################################################################

#Funcion completa para recoger datos, saludar, evaluar conducir.

def saludo_carnet():
  name = input("Hola, ¿Cual es tu nombre?")
  age = int(input(f"¡Hola {name}!, ¿Dime que edad tienes?"))
  carnet = input(f"¡Perfecto {name}! y ya con {age} años, ¿Tienes carnet de conducir?").lower()

  can_drive = False
  if age > 17 and carnet == "si":
    can_drive = True

  if not can_drive:
    print(f"Pues lo siento {name}, ")

  

  

############### Refactorizar funcion para chequear por separado los datos ################

def check(age, carnet):
  check_age = False
  check_carnet = False

  if age > 17:
    check_age = True

  if carnet == "si":
    check_carnet = True

  return check_carnet, check_age