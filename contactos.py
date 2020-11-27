# -*- coding: utf-8 -*-

# self._name" el "_" hace que sea privado
# siempre se inicia con self y se llama para asignar
# si se quiere llamar un atributo o metodo dentro de un metodo se antepone la palabra self
# (color , material , etc) parametros

import csv

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:

    def __init__(self):
        self._contacts = []                             # creamos este array para guardar los contactos

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)                  #añadimos mediante append los parametros con los datos ya establecidos
        self._save()

    def show_all(self):
        for contact in self._contacts:                   #agarramos los datos del array y creamos una funcion con esos datos mediante el parametro "contact"
            self._print_contact(contact)

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):  #para poder borrar los contactos necesitamos del indice...este se obtiene
            if contact.name.lower() == name.lower():    #usando el metodo enumerate.. "lower" es para aplicar minusculas al texto
                del self._contacts[idx]
                self._save()
                break

    def search(self, name):
        for contact in self._contacts:                  #hagarramos los datos del array
            if contact.name.lower() == name.lower():    #si el contacto del array es == al asignado por el usuario
                self._print_contact(contact)            #usamos la funcion ya establecida mas el parametro del objeto 
                break
        else:
            self._not_found()                           #este else no esta con el if porque ya posee un break 

    def _save(self):
        with open('contacts.csv', 'w') as f:            #con esta funcion creamos una carpeta en la que se va a escribir los contactos y con
            writer = csv.writer(f)                      #lo cual hará que se guarden en memoria... w = escribir
            writer.writerow( ('name', 'phone', 'email') )

            for contact in self._contacts:
                writer.writerow( (contact.name, contact.phone, contact.email) )


    def actualizar(self, name):                         
        for contact in self._contacts:                  #tomamos los datos del array
            if contact.name.lower() == name.lower():    #abrimos la funcion comparativa
                contact_name = input("nombre: ")        #creamos unas variables las cuales seran rellenadas por el usuario
                contact_phone = input("telefono: ")
                contact_email = input("emali: ")

                contact.name = contact_name             #asignamos esas variables creadas 
                contact.phone = contact_phone
                contact.email = contact_email
                break

    def _print_contact(self, contact):                  #funcion para imprimir datos
        print("-.-.-.-.-.-.-.-.-.-.")
        print("nombre: {}".format(contact.name))
        print("telefono: {}".format(contact.phone))
        print("email: {}".format(contact.email))
        print("-.-.-.-.-.-.-.-.-.-.")

    def _not_found(self):                               #funcion para las teclas fuera del parametro de elecciones
        print('*******')
        print('¡No encontrado!')
        print('*******')


def run():

    contact_book = ContactBook()                         # con esta variable se trae la clase "" a la funcion

    with open('contacts.csv', 'r') as f:                 #con esta funcion hacemos que le lea el documento creado en la funcion "save" y se 
        reader = csv.reader(f)                           #traiga sus elementos guardados
        for idx, row in enumerate(reader):
            if idx == 0:                                 # no dejamos que el primer elemento se imprima ya que son innecesarios
                continue

            contact_book.add(row[0], row[1], row[2])     #pero si dejamos que los demás se impriman

    while True:                                          #ciclo sin fin para mostrar la interface de opciones
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el tel del contacto: '))
            email = str(input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)

        elif command == 'ac':
            name = input("contacto a actualizar")
            contact_book.actualizar(name)

        elif command == 'b':
            name = input("contacto a buscar: ")
            contact_book.search(name)

        elif command == 'e':
            name = input("contacto a eliminar: ")
            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('B I E N V E N I D O  A  L A  A G E N D A')
    run()