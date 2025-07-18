from pprint import pprint
def menu():
    tareas = []
    while True:
        print("--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        print("Elige una opción: ")
        opcion = validarOpcion()
        if opcion == 1:
            agregarTarea(tareas)
        elif opcion == 2:
            verTareas(tareas)
        elif opcion == 3:
            marcarTarea(tareas)
        elif opcion == 4:
            eliminarTarea(tareas)
        else:
            print("¡Has salido del programa exitosamente!")
            break

def agregarTarea(tarea):
    nombreTarea = input("Ingrese el contenido de su tarea: ")
    estadoTarea = validarEstado()
    if estadoTarea == 1:
        diccionario = {"tarea": nombreTarea, "estado": "pendiente"}
    else:
        diccionario = {"tarea": nombreTarea, "estado": "completada"}
    tarea.append(diccionario)
    print("¡Su tarea ha sido agregada satisfactoriamente!")
    print()

def verTareas(tarea):
    if len(tarea) == 0:
        print("No tienes tareas para mostrar")
    else:
        pprint(tarea)
    print()

def marcarTarea(tarea):
    nombre = input("Ingresa tu tarea tal cual como la registraste: ").lower()
    encontrado = 0
    for elementos in tarea:
        if elementos["tarea"].lower() == nombre:
            elementos["estado"] = "completada"
            encontrado += 1
    if encontrado > 0:
        print("El estado de tu tarea ha sido cambiada a 'completada' con éxito.")
    else:
        print("No encontramos una tarea con la descripción señalada, por favor ver tareas para buscar una que coincida.")
    print()


def eliminarTarea(tarea):
    nombre = input("Ingresa tu tarea tal cual como la registraste: ").lower()
    encontrado = 0
    for i in range(len(tarea)):
        if tarea[i]["tarea"].lower() == nombre:
            tarea.pop(i)
            encontrado += 1
            break
    if encontrado > 0:
        print("¡La tarea ha sido eliminada satisfactoriamente!")
    else:
        print("No se encontró una tarea con la descripción señalada, por favor ver tareas para buscar una que coincida")
    print()



def validarOpcion():
    while True:
        try:
            valor = int(input("Ingrese un número del 1 al 5: "))
            if valor == 1 or valor == 2 or valor == 3 or valor == 4 or valor == 5:
                return valor
            else:
                print("Por favor ingresa un número del 1 al 5")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def validarEstado():
    while True:
        try:
            print("Ingrese 1 para estado de tarea 'Pendiente'")
            print("Ingrese 2 para estado de tarea 'Completada'")
            valor = int(input("Ingrese número 1 o número 2: "))
            if valor == 1 or valor == 2:
                return valor
            else:
                print("Por favor ingresa un número del 1 al 5")
        except ValueError:
            print("Por favor, ingrese un número válido.")


menu()