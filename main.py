import json
import datetime

with open("menu.json", "r") as openfile:
    menu = json.load(openfile)

with open("pagos.json", "r") as openfile:
    pagos = json.load(openfile)

with open("pedidos.json", "r") as openfile:
    pedidos = json.load(openfile)

print("/////////////////////////////////////////////////////")
print("                      MoliPollo                               ")
print("/////////////////////////////////////////////////////")
print("")

while True:

    print("1. Registrar pedido")
    print("2. Editar pedido")
    print("3. Registro de pago")
    print("4. Consulta de pedidos")
    print("5. Salir")
    print("")
    opcion = int(input("Ingrese una opción: "))
    print("")

    if opcion == 1:
        # Registrar pedido

        nombre_cliente = input("Ingrese el nombre del cliente: ")
        print("")
        print("Estas son las categorías disponibles:\n1. Entrada\n2. Plato Fuerte\n3. Bebida\n\n")
        
        opc = int(input("¿Qué desea pedir\n"))
        print("")

        if opc == 1:

            for i in menu[0]["entrada"]:
                print("Nombre:", i["nombre"], "----- ""Precio(COP): ", i["precio"])
            print("")

            productos_vendidos = []

            while True:
                nombre_producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
                if nombre_producto.lower() == 'salir':
                    break

                encontrado = False
                for producto in menu[0]["entrada"]:
                    if producto['nombre'].lower() == nombre_producto.lower():
                        precio = producto['precio']

                        cantidad = int(input("Ingrese la cantidad que desea comprar: "))

                        productos_vendidos.append({
                            "nombreMedicamento": nombre_producto,
                            "cantidadVendida": cantidad,
                            "precio": precio,
                        })

                        encontrado = True
                        break

                if not encontrado:
                    print("Lo sentimos, no tenemos ese producto.")

                add_more = input("¿Desea agregar otro producto? (si/no): ")
                if add_more.lower() != 'si':
                    break

        if opc == 2:

            for i in menu[0]["plato_fuerte"]:
                print("Nombre:", i["nombre"], "----- ""Precio(COP): ", i["precio"])
            print("")

        if opc == 3:

            for i in menu[0]["bebida"]:
                print("Nombre:", i["nombre"], "----- ""Precio(COP): ", i["precio"])
            print("")

    elif opcion == 5:
        break


