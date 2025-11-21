#Llamamos a la funcion agregar al inventario de la historia de usuario 1
from historia_1 import *
#Creacion del menú interacctivo
salir = False

while salir == False:

    print("Bienvenido,. ¿Que desear hacer hoy?")
    print("")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadisticas del producto")
    menu = input("4. Salir: ")

    match menu:

        case "1":
            #Vamos a preguntarle al usuario    
            print("")
            print("Redirigiendo a la funcion para agregar producto...")
            print("")
            #Aqui llamamos a la funcion
            append_inventario()
            inv = 0
            while inv == 0:
                print("")
                finalizar = input("Desea finalizar el registro de productos en inventario? (y/n): ")
                if finalizar == "y":
                    inv = 1
                elif finalizar == "n":
                    append_inventario()
        case "2":
            #Implementamos un ciclo for que nos recorra el inventario
            print("")
            print("Actualmente, el inventario está así: ")
            indice_prod = 1
            cont = 0
            for i in inventario:
                print("")
                print(f"Nombre del producto {indice_prod}: {inventario[cont]["Nombre"]} | Categoria: {inventario[cont]["Categoria"]} | Cantidad disponible: {inventario[cont]["Cantidad disponible"]} | Precio de compra: {inventario[cont]["Precio de compra"]} | Precio de venta al público: {inventario[cont]["Precio de venta al público"]}")
                cont += 1
                indice_prod += 1
        case "3":
            #Llamamos a la funcion estadisticas prod 
            estadisticas_prod()
        case "4":
            print("Saliendo del programa, gracias por utilizar nuestro servicio de inventario...")
            salir = True
