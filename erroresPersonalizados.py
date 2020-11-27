# -*- coding: utf-8 -*-

# con esto podemos hacer que los programas sean mas robustos ya que en vez de mostrar error y romper el codigo simplemete le asignamos una funcion 
# print diciendo que no esta en el diccionario ... y asi poder seguir usando el programa sin tener que volverlo a abrir

countries = {
    'mexico' : 122,
    'colombia' : 49,
    'chile' : 18,
    'argentina' : 43,
    'peru' : 31
}

while True:
    country = str(input('Escribe el nombre de un pais: ')).lower()

    # aqui con try, except y el tipo de error... podemos personalizar el error dandole un uso de funcion
    try:
        print('la poblacion de {} es: {} millones'.format(country, countries[country]))
    except KeyError:                                                                        
        print('No tenemos el dato de la poblacion de {}'.format(country))