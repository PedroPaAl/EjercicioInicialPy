x = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
notas = []
asignaturas = []
prompt = '> '
for i in range(len(x)):
    print("Introduzca una nota para %s" % (x[i]))
    numero = int(input(prompt))
    if numero >=5:
        asignaturas.append(x[i])          
    else:
        notas.append(numero)
for i in range(len(asignaturas)):
    x.remove(asignaturas[i])
for i in range(len(notas)):
    print(print(x[i],":",notas[i]))

