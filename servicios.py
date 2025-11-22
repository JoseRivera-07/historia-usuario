# Plasmamos diagrama de flujo a codigo
inventario = []
# Función mínima para validar números decimales 
def es_float(valor):
    # Permite decimales usando solo métodos de cadena
    partes = valor.replace(".", "", 1)
    return partes.isdigit()



#Funcion para agregar producto al inventario

def agregar_prod():
    inv = 0
    while inv == 0:
        print("")
        finalizar = input("Desea continuar con el registro de productos? y/n ")
        if finalizar == "n":
            inv = 1
        elif finalizar == "y":
            print("Bienvenido al sistema inventario")
            print("")
            print("")

            # Nombre producto
            # Se solicita al usuario el nombre del producto
            nombre_p = str(input("Digite el nombre del producto que desea agregar: "))
            print("")

            # Tipo producto
            # Se solicita la categoría a la que pertenece el producto
            tipo_producto = str(input("Ingrese a que categoria pertenece: "))
            print("")

            #Validacion del que el dato ingresado sea válido
            valid_compra = False
            while valid_compra == False:  
                temp = input("Digite el precio de compra del producto: ")
                if es_float(temp):
                    valid_compra = True
                else:
                    print("")
                    print("Error: Ingrese un número válido para el precio de compra.")

            #Validacion del que el dato ingresado sea float y si no que se repita hasta que lo sea
            precio_compra = float(temp)
            print("")

            # Validacion para que el dato ingresado sea entero
            valid_cantidad = False
            while valid_cantidad == False:
                temp = input("Cuantas unidades agregaremos al inventario de este producto?: ")
                # Validación solo con isdigit (sin try/except)
                if temp.isdigit():
                    valid_cantidad = True
                else:
                    print("Error: Ingrese un número entero válido para la cantidad.")

            cant_disp = int(temp)
            print("")

            product = {"Nombre": nombre_p, "Categoria": tipo_producto, "Cantidad disponible":cant_disp, "Precio": precio_compra}

            inventario.append(product)
    
#Funcion mostrar el inventario
def mostrar_inventario(inventario):
    if inventario:
        print("")
        print("Actualmente, el inventario está así: ")
        indice_prod = 1
        cont = 0
        for i in inventario:
            print("")
            print(f"Nombre del producto {indice_prod}: {inventario[cont]["Nombre"]}  | Precio: {inventario[cont]["Precio"]} | Cantidad disponible: {inventario[cont]["Cantidad disponible"]}")
            cont += 1
            indice_prod += 1
    else:
        print("El inventario está vacío")


print(inventario)

def estadisticas_prod():
    av_inventario = 0

    cont = 0
    for i in inventario:

        # Se calcula el costo total del inventario (precio compra × cantidad)
        costo_total = inventario[cont]["Precio de compra"] * inventario[cont]["Cantidad disponible"]

        #Se calcula el costo del inventario 
        av_inventario = costo_total + av_inventario

    print("--------------------------------------------------------")
    print("                ESTADISTICAS INVENTARIO                 ")
    print("--------------------------------------------------------")

    est_inv = (av_inventario, len(inventario)) 
    print("El costo del inventario es de: $", est_inv[0])
    print(f"Hay un total de {est_inv[1]} productos en el inventario")
    
    