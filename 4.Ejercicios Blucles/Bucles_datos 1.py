x = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
notas = []
prompt = '> '
for i in range(len(x)):
    print("Introduzca una nota para %s" % (x[i]))
    notas.append(int(input(prompt)))
for i in range(len(notas)):
    print(x[i],":",notas[i])
