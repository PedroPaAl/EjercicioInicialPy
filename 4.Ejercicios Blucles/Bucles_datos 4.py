prompt = '> '
print("Introduzca una palabra")
palabra = input(prompt)
if palabra == palabra[::-1]:
    print("%s es palindromo" % palabra)
else:
    print("%s no es palindromo" % palabra)