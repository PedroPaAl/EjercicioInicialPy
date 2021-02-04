prompt = '> '
print("Introduzca un numero")
numero = int(input(prompt))
try:
    f = open("tabla-%d.txt"%numero, "r")
    for i in range(11):
        print(f.readline())
    f.close()
except IOError:
    print("El archivo no existe")