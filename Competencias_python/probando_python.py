import random #Importa módulo random

print('¡Bienvenidos al Himalaya!') #Imprime por consola "¡Bienvenido a Python!"



print("Esta función pide un número mayor a 1 para imprimir un rango y decir si cada número impreso es par o impar.")
def impresionRango(a):
    while a <= 1:
        print("Ingrese un número válido")
        a = int(input("Ingrese un número número mayor a 1 para la cantidad de impresiones: "))
    else:
        for num in range(1, a+1):
            if (num%2)==0:
                print(f'El número {num} es par')
            else:
                print(f'El número {num} es impar')


rango = int(input("Ingrese un número mayor a 1 para la cantidad de impresiones: "))
impresionRango(rango)

menu = ['Pollo con papas fritas', 'Salmón a las finas hierbas', 'Ensalada César', 'Comida china', 'Recalentado']
comida = random.choice(menu)

print("¿Qué comeremos hoy?")
print(f'Hoy nos toca comer: {comida}')

if comida == 'Pollo con papas fritas':
    print('¡Que suerte!')
elif(comida == 'Salmón a las finas hierbas'):
    print('¡Que elegancia la de Francia!')
elif (comida == 'Ensalada César'):
    print('Hoy tocó comida ligera')
elif (comida == 'Comida china'):
    print('¡Trae la salsita!')
else:
    print('¡Mala suerte! Tocó Recalentado :c')