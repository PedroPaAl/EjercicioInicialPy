prompt = '> '


facturas = {}
beneficios = 0
perdidas = 0

print("Introduce 1 para pagar y 2 para cobrar una factura 3 para salir")
opcion = input(prompt)
while opcion != '3':
    if opcion == '1':

        print('Introduce el número de factura')
        factura=input(prompt)
        print("Introduce el coste")
        cantidad = float(input(prompt))
        facturas[factura] = cantidad
        perdidas += cantidad
    if opcion == '2':
        print('Introduce el número de factura')
        factura=input(prompt)
        print("Introduce el pago")
        cantidad = float(input(prompt))
        facturas[factura] = cantidad
        beneficios += cantidad
    print("Beneficio = ", beneficios)
    print("Perdidas = " , perdidas)
    print("Total beneficio=",beneficios-perdidas)
    print("Introduce 1 para pagar y 2 para cobrar una factura 3 para salir")
    opcion = input(prompt)
    