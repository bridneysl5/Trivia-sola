import random  # Importamos la librería random

# Para implementar puntajes, crearemos una nueva variable llamada "puntaje", la que inicializamos en 0.
puntaje = random.randint(0, 10)

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print("\033[33m Bienvenido a mi trivia sobre la Independencia del Perú")
print ("Pondremos a prueba tus conocimientos")
print ("Cada pregunta respondida correctamente vale 10 puntos")

import time

# Ejemplo 1
print ("\033[32m Un momento, nos vemos en 5 segundos")

time.sleep(2) # Espera 5 segundos antes de continuar.

print ("ya volví!")

# Ejemplo 2
x = input ("¿Que expectativas tienes de esta trivia? ")
print ("mmmmmmmmmm")
time.sleep(1)
print("muy buena tu respuesta")
print("Ahora sí, empiezas la trivia con", puntaje, "puntos")

# Agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable

nombre = input("Ingresa tu nombre: ")

# Es importante dar instrucciones sobre cómo jugar:
# Ahora, lo personalizaremos con el nombre del jugador, diciéndole a print() que muestre el contenido de la variable "nombre". Cada cosa distinta que queremos que muestre en la pantalla, la separamos con comas
print("\033[36m \nHola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")

# OJO, el \n al final de la línea 6 es para dar un "salto de línea"

# Pregunta 1
print ("1) ¿Quién fue el libertador de nuestro país?")
print ("a) Bernald O'higgins")
print ("b) José Olaya")
print ("c) Don Jose de San Martin")
print ("d) Cristobal Colón")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input("\nTu respuesta: ")

while respuesta_1 not in ("a", "b", "c", "d"):
  respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_1 == "a":
  print("Totalmente incorrecto!", nombre, "El fue quien ayudó a San Martin a Liberar nuestro país")
elif respuesta_1 == "b":
  print("Mmmm ... No!", nombre, "El fue un pescador,el emisario al servicio de los patriotas ")
  puntaje = puntaje - 5
elif respuesta_1 == "d":
  print("No ... Incorrecto!", nombre, "El fue quien descrubrió América")
  puntaje = puntaje - 5
else:
  puntaje * 2
  print("Muy bien", nombre, "!")

# Pregunta 2
print ("2) (\033[36m ¿Cuántas banderas tuvo nuestro país antes de la actual?")
print ("a) 1")
print ("b) 2")
print ("c) 3")
print ("d) 4")

# Almacenamos la respuesta del usuario en la variable "respuesta_2"
respuesta_2 = input("\nTu respuesta: ")

while respuesta_2 not in ("a", "b", "c", "d"):
  respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
while respuesta_2 not in ("b"):
  print("respuesta incorrecta")
  respuesta_2 = input("Debes responder bien para pasar a la siguiente pregunta.responde nuevamente: ")
# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_2 == "b":
  puntaje += 10
  print ("Wow, excellent :D", nombre, "!")
else:
  print("se que tu puedes!")

# Pregunta 3
print("3) ¿En qué año se proclamó la Independencia del Perú?")
print ("a) 1834")
print ("b) 1810")
print ("c) 1850")
print ("d) 1821")

# Almacenamos la respuesta del usuario en la variable "respuesta_3"
respuesta_3 = input("\nTu respuesta: ")

while respuesta_3 not in ("a", "b", "c", "d"):
  respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
while respuesta_3 not in ("d"):
  print("respuesta incorrecta")
  respuesta_3 = input("Debes responder bien para pasar a la siguiente pregunta.responde nuevamente: ")
# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_3 == "d":
  puntaje += 10
  print ("very good", nombre, "!")
else:
  print("se que tu puedes!")

print("\033[37m \n4) ¿del 1 al 3 como calificarias la trivia?")
print("1) no me gusto")
print("2) puedes mejorar")
print("3) buen trabajo")

respuesta_4 = input("\nTu respuesta: ")

if respuesta_4 == "3":
  print("realmente te divertiste")
else:
  print("thanks por tu comentario, voy a mejorar")

print ("Gracias", nombre, "por jugar mi trivia, ganaste", puntaje, "puntos")