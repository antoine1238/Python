# este archivo no debe llamarse csv.py

#  Lectura
import csv 

with open("documento.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        print("{} - {} - {}".format(row[0], row[1], row[2]))



# Escritura
personas = [
    ["charles", "manuel", 23],
    ["douglas", "garvet", 19],
    ["fido", "nose", 23],
]
    

with open("documento.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerows(personas)


# Eliminación
# lo que hacemos es eliminar todo y luego volver a guardar segun los datos que esten en contactos
contactos = [
    ["charles", "manuel", 23],
    ["douglas", "garvet", 19],
    ["fido", "nose", 23],
]

with open("documento.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    delete_id = int(input("contacto a eliminar: "))
    del contactos[delete_id]
    

    writer.writerows(contactos)


