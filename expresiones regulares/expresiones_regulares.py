import re 

string = "vamos a aprender expresiones regulares en python. python es un lenguaje de sintaxis sencilla"
palabra_encontrar = "expresiones"

busqueda = re.search(palabra_encontrar, string)     # >>> <re.Match object; span=(17, 28), match='aprender'>
find_all = re.findall("python", string)             # >>> ['python', 'python']

start = busqueda.start()    # >>> 17
end = busqueda.end()        # >>> 18
spam = busqueda.span()   # >>> (17, 28)   "una tupla"

"""
    ^ = para los caracteres que empiecen 
    $ = para los caracteres que terminen
    [] = busca si se encuentra en algun lugar el caracter colocado
    [a-z] = para obtener los elementos que contengan un determinado conjunto de letras. [<desde>-<hasta>]

    Coincidencias Basicas
    .       - Cualquier Caracter, excepto nueva linea
    \d      - Cualquier Digitos (0-9)
    \D      - Cualquier caracter menos los numeros
    \w      - Caracter de Palabra (a-z, A-Z, 0-9, _) 
    \W      - cualquier caracter menos letras y numeros (espacios, saltos de lineas, . @ : / -)
    \s      - Espacios de cualquier tipo. (espacio, tab, nueva linea)
    \S      - Todo menos los espacios

    Limites
    \b      - Limite de Palabra
    \B      - No es un Limite de Palabra
    ^       - Inicio de una cadena de texto
    $       - Final de una cadena de texto

    Cuantificadores:
    *       - 0 o Más
    +       - 1 o Más
    ?       - 0 o Uno
    {3}     - Numero Exacto
    {3,4}   - Rango de Numeros (Minimo, Maximo)

    Conjuntos de Caracteres
    []      - Caracteres dentro de los brackets
    [^ ]    - Caracteres que NO ESTAN dentro de los brackets

    Grupos
    ( )     - Grupo
    |       - Uno u otro
"""

personas = [
    "antoine manuel", 
    "richard enrique",
    "charles manuel", 
    "richard ernesto",
    "Sasuke uchiha",
    "Araña vermudez"
]
personas_2 = [
    "niños",
    "niñas",
    "camion",
    "camión"
]
estados = [
    "madrid1",
    "madrid2",
    "madrid3",
    "madridA",
    "madridB",
    "madridC",
    "barcelona:1",
    "barcelona.2",
    "barcelona..3"
]

# ^
for p in personas:
    if re.findall("^richard", p):
        print(f"^: {p}")

# $
for p in personas:
    if re.findall("manuel$", p):
        print(f"$: {p}")

# []
for p in personas:
    if re.findall("[k]", p):
        print(f"[]: {p}")
    
for p in personas_2: 
    if re.findall("niñ[oa]s", p):  # para buscar mas específicamente, muy útil
        print(f"[]: {p}")
            
for p in personas_2: 
    if re.findall("cami[oó]n", p):  # para traer a los que tengan o no acento
        print(f"[]: {p}")
    
# [rangos]
for p in personas:
    search = re.findall("[m-m]", p)
    if search:
        print(p)    # solo trae personas que tengan en su nombre la letra "m"  

for p in personas:
    search = re.findall("[a-a]$", p)
    if search:
        print(p)    # >>>  Sasuke uchiha

for p in personas:
    search = re.findall("^[A-A]", p) 
    if search:
        print(p)    # >>>  Araña vermudez. (sólo ese por empezar en mayuscula)

for e in estados:
    search = re.findall("madrid[0-2]", e) 
    if search:
        print(e)    # >>> madrid1  madrid2

# Negación
for e in estados:
    search = re.findall("madrid[^0-2]", e)  # trae a los que NO tengan los rangos dados. [^0-2] = negación
    if search:
        print(e)    # >>> madrid3

# Varios rangos
for e in estados:
    search = re.findall("madrid[0-2A-B]", e)  # justo al lado podemos agregar mas rangos para traer tambien los que cumplan esas especificaciones
    if search:
        print(e)    # >>> madrid1  madrid2  madridA  madridB

for e in estados:
    search = re.findall("madrid[^0-2A-B]", e) # trae los que no tengan esas especificaciones
    if search:
        print(e)    # >>> madrid3  madridC

for e in estados:
    search = re.findall("[.:]", e) # trae los que tengan esos caracteres
    if search:
        print(e)      # >>> barcelona:1  barcelona.2  barcelona..3


Match: sirve para analizar el inicio de un texto
nombre1 = "Antoine Manuel"

if re.match("antoine", nombre1): # Fallido porque no esta en mayuscula
    print("Encontrado")
else:
    print("Fallido")

if re.match("antoine", nombre1, re.IGNORECASE): # Encontrado porque asignamos "re.IGNORECASE" el cual admite mayusculas y minusculas por igual
    print("Encontrado")
else:
    print("Fallido")

# .<texto_sig.> = el punto representa cualquier palabra variable. devuelve true siempre y cuando el texto añadido sea el mismo, el punto es el único que puede variar
palabra = "poderio"
palabra2 = "joderio"

if re.match(".oderio", palabra) and re.match(".oderio", palabra2):  # "Encontrado" porque ambas poseen el mismo texto y el punto seria el variante 
    print("Encontrado")
else:       
    print("Fallido")


# \d = devuelve True si el string empieza con un dígito numérico 
numero = "123123"
numero_2 = "a123123"

if re.match("\d", numero): # True
    print("Econtrado")

if re.match("\d", numero_2): # False porque no empieza con numero
    print("Encontrado")


# Search : busca en todo el texto. encuentra una acoincidencia
for i in personas:
    search = re.search("manuel", i)
    if search:
        print(i)    #  antoine manuel  charles manuel

codigo = "asdasd21ajsdk kkaweqwe asdad171199askld"

if re.search("171199",codigo):
    print("encontramos el codigo")  # >>> True

palabra = re.search("171199", codigo)
print(palabra[0])  # >>> 171199



# Practicas
import re 

caracter = [
    "numero de telefono: 0416 961 4076",
    "numero de telefono: 0412 123 4567",
    "numero de codigo: 0-2-1-2",
    "https://www.youtube.com/watch?v=wfogZfIS03U&ab_channel=FalconMasters"
]

for i in caracter:
    search = re.findall("\d\-\d\-\d\-\d", i) # numero + simbolo " - "
    if search:
        print(i)    # >>> numero de codigo: 0-2-1-2

for i in caracter:
    search = re.findall("v=(\S{11})", i) # {11} es la cantidad especificada de caracteres que hay dentro y que queremos que traiga
    if search:
        print(search)  # >>> ['wfogZfIS03U']

for i in caracter:
    search = re.findall("\d{4} \d{3} \d{4}", i) # 4 num + espacio + 3 num + espacio + 4 num
    if search:
        print(search)   # >>> ['0416 961 4076'] ['0412 123 4567']
