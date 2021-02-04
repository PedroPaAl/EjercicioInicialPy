prompt = '> '
print("Introduzca un numero")
numero = int(input(prompt))
f = open("tabla-%d.txt"%numero, "w")
for i in range(11):
    f.write("%dx%d=%d\n"% (numero,i,numero*i))
f.close()