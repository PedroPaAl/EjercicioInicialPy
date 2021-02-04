from sys import argv

script, user_name = argv


#Ejercicio 1

apellido = argv
prompt = '> '

print("Como se llama?")
nombre = input(prompt)
print("Cual es su apellido?")
apellido =input(prompt)
print("Escriba su DNI")
dni = input(prompt)

print('''Su nombre es %s
         su apellido es %s
         su dni es %d''',nombre,apellido,dni)