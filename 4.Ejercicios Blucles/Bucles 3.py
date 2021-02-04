prompt = '> '
print("Introduzca un numero")
numero = int(input(prompt))
for i in range(numero):
    if i%2 !=0:
        print(i ,end=',')