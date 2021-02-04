frutas = {"Naranja": 1.20,"Pera":2.00,"Manzana":2.40}
prompt = '> '
print("Indique la fruta")
fruta = input(prompt)
print("Indique el numero de kg")
kilos = float(input(prompt))

precio = float(frutas.get(fruta,"Fruta no disponible"))
total = precio*kilos
print(total,"€")
