# -*- coding: utf-8 -*-

def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number -1)

if __name__ == "__main__":
    number = int(input("epale dame un numero: "))

    result = factorial(number)

    print(result)


# len = es longitud de caracteres 
a = "platzi"
len(a)
a[len(a) - 1]

# asigna mayuscula o misnuscula 
a.upper = "mayuscula"
a.lower = "minuscula"

# invoca el caracter correspondiente al numero o al contrario.. muestra caracteres desde un numero hasta el numero que asignes
# a[inicio:final:saltos]=
a[4]= "platzi"
a.find("z")

a = "platzi"
a[1:5]

# nombre = "tony"
# print(nombre[::-1])

