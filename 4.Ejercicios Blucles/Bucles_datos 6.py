diccionario = {}
prompt = '> '
print("Introduce una lista de palabras y su traduccion separada por :")
palabras = input(prompt)

for i in palabras.split(','):
    palabra, traduccion = i.split(':')
    diccionario[palabra] = traduccion


print("Introduce el texto a traducir")
texto = input(prompt)
for i in texto.split():
    if i in diccionario:
        print(diccionario[i])
    else:
        print(i)