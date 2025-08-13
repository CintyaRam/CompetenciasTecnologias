from Libro import Libro

class Biblioteca():

    def __init__(self):
        try:
            biblioteca = open("biblioteca.txt", "r", encoding="utf-8")
            lista = biblioteca.readlines()
            lista_objetos = []
            for linea in lista:
                objeto = Libro.from_csv(linea)
                lista_objetos.append(objeto)
            self.lista_libros = lista_objetos
        except FileNotFoundError:
            print('El archivo no se encuentra.')
        except IOError:
            print('No se pudo leer o modificar el archivo.')
        finally:
            try: 
                biblioteca.close()
            except NameError:
                print('No se pudo cerrar el archivo debido a un error')

    def agregar_libro(self):
        bandera = True
        while bandera:
            try:
                biblioteca = open("biblioteca.txt", "a", encoding="utf-8")
                titulo = input("Ingresa el título del libro: ").title()
                autor = input("Ingresa el autor del libro: ").title()
                anio = input("Ingresa el año de publicación del libro: ")
                estado = input("Ingresa el estado en el que se encuentra el libro (disponible o prestado): ").capitalize()
                if estado.lower() != "disponible" and estado.lower() != "prestado":
                    raise ValueError
                else:
                    nuevo_libro = Libro(titulo, autor, anio, estado)
                    biblioteca.write(nuevo_libro.to_csv() + "\n")
                    self.lista_libros.append(nuevo_libro)
                    print(f"Libro agregado: {nuevo_libro}")
                    bandera = False
            except ValueError:
                print('El valor para estado debe ser "disponible" o "prestado".')
            except FileNotFoundError:
                print('El archivo no se encuentra.')
            except IOError:
                print('No se pudo leer o modificar el archivo.')
            finally:
                try: 
                    biblioteca.close()
                except NameError:
                    print('No se pudo cerrar el archivo debido a un error')

    def eliminar_libro(self):
        libro_buscado = input("Ingresa el título del Libro que quieres eliminar: ").title()
        encontrado = False
        for libro in self.lista_libros:
            if libro_buscado == libro.titulo:
                self.lista_libros.remove(libro)
                print(f"El libro {libro.titulo} ha sido eliminado.")
                encontrado = True
        if encontrado is False:
            print(f"El libro {libro_buscado} no fue encontrado en la biblioteca")
        else:
            self.sobreescribir_archivo()
            
    def sobreescribir_archivo(self):
        try:
            biblioteca = open("biblioteca.txt", "w", encoding="utf-8")
            for linea in self.lista_libros:
                biblioteca.write(linea.to_csv() + "\n")
        except FileNotFoundError:
            print('El archivo no se encuentra.')
        except IOError:
            print('No se pudo leer o modificar el archivo.')
        finally:
            try: 
                biblioteca.close()
            except NameError:
                    print('No se pudo cerrar el archivo debido a un error')



    def listar_libros(self):
        if len(self.lista_libros) == 0:
            print("No tienes libros para mostrar.")
        else:
            for libro in self.lista_libros:
                print(libro)

    def buscar_libro(self):
        libro_buscado = input("Ingresa el título del Libro que quieres buscar: ").title()
        encontrado = False
        for libro in self.lista_libros:
            if libro_buscado == libro.titulo:
                print(f"Libro encontrado: {libro.__str__()}")
                encontrado = True
                print("¿Deseas cambiar el estado del libro?")
                bandera = True
                while bandera:
                    try:
                        opcion = input("Ingresa 1 para cambiar a Prestado, 2 para Disponible, 3 para volver al menú principal: ").strip()
                        if opcion == "1":
                            libro.set_estado(Biblioteca.prestar(libro.get_estado()))
                            print("Se ha cambiado el estado satisfactoriamente.")
                            self.sobreescribir_archivo()
                            bandera = False
                        elif opcion == "2":
                            libro.set_estado(Biblioteca.devolver(libro.get_estado()))
                            print("Se ha cambiado el estado satisfactoriamente.")
                            self.sobreescribir_archivo()
                            bandera = False
                        elif opcion == "3":
                            bandera = False
                            self.menu()
                        else:
                            raise ValueError
                    except ValueError:
                        print("La opción ingresada no es válida, ingresa 1, 2 o 3.")
        if encontrado == False:
            print(f"El libro {libro_buscado} no fue encontrado en la biblioteca")

    def prestar_libro(self):
        libro_prestar = input("Ingresa el título del libro que deseas prestar: ").title()
        encontrado = False
        for libro in self.lista_libros:
            if libro_prestar == libro.titulo:
                print(f"Libro encontrado: {libro.__str__()}")
                encontrado = True
                libro.set_estado(Biblioteca.prestar(libro.get_estado()))
                print("Se ha cambiado el estado del libro a Prestado.")
                self.sobreescribir_archivo()    
        if encontrado == False:
            print(f"El libro {libro_prestar} no fue encontrado en la biblioteca")


    def devolver_libro(self):
        libro_devuelto = input("Ingresa el título del libro que deseas devolver: ").title()
        encontrado = False
        for libro in self.lista_libros:
            if libro_devuelto == libro.titulo:
                print(f"Libro encontrado: {libro.__str__()}")
                encontrado = True
                libro.set_estado(Biblioteca.devolver(libro.get_estado()))
                print("Se ha cambiado el estado del libro a Disponible.")
                self.sobreescribir_archivo()
        if encontrado == False:
            print(f"El libro {libro_devuelto} no fue encontrado en la biblioteca")


    def menu(self):
        while True:
            print("""\n
 ----------------------
    Sistema de Gestión Bibliotecaria:

    1 - Agregar un libro
    2 - Eliminar libro
    3 - Listar libros
    4 - Buscar libro
    5 - Prestar libro
    6 - Devolver libro
    7 - Salir del Programa
----------------------""")
        
            try:
                opcion = input("Ingresa una opción: ").strip()
                if opcion == "1":
                    self.agregar_libro()
                elif opcion == "2":
                    self.eliminar_libro()
                elif opcion == "3":
                    self.listar_libros()
                elif opcion == "4":
                    self.buscar_libro()
                elif opcion == "5":
                    self.prestar_libro()
                elif opcion == "6":
                    self.devolver_libro()
                elif opcion == "7":
                    print("Has salido del programa satisfactoriamente.")
                    break
                else:
                    raise ValueError
            except ValueError:
                print("El valor ingresado no es válido, ingresa una opción del 1 al 7.")


    @staticmethod
    def prestar(estado):
        try:
            if estado == "Prestado":
                raise ValueError
            else:
                estado = "Prestado"
                return estado
        except ValueError:
            print("No se puede cambiar el estado, el libro ya se encuentra prestado.")
                      
    @staticmethod
    def devolver(estado):
        try:
            if estado == "Disponible":
                raise ValueError
            else:
                estado = "Disponible"
                return estado
        except ValueError:
            print("No se puede cambiar el estado del libro, ya se encuentra disponible.")

    



