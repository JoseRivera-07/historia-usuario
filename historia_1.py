# Plasmamos diagrama de flujo a codigo
inventario = []
# Función mínima para validar números decimales 
def es_float(valor):
    # Permite decimales usando solo métodos de cadena
    partes = valor.replace(".", "", 1)
    return partes.isdigit()




def append_inventario():
    # Bienvenida
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

    #Validacion del que el dato ingresado sea float y si no que se repita hasta que lo sea
    valid_venta = False
    while valid_venta == False:
        temp = input("Digite el precio de venta del producto: ")
        if es_float(temp):
            valid_venta = True
        else:
            print("Error: Ingrese un número válido para el precio de venta.")

    precio_venta = float(temp)
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

    product = {"Nombre": nombre_p, "Categoria": tipo_producto, "Cantidad disponible":cant_disp, "Precio de compra": precio_compra, "Precio de venta al público": precio_venta }

    inventario.append(product)
    

print(inventario)

def estadisticas_prod():


    av_inventario = 0
    ganancia_inv = 0
    venta_tot = 0
    cont = 0
    for i in inventario:

        # Se calcula el costo total del inventario (precio compra × cantidad)
        costo_total = inventario[cont]["Precio de compra"] * inventario[cont]["Cantidad disponible"]

        #Se calcula el costo del inventario 
        av_inventario = costo_total + av_inventario

        # Se calcula el total de venta en caso de vender todo el inventario
        total_venta = inventario[cont]["Precio de venta al público"] * inventario[cont]["Cantidad disponible"]
        venta_tot = total_venta + venta_tot

        # La ganancia debería ser total_venta - costo_total
        ganancia = total_venta - costo_total
        ganancia_inv = ganancia + ganancia_inv

    print("--------------------------------------------------------")
    print("                ESTADISTICAS INVENTARIO                 ")
    print("--------------------------------------------------------")

    print("El inventario deja una ganancia de: $", ganancia_inv)
    print("El costo del inventario es de: $", av_inventario)
    print(f"Hay un total de {len(inventario)} productos en el inventario")
