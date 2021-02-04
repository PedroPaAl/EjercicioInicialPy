prompt = '> '
print("Introduzca una palabra")
palabra = input(prompt)
conteo = {i:0 for i in 'aeiouAEIOU'}
for char in palabra:
    if char in conteo:
        conteo[char] +=1
for i,j in conteo.items():
    print(i,j)