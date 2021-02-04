
#Ejercicio 2 (el 1 es online)

prompt = '> '
dineros = {"Euro": "€", "Dollar": "$", "Yen": '¥'}
print("¿De que moneda desea conocer el simbolo?")
divisa = input(prompt)
print("El simbolo del",divisa,"es",dineros.get(divisa,"Divisa no disponible"))