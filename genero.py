# -*- coding: utf-8 -*-

name = str(input("cual es tu nombre"))
edad = int(input("cual es tu edad"))
sexo = str(input("cual es tu genero sexual"))

def datos():
    print("te llamas {}, tu edad es de {} años y eres de genero {}".format(name,edad,sexo))

def especificaciones():
    if edad >= 18 :
        print("eres un adult@ " + sexo)
    else:
        print("eres un crio")

if __name__ == "__main__":
    datos()
    especificaciones()