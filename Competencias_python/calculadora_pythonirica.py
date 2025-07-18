'''
=========================================
    Calculadora Pythonirica!
=========================================
Elige una opción:

1. Sumar dos números
2. Restar dos números
3. Multiplicar dos números
4. Dividir dos números (con validación de 0)
5. Calcular el cuadrado y cubo de un número
6. Contar cuántas letras tiene una palabra
7. Saber si una palabra es corta, media o larga
8. Calcular el promedio de tres números
9. Comparar tres números y decir cuál es el mayor
10. Convertir una palabra a MAYÚSCULAS, minúsculas y contar vocales
11. Salir de la Súper Calculadora

=========================================
Recomendaciones:
-Usar try-except
-Revisar que los números sean válidos para cada acción
-Eliminar espacios y validar que hayan ingresado una palabra en los casos de palabras
-En el promedio, redondear
'''

def validar_numero():
    while True:
        valor = input("Ingrese un número: ")
        try:
            return float(valor)
        except ValueError:
            print("Por favor, ingrese un número válido.")

def validar_not_cero():
    while True:
        valor = input("Ingrese un número distinto a cero: ")
        try:
            valor = float(valor)
            if valor != 0:
                return valor
            else:
                print("El valor ingresado debe ser distinto de cero >:C  ")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def validar_palabra():
    while True:
        pal = (input("Ingrese una palabra: ")).strip()
        if pal == "":
            print("Ingresa una palabra válida.")
        else:
            return pal


def menu():
    while True:
        print("=========================================")
        print("Calculadoooora Pitoniiiiiiiiiisaaaaa")
        print("=========================================")
        print("")
        print("Elige una opción:")
        print("")
        print("1. Sumar dos números")
        print("2. Restar dos números")
        print("3. Multiplicar dos números")
        print("4. Dividir dos números (con validación de 0)")
        print("5. Calcular el cuadrado y cubo de un número")
        print("6. Contar cuántas letras tiene una palabra")
        print("7. Saber si una palabra es corta, media o larga")
        print("8. Calcular el promedio de tres números")
        print("9. Comparar tres números y decir cuál es el mayor")
        print("10. Convertir una palabra a MAYÚSCULAS, minúsculas y contar vocales")
        print("11. Salir de la Súper Calculadora")
        print("")
        opc = validar_numero()
        print("")
        if opc == 1:
            print("Vamos a sumar!")
            a = validar_numero()
            b = validar_numero()
            suma = a + b
            print("")
            print(f"El resultado de tu suma es: {suma}.")
        elif opc == 2:
            print("Vamos a restar!")
            a = validar_numero()
            b = validar_numero()
            resta = a - b
            print("")
            print(f"El resultado de tu resta es: {resta}.")
        elif opc == 3:
            print("Ok compa, vamos a multiplicar!")
            a = validar_numero()
            b = validar_numero()
            multiplicación = a * b
            print("")
            print(f"El resultado de la multiplicación es: {multiplicación}.")
        elif opc == 4:
            print("Vamos a dividir!")
            a = validar_numero()
            b = validar_not_cero()
            division = a / b
            print("")
            print(f"El resultado de la división es: {division}.")
        elif opc == 5:
            print("Calculemos tu número al cuadrado y al cubo!!")
            a = validar_numero()
            print("")
            print(f"El resultado de tu número al cuadrado es {a ** 2} y al cubo es {a ** 3}.")
        elif opc == 6:
            print("Vamos a contar letritas mijo!")
            palabra = (input("Ingresa una palabra: ")).strip()
            print("")
            print(f"Tu palabra tiene {len(palabra)} letras")
        elif opc == 7:
            print("Vamos a ver qué tan larga es tu palabra...")
            palabra = validar_palabra()
            print("")
            if len(palabra) <= 4:
                print("Tu palabra es corta")
            elif len(palabra) <= 8:
                print("Tu palabra es mediana")
            else:
                print("Tu palabra es laaaaaaaarga!")
        elif opc == 8:
            print("Vamos a calcular el promedio de 3 numeritos!")
            a = validar_numero()
            b = validar_numero()
            c = validar_numero()
            promedio = round(((a + b + c) / 3), 2)
            print("")
            print (f"El promedio de tus tres números es: {promedio}.")
        elif opc == 9:
            print("¿Quieres saber cuál es el mayor de 3 números? Ingrésalos!")
            a = validar_numero()
            b = validar_numero()
            c = validar_numero()
            print("")
            if a > b and a > c:
                print(f"Tu número {a} es el mayor de los 3!!!")
            elif b > a and b > c:
                print(f"Tu número {b} es el mayor de los 3!!!")
            else:
                print(f"Tu número {c} es el mayor de los 3!!!")
        elif opc == 10:
            print("Vamos a convertir tu palabrita pitonisa!")
            palabra = validar_palabra()
            print("")
            print(f"Tu palabra {palabra} en mayúsculas: {palabra.upper()}.")
            print(f"Tu palabra {palabra} en minúsculas: {palabra.lower()}.")
            palabra_contar = palabra.lower()
            contador = 0
            contador += palabra_contar.count("a")
            contador += palabra_contar.count("e")
            contador += palabra_contar.count("i")
            contador += palabra_contar.count("o")
            contador += palabra_contar.count("u")
            print(f"Tu palabra tiene {contador} vocales compis!")
        elif opc == 11:
            print("Entonceh...")
            print("Saliste satisfactoriamente de la calculadora pitonisa!!!!")
            break
        else:
            print("La opción ingresada no es válida... ingresa una opción del 1 al 10")




menu()

