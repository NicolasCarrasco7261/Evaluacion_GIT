alumnos = []

def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar un alumno")
    print("2. Mostrar todos los alumnos")
    print("3. Eliminar alumno por nombre")
    print("4. Salir")

def validar_nombre(nombre):
    return nombre.isalpha()

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        nombre = input("Ingresa el nombre del alumno: ")
        if validar_nombre(nombre):
            alumnos.append(nombre)
            print(f"Alumno '{nombre}' agregado.")
        else:
            print("Nombre inválido. Solo se permiten letras.")
    elif opcion == "2":
        print("Lista de alumnos:")
        for i, alumno in enumerate(alumnos, 1):
            print(f"{i}. {alumno}")
        if not alumnos:
            print("No hay alumnos en la lista.")
    elif opcion == "3":
        nombre = input("Ingresa el nombre del alumno a eliminar: ")
        if not validar_nombre(nombre):
            print("Nombre inválido. Solo se permiten letras.")
        elif nombre in alumnos:
            alumnos.remove(nombre)
            print(f"Alumno '{nombre}' eliminado.")
        else:
            print(f"El alumno '{nombre}' no está en la lista.")
    elif opcion == "4":
        print("Programa cerrado.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")