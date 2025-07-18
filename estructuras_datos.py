#Lista / Array / Arreglo
lista_vacia = []
lista_compras = ["leche", "manzanas", "pan"]

print(lista_compras[1])

lista_compras[2] = "marraqueta"

print(lista_compras)

lista_compras.pop() #Elimina el último valor de mi lista
print(lista_compras)
lista_compras.pop(0) #Enviando un valor, elimina ese índice del listado
print(lista_compras)
lista_compras.append("pollo") #Agreda el elemento al final de la lista
print(lista_compras)
lista_compras.insert(1, "sal") #Se indica el índice y el valor a agregar
lista_compras.insert(1, "sal")
print(lista_compras)

print(lista_compras.index("sal"))
indice = lista_compras.index("manzanas")
lista_compras.pop(indice)
print(lista_compras)

lista_compras.remove("sal") #borra la primera ocurrencia que encuentre del valor

verso_1 = ['dale', 'a', 'tu', 'cuerpo']
verso_2 = ['alegria', 'macarena']
estrofa = verso_1 + verso_2
print(estrofa)
cancion = 3*estrofa
print(cancion)


lista_con_muchos_valores = [12, True, 1.2, "texto", ["otra", "lista"]]
print(lista_con_muchos_valores)

lista_grande = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista_grande[3:]) #parto a partir del índice 3 al final de mi lista
print(lista_grande[:6]) #parto desde el 0 hasta el límite 6
print(lista_grande[3:6]) #dividiendo desde índice 3 hasta límite 6

lista_numeros = [2, 7, 5, 9, 1, 2, 3, 5, 5]
print(len(lista_numeros))#longitud de mi secuencia
print(max(lista_numeros)) #valor máximo, se puede ocupar para string igual
print(min(lista_numeros)) #valor mínimo
print(sorted(lista_numeros))#ordenado
print(sorted(lista_numeros, reverse=True)) #De más grande a chico

cadena = ["ba", "ao", "wdak", "eoa"]
print(sorted(cadena, key = len)) #Ordena el sorted por tamaño 

print(lista_grande[:-1])#-1 es la última posición

#Tupla
tupla = ("a", "e", 3, "asdsa")
tupla_sin_p = "alskdj", "js", "asld", 1 #ambas sintaxis son correctas

print(tupla[2])
#tupla[2] = "j"error porque no se puede modificar

tupla = tupla + ("j", "k", "l")
print(tupla)
print(tupla[2:5])


#Diccionario: pares clave - valor
estudiante1 = {
    "nombre": "Juanita",
    "apellido": "Petronila",
    "email": "wikiliki@lala.cl",
    "edad": 22
}

estudiante2 = {
    "nombre": "Juana",
    "apellido": "Petrs",
    "email": "sdfsdfs@lala.cl",
    "edad": 74
}

print(estudiante1["edad"])

estudiante1["edad"] = 123

print(estudiante1["edad"])

estudiante2["curso"] = "Python" #agrega clave- valor nueva

print(estudiante2)

estudiante1.pop("edad")
print(estudiante1)

skillnest = {
    "nombre": "skillnest",
    "fecha_inicial": "2025-07-11",
    "cursos": [
        {"nombre": "Python", "duracion": 24, "modulos": ["Modulo1", "Modulo2", "Modulo3", "Modulo4", "Modulo5"]},
        {"nombre": "Java", "duracion": 16, "modulos": ["Fundamentos de Java", "POO", "Spring", "MVC"]}
               ]
}


skillnest["cursos"][0]["modulos"][2] = "Fundamentos de python"
#Impresion linda
from pprint import pprint

pprint(skillnest)

#Set valores únicos para usar operaciones matemáticas, no se pueden repetir

ids ={1, 2, 3, 4, 1}

print(ids)

set1 = {2, 3, 4, 5, 6}
set2 = {3, 5, 6, 7, 8}

print(set1.union(set2)) #se hace una unión
print(set1.intersection(set2)) #se muestran los elementos en común
print(set1.difference(set2))#Lo que difiere desde el primer set al segundo
print(set2.difference(set1))

print(set1.difference(set2) | set2.difference(set1)) #diferencia


estructura_datos = [200, 150, 300, 350]

for item in estructura_datos:
    print(item)

for indice in range(len(estructura_datos)):
    print(indice, estructura_datos[indice])


maestra = {
    "nombre": "Juanita",
    "apellido": "Salvador",
    "curso": "Python"
}
for clave, valor in maestra.items(): #maestra.keys() para claves y maestra.value() para valores
    print(clave, valor, sep=" = ")