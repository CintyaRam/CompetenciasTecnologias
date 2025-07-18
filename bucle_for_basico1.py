print("Números del 10 al 100: ")
for enteros in range(101):
    print(enteros)
print("")

print("Múltiplos de 2:")
for multiplo in range(2, 501, 2):
    print(multiplo)
print("")

print("Contando Vanilla Ice!!")
for numero in range(1, 101):
    if numero%10 == 0:
        print("Baby")
    elif numero%5 == 0:
        print("Ice ice")
    else:
        print(numero)
print("")

print("Wow. Número gigante a la vista!!!")
suma = 0
for par in range(0, 500001, 2):
    suma += par
print(f"La suma de todos los números pares entre 0 y 500.000 es: {suma}")
print("")

print("Regrésame al 3:")
for i in range(2024, 1, -3):
    print(i)

print("")

numInicial = 2
numFinal = 305
multiplo = 5
print("Contador dinámico:")
for num in range(numInicial, numFinal+1):
    if num%multiplo == 0:
        print(num)
    else:
        continue

