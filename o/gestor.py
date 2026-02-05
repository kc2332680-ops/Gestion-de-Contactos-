def mostrar_menu():
    print("\n--- GESTOR DE CONTACTOS ---")
    print("1. Nuevo contacto")
    print("2. Buscar por ID")
    print("3. Listar todos")
    print("4. Salir")
    return input("Seleccione opción: ")

def nuevo_contacto():
    id_cont = input("ID: ")
    nom = input("Nombres: ")
    ape = input("Apellidos: ")
    corr = input("Correo: ")
    gen = input("Género: ")
    
    if input("Guardar? (s/n): ").lower() != 's':
        print("Cancelado")
        return
    
    try:
        with open("contactos.txt", "a", encoding="utf-8") as f:
            f.write(f"{id_cont};{nom};{ape};{corr};{gen}\n")
        print("Contacto guardado!")
    except IOError as e:
        print(f"Error al guardar: {e}")

def buscar_por_id():
    id_buscar = input("ID a buscar: ")
    encontrado = False
    try:
        with open("contactos.txt", "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split(";")
                if datos[0] == id_buscar:
                    print(f"\nID: {datos[0]}\nNombre: {datos[1]} {datos[2]}\nCorreo: {datos[3]}\nGénero: {datos[4]}")
                    encontrado = True
                    break
        if not encontrado:
            print("No encontrado")
    except FileNotFoundError:
        print("No hay contactos registrados")

def listar_contactos():
    print("\n--- LISTA DE CONTACTOS ---")
    try:
        with open("contactos.txt", "r", encoding="utf-8") as f:
            lineas = f.readlines()
            if not lineas:
                print("Sin contactos")
                return
            print(f"{'ID':<8} {'Nombre completo':<20} {'Correo':<25}")
            print("-"*55)
            for l in lineas:
                d = l.strip().split(";")
                print(f"{d[0]:<8} {d[1]} {d[2]:<15} {d[3]:<25}")
    except FileNotFoundError:
        print("Sin contactos registrados")

# Programa principal
print("Bienvenido al gestor!")
while True:
    opc = mostrar_menu()
    if opc == "1":
        nuevo_contacto()
    elif opc == "2":
        buscar_por_id()
    elif opc == "3":
        listar_contactos()
    elif opc == "4":
        print("Saliendo...")
        break
    else:
        print("Opción inválida")