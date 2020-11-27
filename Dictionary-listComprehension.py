# -*- coding: utf-8 -*-

numeros = []

for num in range(1,31):
    if num % 2 == 0:              # => normal
        numeros.append(num) 

pares = {num: num**2 for num in range(1, 11)} # ==> 
