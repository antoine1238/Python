import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="antoine",
    db="simple_db"
)
cursor = connection.cursor()


def añadir():
    nombre = input("nombre: ")
    apellido = input("apellido: ")
    edad = int(input("edad: "))
    sql = "INSERT INTO personas(nombre, apellido, edad) VALUES('{0}','{1}',{2})".format(nombre, apellido, edad)
    
    cursor.execute(sql)
    connection.commit()


def eliminar():
    nombre = input("nombre: ")
    sql = "DELETE FROM personas where nombre='{}'".format(nombre)
    
    cursor.execute(sql)
    connection.commit()


def run():
    while True:
        variable = input("""
            [a]ñadir
            [e]liminar
            [S]alir
        """)

        if variable.lower() == "a":
            añadir()
        elif variable.lower() == "e":
            eliminar()
        elif variable == 's' or "S":
            break
        else: 
            print("comando no encotrado :(")

if __name__ == "__main__":
    run()