# -*- coding: utf-8 -*-

# r = read 
# w = write 
# a = append 
# r+ = read and write

#con este metodo accedemos a la lectura del archivo y en este caso hacer un conteo de una palabra espicifica

def run():
    counter = 0 
    with open("ff.txt") as f:
        for line in f:
            counter += line.count("Zack")

    print("zack se encuentra {} en el texto".format(counter))


if __name__ == "__main__":
    run()


# con este metodo manejamos la escritura mediante un archivo a sobreescribir o crear automaticamente

def run():
    counter = 0 
    with open("ff.txt", "w") as f:
        for i in range(10):
            f.write(str(i))
            
if __name__ == "__main__":
    run()
