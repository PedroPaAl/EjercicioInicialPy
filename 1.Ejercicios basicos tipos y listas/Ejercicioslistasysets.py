
#Ejercicio 2
x = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
print(x)

#Ejercicio 3
print("Yo estudio", x)

#Ejercicio 4

x = x + ["Matematicas"]

print(x)
y = set(x)
print(y)

#Ejercicio 5

numeros = [1,2,3]
cadenas = ["hola","mundo"]
numeros.append(cadenas)
print(numeros)

#ejercicio 6

A = ["Jake","John","Eric"]
B = ["John","Jill"]

C = set(A)
D = set(B)

print(C.difference(D))

#Ejercicio 7
x = [1,2,3,4,5]
[y**2 for y in x]
print(x)
