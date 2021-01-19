import re
#Ejercicio 1
nombre = "Juan Perez"
balance = 53.44
print("Hola %s. Su balance es de %.2f$." % (nombre,balance))

#Ejercicio 2
decimal = 2.2
entero = 5
texto = "Paco"

decimalString = str(decimal)
print(decimalString)

decimal = int(decimal)
print(decimal)

#Ejercicio 3
#No se puede usar len con enteros y decimales
entero = 50
entero_a_string = str(entero)

longitud = len(entero_a_string)
print(longitud)

#Ejercicio 4

texto = "Hola me llamo Pedro"
tsplit = texto.split()

tfind = texto.find("a")
tindex = texto.index("e")
print (tsplit,"La letra a se encuentra en la posicion",tfind)

print ("La letra e se encuentra en la posicion",tindex)

texto = "hOlAaAaAa"
tlower = texto.lower()
tupper = texto.upper()
tstarwith = texto.startswith("h")
print(tupper,tlower)
print("Empieza el texto ",texto,"con la letra h?", tstarwith)

 #Ejercicio 5.

texto ="En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor."
 
r1 =len(re.findall(r"a",texto))
print(r1)