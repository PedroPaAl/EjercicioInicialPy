prompt = '> '
numeros = []
print("Introduzca los numeros ganadores de la primitiva")
for i in range(7):    
    numeros.append(int(input(prompt)))
numeros.sort()
print(numeros)
