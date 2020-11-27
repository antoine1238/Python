# -*- coding: utf-8 -*-
# tenemos que importar random para asi poder usar su funcion ..
# e igual no podemos poner random como nombre del archivo ya que genera error
# random.radint(minimo, maximo)
import random

def run():
    number_found = False
    random_number = random.randint(0, 20)
    
    while not number_found:
        number = int(input("intenta con un numero"))

        if number == random_number:
            print("lo Conseguiste")
        elif number > random_number:
            print("es un numero mas pequeño")
        else:
            print("es un numero mayor")


if __name__ == "__main__":
    run()