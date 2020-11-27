# -*- coding: utf-8 -*-
# los decoradores hacen que una funcion pueda tener mas funciones tal cual como su nombre dice

def protected(func):      # "func" es la misma funcion "protected_func" pero dentro de la funcion decoradora

    def wrapper(password):
        
        if password == "platzi":
            return func()
        else:
            print("contraseña incorrecta.")

    return wrapper

@protected                # mediante el "@" podemos asignar el decorador
def protected_func():
    print("contraseña correcta.")


if __name__ == "__main__":
    password = input("pon contraseña: ")

    protected_func(password)


# ------------------------------------------------------------------

def funcion_decoradora(funcion_parametro):

    def funcion_interior():

        #ACCIONES ADICIONALES QUE DECORAN

        print("vamos a realizar calculos")

        funcion_parametro()             #La "funcion_parametro" es la funcion suma dentro de la funcion decoradora.. puede tener cualquier nombre

        print("calculo realizado")
    
    return funcion_interior              #El return no en la primera si no en la segunda "funcion interior"

@funcion_decoradora
def suma():

    print(15 + 20)

@funcion_decoradora
def resta():

    print(30 - 10)

# invocacion de funciones
suma()
resta()
