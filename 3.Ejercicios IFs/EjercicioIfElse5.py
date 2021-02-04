prompt = '> '
print("Introduzca el dividendo")
dividendo = int(input(prompt))
print("Introduzca el divisor")
divisor = int(input(prompt))
if divisor ==0:
    print("Error, el divisor no puede ser 0")
else:
    print(dividendo/divisor)