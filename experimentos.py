# -*- coding: utf-8 -*-

# def run(palabra):
#     palabra_revertida = palabra[::-1]
    
#     if palabra_revertida == palabra:
#         return True 
#     return False

# if __name__ == "__main__":
#     palabra = str(input("escribe la palabra aqui: "))

#     result = run(palabra)

#     if result is True:
#         print("es un palindromo")
#     else:
#         print("no es un palindromo")
# -----------------------------------------------------------------------------------------
# lista =["antoine", "manuel", 27590962]

# print("mi nombre es {}, mi apellido {} y mi cedula de identidad es {}".format(lista[0], lista[1], lista[2]))
# ---------------------------------------------------------------------------------
# subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# scores = []

# for subject in subjects:
#     score = input("¿Qué nota has sacado en " + subject + "?")
#     scores.append(score)
    
# for i in range(len(subjects)):
#     print("En " + subjects[i] + " has sacado " + scores[i])
# ------------------------------------------------------------------------
# materias = ["matematicas ", "ciencias ", "leguaje ", "fisica "]
# nota = []

# for i in materias:
#     notas = input("cuanto sacaste en " + i)
#     nota.append(notas)
    
# for o in range(len(materias)):
#     print("sacaste " + nota[o] + " en " + materias[o])

# -------------------------------------------------------------------------
# con este modo imprimimos cada variable-diccionario individualmente

# materias ={"lengua", "matematicas", "programcion", "fisica"}
# notas ={15,16,17,18}

# for m in materias:
#     print("materia: " + m)

# for n in notas:
#     print("notas: ")
#     print(n)

# ------------------------------------------------------------------------------
# con este modo podemos poner tanto el nombre como el valor

# materias = {}
# materias["matematicas"] = int(input("cuanto sacaste en matematicas? "))
# materias["fisica"] = int(input("cuanto sacaste en fisica? "))
# materias["programacion"] = int(input("cuanto sacaste en programacion? "))
# materias["lenguaje"] = int(input("cuanto sacaste en lenguaje? "))

# for m,v in materias.items():
#     print("en la materia: {} sacaste {}".format(m,v))
   
# ------------------------------------------------------------------------------
# un ejemplo mas completo ... OJO con la , de abajo en promedio 

# calificaciones = {}
# calificaciones["matematicas"] = 15
# calificaciones["fisica"] = 20
# calificaciones["programacion"] = 18
# calificaciones["lenguaje"] = 17

# for key in calificaciones:
#     print(key)

# for value in calificaciones.values():
#     print(value)

# for key,value in calificaciones.items():
#     print("materia: {}, notas: {}".format(key, value))

# suma_de_calificaciones = 0
# for calificacion in calificaciones.values():
#     suma_de_calificaciones += calificacion

#     promedio = suma_de_calificaciones / len(calificaciones.values())
#     print("el promedio es:", promedio) 

# ---------------------------------------------------------------------------
# para usar el * int tenemos que encerrarlo en un parentesis tambien 

# nombre = input("cual es tu nombre ")
# edad = input ("cual es tu edad ")
# print(("te llamas: " + nombre + "\ntu edad: " + edad) * int(edad))
# ------------------------------------------------------------------------------
# usando el codigo "len" que da la longitud

# nombre = input("¿cual es tu nombre?")
# cantidad = len(nombre)
# print("{} tiene {} letras".format(nombre, cantidad))
# #-------------                                                     --------------
# name = input("¿Cómo te llamas? ")
# print(name.upper() + " tiene " + str(len(name)) + " letras")
# ---------------------------------------------------------------------------------

# numeros = []

# for num in range(1,31):
#     if num % 2 == 0:             
#         numeros.append(num) 

# ---------------------------------------------------------------------------------
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.

# horas = int(input("cuantas horas trabajas al dia? "))
# sueldo = int(input("cual es tu sueldo")) 
# print(sueldo * horas)

# ---------------------------------------------------------------------------------
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable
# y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado 
# redondeado con dos decimales.

# peso = input("cual es tu peso: ")
# altura = input("cual es tu altura: ")         #no poner int a los valores si no seran enteros 
# imc = round(float(peso) / float(altura)*2)    #"round" redondea el numero al entero mas cercano y "float" los combierte en numeros
# print("tu imc es de :" + str(imc) + " kg")

# ---------------------------------------------------------------------------------
# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla
# la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario,
# y <c> y <r> son el cociente y el resto de la división entera respectivamente.

# ---------------------------------------------------------------------------------
# clase simple

# class Usuario:
#     def __init__(self, username, password, email):
#         self.username = username
#         self.password = password
#         self.email = email

# charles = Usuario("charles", "26436457", "charles@gmail.com")
# print(charles.username)
# print(charles.password)
# print(charles.email)

# -----------------------------------------------------------------------------------
#funcion de suma recursiva

# def suma_recursiva(numero):
#     if numero == 1:
#         return 1
#     else:
#         return numero + suma_recursiva(numero-1)

# while True:

#     try:
#         numero = int(input('Número a sumar recursivamente: '))
#         result = suma_recursiva(numero)
#         print(result)
#         print('')

#     except RecursionError:
#         print('Máximo número es 998')
#         print('')

#     except ValueError:
#         print('Input no válido')
#         print('')


# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------------
# una forma de encriptar en codigo binario

# def encrypt(word):
#     ans = ''.join(format(i, 'b') for i in bytearray(word, encoding='utf-8'))
#     return ans


# def run():
#     word = str(input('Ingrese la palabra a encriptar: '))
#     ans = encrypt(word)
#     print('La palabra en binario es: {}'.format(ans))


# if __name__ == '__main__':
#     run()

#-----------------------------------------------------------------------------------

# class Saludo:

#     saludos = ["Hola", "Chao"]

#     def __init__(self, he_saludado):
#         self.he_saludado = he_saludado

#     def saludando(self):
#         self.amigo = True
#         self.inprimir()

#     def despidiendo(self):
#         self.amigo = False
#         self.inprimir()

#     def inprimir(self):
#         if self.amigo:
#             print(self.saludos[0])

#         else:
#             print(self.saludos[1])

# def run():

#     saludo = Saludo(he_saludado = False)

#     while True:
#         codigo = input("que deseas hacer.. (s)aludar, (d)espedir ")

#         if codigo == "s":
#             saludo.saludando()

#         elif codigo == "d":
#             saludo.despidiendo()

#         else:
#             print("codigo no identificado")


# if __name__ == "__main__":
#     run()
   
# ----------------------------------------------------------------------------------------

# def calculo():
#     if edad >= 18:
#         print("eres mayor de edad")
#     else:
#         print("no eres mayor de edad")

# if __name__ == "__main__":
#     while True:
#         edad = int(input("cual es tu edad: "))
#         calculo()

# ----------------------------------------------------------------------------------------
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario
# por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada
# en la variable sin tener en cuenta mayúsculas y minúsculas.

# class Usuario:

#     def __init__(self, ingreso):
#         self.ingreso = ingreso

#     def login(self, user, password):
#         if user == "tony" and password == "contraseña":
#             print("has ingresado exitosamente")
#         else:
#             print("usuario equivocado")

# def run():
#     usuario = Usuario(ingreso = False)

#     print("que deseas hacer: (i)ngresar , (s)alir: ")
#     accion = input()

#     while True:
#         if accion == "i":
#             user = str(input("ingresa usuario: "))
#             password = str(input("cual es la contraseña: "))
#             usuario.login(user, password)

#         elif accion == "s":
#            break

#         else:
#            print("error en escritura")
            

# if __name__ == "__main__":
#     run()
        
# para hacer una clase hay que crear un init y este en realidad puede si quiere no llevar nada relevante 
# .. la cuestion esta en definir el init y ponerle un atributo cualquiera ya que sin eso no sirve el codigo
# .. es como una forma de enlazar la clase con la funcion RUN().. tengo sueño
# -----------------------------------------------------------------------------------------

# def run():
#     nombre = input("cual es tu nombre")
#     print("hola {}".format(nombre))

# if __name__ == "__main__":
#     run()

# ----------------------------------------------------------------------------------------------

# FACTORIAL
# num = int(input("numero: "))
# factorial = 1 

# for i in range(num):
#     print(factorial, " * ", num)
#     factorial *= num

#     num -= 1
    

# print(factorial)
# ---------------------------------------------------------------------------------------------------
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla
#  el capital obtenido en la inversión.

# def run(invercion,interes_anual,años):
#     capital = invercion * años
#     interes = (capital * interes_anual) /100
#     capital = capital - interes
#     print("el interes seria un total de: {}".format(interes), "\ny la ganancia total seria de: {}".format(capital))


# if __name__ == "__main__":
#     while True:

#         invercion = int(input("cantidad a invertir: "))
#         interes_anual = int(input("interes: "))
#         años = int(input("años: "))
#         run(invercion,interes_anual,años)

# ------------------------------------------------------------------------
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo
# el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se 
# le hace por no ser fresca y el coste final total


# def run(compra,pan_nuevo,pan_viejo):

#     if compra <= 6:
#         coste = float(compra * pan_nuevo)
#         print(coste)

#     if compra > 11:
#         print("no tenemos tantos panes ")

#     elif compra >=7:
#         compra -= 6 
#         compra *= pan_viejo
#         coste = float((6 * pan_nuevo) + compra)
#         print(coste)
    
#     else:
#         print("habla bien coño")

# if __name__ == "__main__":
#     while True:
#         compra = int(input("cuantos panes quieres: "))
#         pan_nuevo = 3.49
#         pan_viejo = 2.09
#         run(compra,pan_nuevo,pan_viejo)

# -------------------------------------------------------------------------------
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.


# def division(divisisa,numero_2,numero_1):

#     if divisa == 0:
#         print("da cero") 
#     else: 
#         print(divisa)

# if __name__ == "__main__":
#     while True:
#         numero_1= int(input("dime el primer numero: "))
#         numero_2= int(input("dime el segundo numero: "))
#         divisa= numero_1 % numero_2
#         division(divisa,numero_2,numero_1)

# -----------------------------------------------------------------------------------
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

# def run(numero):
#     if prueba == 0:
#         print("es par")
#     else: 
#         print("no es par")

# if __name__ == "__main__":
#     while True:
#         numero = int(input("dadme el numero: "))
#         prueba = numero % 2 
#         run(numero)
# ---------------------------------------------------------------------------------------
# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

# def run(edad,sueldo):

#     if edad > 16 and sueldo >= 1000:
#         print("si puedes tributar")
        
#     else:
#         print("no puedes tributar")

# if __name__ == "__main__":

#     edad = int(input("que edad tienes.? "))
#     sueldo = int(input("cuanto son tus ingresos mensuales.? "))
#     run(edad,sueldo)

# ---------------------------------------------------------------------------------------------
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres 
# con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que 
# pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.


# name = input("¿Cómo te llamas? ")
# gender = input("¿Cuál es tu sexo (M o H)? ")
# if gender == "M":
#     if name.lower() < "m":
#         group = "A"
#     else:
#         group = "B"
# else:
#     if name.lower() > "n":
#         group = "A"
#     else:
#         group = "B"
# print("Tu grupo es " + group)

# -------------------------------------------------------------------

class Control:

   def __init__(self, nombre, telefono):
      self.nombre = nombre
      self.telefono = telefono
   
class ControlBook:

    def __init__(self):
       self.contactos = []

    def guardar(self, nombre, telefono):
       control = Control(self, nombre, telefono)                         
       self.contactos.append(control)
    
    def inprimir(self):
         for contacto in self.contactos:
             self.show(contacto)

    def show(self, contacto):
        print("********")
        print("nombre: {}".format(contacto.nombre))
        print("telefono: {}".format(contacto.telefono))
        print("********")

if __name__ == "__main__":
   control_book = ControlBook()
   
   while True:
      print("que deseas hacer.?\n(g)uardar \n(b)orrar \n(l)istar")
      codigo = input("")

      if codigo == "g":
         nombre = input("ingrese nombre: ")
         telefono = input("ingresa el numero: ")

         control_book.guardar(nombre, telefono)

      elif codigo == "b":
         nombre = input("ingrese nombre: ")
         control_book.borrar(nombre)

      elif codigo == "l":
         control_book.inprimir()

      else:
         print("error")

