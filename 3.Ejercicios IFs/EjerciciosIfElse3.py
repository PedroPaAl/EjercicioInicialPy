prompt = '> '
contraseña = "Hola1"
print("escriba la contraseña")
respuesta = input(prompt)
if (contraseña.upper() == respuesta.upper()):
 print("contraseña correcta")
else:
 print("contraseña incorrecta")