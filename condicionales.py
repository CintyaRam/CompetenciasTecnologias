import random
x = 20
"""
if x > 10:
    print("El número ingresado es mayor a 10")
    print("El valor de x es: ", x)
else:
    print("El número es menor a 10")


edad_infante = 4

if edad_infante < 2:
    print("El infante es un bebesito")
elif edad_infante < 5:
    print("El infante es un toddler")
else:
    print("El infante es un niño")


#&& and ?
temperatura = 20
esta_lloviendo = False
if temperatura > 18 and not esta_lloviendo: #! not
    print("Salgamos al parque a pasear!!")
else:
    print("Quedémonos en casa a descansar!")

#|| or
edad = 17
permiso_padres = True
if edad >= 18 or permiso_padres:
    print("Ya puedes obtener tu licencia de conducir")

# < > <= >= == !=
# and or not

'''
ADIVINA ADIVINADOR
Pide al usuario que ingrese un número del 1 al 10.
Crea un número aleatorio mágico ;)

Muestra un mensaje especial según si:
Le atinó,
Estuvo cerca (a 1 número de distancia),
Falló por mucho.
'''




print("ADIVIIIIINA ADIVINADOOOOOOOOR")



numero_magico = random.randrange(1, 11)


while True:
    numero = input("¡Ingresa el numerito del 1 al 10 a ver si le achuntas!: ")
    if numero.isdigit():
        numero = int(numero)
        if 1 <= numero <= 10:
            break
        else:
            print("El número debe estar entre 1 y 10, ingrésalo de nuevo porfa compa.")
    else:
        print("Compita, eso que ingresaste no es válido, intenta otra vez.")

if numero == numero_magico:
    print("¡Felicidades! Le achuntaste al numerito, en efecto es", numero_magico)
elif abs(numero - numero_magico) == 1:
    print("¡Uuuuuuuuy, caaaaaasi le achuntas criaturita!")
else:
    print("Mala sueeerte, no le atinaste :c")
"""

'''
MOOD DEL DÍA
Pide al usuario que ingrese su estado de ánimo (feliz, triste, cansado, emocionado).
Según la respuesta, muestra un mensaje motivador o divertido.
'''
"""
print("MOOD DEL DÍA, CÓMO ESTÁS MIJO?")
animo = input("Ingresa tu estado de ánimo, pueden ser los siguientes: feliz - triste - cansado - emocionado: ").lower()
flag = True
while flag:
    if animo == "feliz":
        print("Wachis, que maravilloso saber que te sientes feliz :3")
        flag = False
    elif animo == "triste":
        print("Pucha compa, échate unos gatitos encima a ser si pasa la pena :c")
        flag = False
    elif animo == "cansado":
        print("¡Un tutito y se nos reinicia la vida!")
        flag = False
    elif animo == "emocionado":
        print("Ay compa! Comparta un poquito de motivación!")
        flag = False
    else:
        print("Lo siento, no te entendí... Puedes volver a decirme cómo te sientes?")
        animo = input("Ingresa tu estado de ánimo, pueden ser los siguientes: feliz - triste - cansado - emocionado: ").lower()

"""


'''
3 NUMERITOS
Pide tres números. Según sus valores y la suma total, el programa mostrará un mensaje. Solo una opción se mostrará, la primera que cumpla:

Si todos los números son 0: mostrar "Todos los números son cero."
Si algún número es negativo: mostrar "Tienes al menos un número negativo."
Si los tres números son iguales a 100: mostrar "¡Triple 100!"
Si todos los números son iguales: mostrar "Todos los números son iguales."
Si la suma es mayor a 300: mostrar "La suma es altísima."
Si la suma está entre 201 y 300: mostrar "La suma es alta."
Si la suma está entre 101 y 200: mostrar "La suma es media."
Si la suma es 100 o menos: mostrar "La suma es baja."
En cualquier otro caso (no debería ocurrir, pero por buenas prácticas): mostrar "Caso no contemplado. Misterio sin resolver"
'''

print("3 NUMERITOS")

print("A ver compita, ingrese 3 números para poner a prueba: ")



while True:
    num_1 = input("Número 1: ")
    num_2 = input("Número 2: ")
    num_3 = input("Número 3: ")

    if num_1.isdigit() and num_2.isdigit() and num_3.isdigit():
        num_1 = int(num_1)
        num_2 = int(num_2)
        num_3 = int(num_3)
        break
    else:
        print("Las 3 variables deben ser números.")

suma = num_1 + num_2 + num_3

if num_1 == num_2 == num_3 == 0:
    print("Todos los números son cero.")
elif num_1 < 0 or num_2 < 0 or num_3 < 0:
    print("Tienes al menos un número negativo.")
elif num_1 == num_2 == num_3 == 100:
    print("¡Triple 100!")
elif num_1 == num_2 == num_3:
    print("Todos los números son iguales.")
elif suma > 300:
    print("La suma es altísima.")
elif suma > 200 and suma <= 300:
    print("La suma es alta.")
elif suma > 100 and suma <= 200:
    print("La suma es media.")
elif suma <= 100:
    print("La suma es baja.")
else:
    print("Caso no contemplado. Misterio sin resolver...")

