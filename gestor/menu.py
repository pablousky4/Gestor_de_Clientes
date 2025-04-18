import database as db
import helpers

def iniciar():
    while True:
        helpers.limpiar_pantalla()
        print("""
========================
  BIENVENIDO AL Manager 
========================
[1] Listar clientes     
[2] Buscar cliente      
[3] Añadir cliente      
[4] Modificar cliente   
[5] Borrar cliente      
[6] Cerrar el Manager   
========================
""")
        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            for cliente in db.Clientes.lista:
                print(cliente)
        elif opcion == '2':
            dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("Cliente no encontrado.")
        elif opcion == '3':
            while True:
                dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
                if helpers.dni_valido(dni, db.Clientes.lista):
                    break
            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
            apellido = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 chars)").capitalize()
            db.Clientes.crear(dni, nombre, apellido)
            print("Cliente añadido correctamente.")
        elif opcion == '4':
            dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(2, 30, f"Nombre [actual: {cliente.nombre}]").capitalize()
                apellido = helpers.leer_texto(2, 30, f"Apellido [actual: {cliente.apellido}]").capitalize()
                db.Clientes.modificar(dni, nombre, apellido)
                print("Cliente modificado correctamente.")
            else:
                print("Cliente no encontrado.")
        elif opcion == '5':
            dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
            if db.Clientes.borrar(dni):
                print("Cliente borrado correctamente.")
            else:
                print("Cliente no encontrado.")
        elif opcion == '6':
            print("Saliendo...")
            break

        input("\nPresiona ENTER para continuar...")
