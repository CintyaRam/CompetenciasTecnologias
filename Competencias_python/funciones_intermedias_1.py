matriz = [ [10, 15, 20], [3, 7, 14] ]
matriz[1][0] = 6
print(matriz)

cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes)

for cantante in cantantes:
    print(f"nombre - {cantante["nombre"]}, pais - {cantante["pais"]}")

for c in cantantes:
    print(c["nombre"])

for p in cantantes:
    print(p["pais"])



ciudades = {
   "México": ["Ciudad de México", "Guadalajara", "Cancún"],
   "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["México"][2] = "Monterrey"
print(ciudades)


coordenadas = [
   {"latitud": 8.2588997, "longitud": -84.9399704}
]
coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)

print()

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]

def iterarDiccionario(lista):
    for i in lista:
        frase = ""
        for clave, valor in i.items():
            frase += clave + " - " + valor + ", "
        print(frase[:-2])

iterarDiccionario(cantantes)

print()
def iterarDiccionario2(llave, lista):
    for i in lista:
        try:
            print(i[llave])
        except KeyError:
            print("No existe esa llave en el diccionario")

iterarDiccionario2("salsa", cantantes)
print()
iterarDiccionario2("pais", cantantes)

print()
costa_rica = {

   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}
def imprimirInformacion(diccionario):
    for clave, valor in diccionario.items():
        print(f"{len(valor)} {clave.upper()}")
        for elemento in sorted(valor): #sorted para ordenar alfabéticamente
            print(elemento)

imprimirInformacion(costa_rica)