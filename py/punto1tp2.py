import os
"""
■ Nombre: String, entre 3 y 20 caracteres
■ Especie: (P= Perro, G= Gato, H= Hamster)
■ Edad: Entero, en años, rango [0, 20]
■ Peso: Float, en kilogramos
■ Estado de Salud: (S=Saludable, E=Enfermo, C=Control)
■ Dueño: Lista que contenga la información del dueño (DNI, Nombre, Teléfono, Dirección)
"""
# Lista vacía que almacenará otras listas
mascotas_ingresadas = [
    ["Wilson","Perro",15,10,"Enfermo",["Maximo Acosta",1234,3888,"Corbacho"]],
    ["Coki","Perro",10,8,"Saludable",["Maximo Acosta",1234,3888,"Corbacho"]],
    ["Olaf","Perro",1,10,"Saludable",["Maximo Acosta",1234,3888,"Corbacho"]],
    ["Culillo","Gato",6,5,"Enfermo",["Maximo Acosta",1234,3888,"Corbacho"]],
    ["Coco","Gato",1,6,"Saludable",["Maximo Acosta",1234,3888,"Corbacho"]],
    ["Tribilin","Gato",5,7.5,"Saludable",["Emilse Sanchez",4321,388843,"Providencia"]],
    ["Fidel","Gato",1,2,"Saludable",["Emilse Sanchez",4321,388843,"Providencia"]],
    ["Cala","Perro",2,12,"Enfermo",["Emilse Sanchez",4321,388843,"Providencia"]],
    
]

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print(
        "\n--- Menú de Opciones ---\n"
        "1. Opción 1: Ingresar mascotas\n"
        "2. Opción 2: Mostrar Mascotas Ingresadas x Dueño\n"
        "3. Opción 3: Buscar Mascota\n"
        "4. Opción 4: Actualizar salud de Mascota\n"
        "5. Opción 5: Mascotas ENFERMAS\n"
        "6. Opción 6: Salir \n"
        "------------------------"
    )






def ingresarMascotas():
    n = int(input("¿Cuántas mascotas deseas ingresar? "))
    for i in range(n):
        # Pedir al usuario los DATOS DE LA MASCOTA
        nombre = input(f"Ingrese el nombre de la mascota {i+1}: ")
        especie = input("Especie: (P= Perro, G= Gato, H= Hamster)")
        edad = int(input(f"Ingrese la edad de la mascota {i+1}: "))
        peso = float(input("Cuanto pesa?(en Kg):  "))
        estado_de_Salud = input("Estado de Salud: (S=Saludable, E=Enfermo, C=Control)") 
        #DATOS DUEÑO
        nombre_dueño = input("Ingrese el mombre del dueño: ")
        dni_dueño = int(input("DNI del dueño: "))
        tel_dueño = int(input("Ingrese telefono del dueño: "))
        dirección_dueño = input("Ingrese la dirección del dueño: ")
        
        if (especie == "P"):
            especie = "Perro"
        elif(especie == "G"):
            especie = "Gato"
        elif(especie == "H"):
            especie = "Hamster"

        if (estado_de_Salud == "S"):
            estado_de_Salud = "Saludable"
        elif(estado_de_Salud == "E"):
            estado_de_Salud = "Enfermo"
        elif(estado_de_Salud == "C"):
            estado_de_Salud = "Control"


        dueño = [nombre_dueño, dni_dueño, tel_dueño, dirección_dueño]
        # Crear una sublista con los datos ingresados
        sublista = [nombre,especie, edad, peso, estado_de_Salud, dueño]
        
        # Agregar la sublista a la lista principal
        mascotas_ingresadas.append(sublista)


def estadoDeSalud():
    # Solicitar el nombre de la mascota para buscarla
    nombreMascota = input("Ingrese el nombre de la mascota a actualizar: ")
    
    encontrada = False
    # Recorrer la lista de mascotas para encontrar la mascota por nombre
    for mascota in mascotas_ingresadas:
        if mascota[0].lower() == nombreMascota.lower():
            # Mostrar la mascota encontrada
            print(f"Mascota encontrada: {mascota}")
            # Pedir el nuevo estado de salud
            nuevo_estado = input("Ingrese el nuevo estado de salud: (S=Saludable, E=Enfermo, C=Control): ")

            # Convertir el estado a su valor correspondiente
            if nuevo_estado == "S":
                mascota[4] = "Saludable"
            elif nuevo_estado == "E":
                mascota[4] = "Enfermo"
            elif nuevo_estado == "C":
                mascota[4] = "Control"
            else:
                print("Estado de salud no válido.")
                return

            print(f"Estado de salud de {nombreMascota} actualizado a {mascota[4]}.")
            encontrada = True
            break
    
    if not encontrada:
        print(f"No se encontró ninguna mascota con el nombre {nombreMascota}.")

    input("\nPresione Enter para continuar...")  # Para pausar y permitir ver el resultado
            
    
    
def buscarMascotas():
    encontrada = False
    nombreBusqueda = input("Que mascota busca?: ")
    for mascota in mascotas_ingresadas:
        if mascota[0].lower() == nombreBusqueda.lower():
            print(f"Mascota encontrada: {mascota}")
            encontrada = True
            break
    
    if not encontrada:
        print("Mascota no encontrada, por favor busque por otro nombre")
    return 

def mascotaPorDueño():
    encontrada = False
    nombreDueño = input("Ingrese el nombre del dueño: ")
    for mascota in mascotas_ingresadas:
        if mascota[5][0].lower() == nombreDueño.lower():
            print(mascota)
            encontrada=True

    if not encontrada:
        print("Parece que esa persona no tiene mascotas aqui.")

def mascotasEnfermas():
    for mascota in mascotas_ingresadas:
        if mascota[4] == "Enfermo":
            print(mascota)
        

        


opcion = 0
while opcion != 6:
    menu() #Muestro el menu
    opcion = int(input("Ingrese una opcion (1-6): "))

    if opcion == 1:
        ingresarMascotas()
    elif opcion ==2:
        mascotaPorDueño()
    elif opcion == 3:
        buscarMascotas()
    elif opcion == 4:
        estadoDeSalud()
    elif opcion == 5:
        mascotasEnfermas()
    elif opcion == 6:
        print("Cerrando programa...")
