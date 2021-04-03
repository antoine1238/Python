from urllib import request, parse


# print(dir(request))                           # Todas las funciones de request
# r = request.urlopen("https://www.google.com") # busqueda 
# r.read()                                      # contenido en estructura html y bytes
# r.peek()                                      # da una pequeña parte del contenido a diferencia de read()
# r.decode("UTF-8")                             # convierte de tipo binario a STR
# v = parse.urlencode(valores_a_parametros)     # convierte las palabras comunes en codigo para busquedas de urls


# busqueda simple
url = "https://www.youtube.com/watch?"  # 1) url a buscar
r = request.urlopen(url)                # 2) abrir la url
r = r.peek()                            # 3) almacenar los datos de la busqueda  .. se uso peek porque read toma demasiados datos
print(type(r))  # >>> <class 'bytes'>   

r = r.decode("UTF-8")                   # 4) cambiamos el tipo de datos a Str
print(type(r))  # >>> <class 'str'>
print(r)


# busqueda con parametros 
params = {"search_query": "colplay"}        # parametros
querystrings = parse.urlencode(params)      # >>> search_query=colplay

url = "https://www.youtube.com/results?" + querystrings  # >>> https://www.youtube.com/results?search_query=colplay
resp = request.urlopen(url)                 # Abrir la url
print(resp.code)                            # >>> 200

html = resp.read().decode("utf-8")          # de bytes a strings
print(html[:500])                           # solo imprimimos los primeros 500 caracteres


