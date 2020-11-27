# # -*- coding: utf-8 -*-

# # ------------ejemplo de uso en listas-------------------------

# def average_temps(temps):
#     sum_of_temps = 0

#     for temp in temps:
#         sum_of_temps += temp

#     return sum_of_temps / len(temps)

# if __name__ == '__main__':
#     temps = [21, 24, 24, 22, 20, 23, 24]

#     average = int(average_temps(temps))
    
#     print('La temperatura promedio es: {}'.format(average))

# # -----------------------------------------------------------------

# # ----------asi se agregan elementos a la lista------------
# amigos = []
# # amigos.append("douglas") 
# # solo se suma de uno en uno

# variables = []
# # variables.append(1,2,3,4,5)
# # variables[0] == 1

# lista = [1, 2]
# lista2 = [3, 4]
# # lista3 = lista + lista2 == [1, 2, 3, 4]

# # ------------------------------------------------------------------------

# lista4 = "a"
# # lista5 = lista4 * 10 == ["a","a","a"......]

# #mi_lista[inicio:final:saltos]  len(lista)... para nombrar/marcar cantidad de elementos

# # mi_lista = ["douglas","charles","junior","carlos"]
# # mi_lista[3]= "emelin"
# # mi_lista.append("jesus roberto")
# # mi_lista == ["douglas","charles","junior","emelin","jesus roberto"] "[x]" cambia el elemento por el que asignemos

# # mi_lista.sort(x)       ordena los elementos

# # mi_lista.pop(x)        elimina el ultimo elemento
# # mi_lista.remove(x)     elimina a alguien en especifico
# # del mi_lista[x]        elimina a alguien en especifico

# # mi_lista.extend(otra_lista)  es basicamente sumar dos variables

# mi_lista = "casa"
# # mi_lista = list(mi_lista) == ["c", "a", "s", "a"]   los separa
# # str_casa = "".join(lista_casa) == "casa"            los junta

# # -------------------------diccionarios.--------------------------------

# para agregar
diccionario ={}
diccionario["primer_elemento"] = "hola"
diccionario["segundo_elemento"] = "adios"

# para inprimir el primer elemento// para imprimir el valor(.values)// para ambos en uno solo ( .items() )
for i in diccionario:
    print(i)

for v in diccionario.values():
    print(v)

for i, v in diccionario.items():
    print("palabra: {}, valor: {}".format( i , v ))



