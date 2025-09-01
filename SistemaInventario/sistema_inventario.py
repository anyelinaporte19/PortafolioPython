print("*** Sistema de Inventarios ***")

inventario = [
    {'id': 1, 'nombre': "Camisa", 'precio': 25.99, 'cantidad': 50},
    {'id': 2, 'nombre': "Pantalones", 'precio': 39.99, 'cantidad': 30},
    {'id': 3, 'nombre': "Zapatos", 'precio': 49.99, 'cantidad': 20}
]
opcion = 0


def mostrar_inventario():
    for i, productos in enumerate(inventario):
        print(f'Id: {productos.get("id")}, Nombre: {productos.get("nombre")}, Precio: ${productos.get("precio")}, Cantidad: {productos.get("cantidad")}')

def agregar_producto(**kwargs):
     inventario.append(kwargs)

while True:
    print(f'''\n--- Menú ---
    1. Mostrar inventario
    2. Agregar nuevo producto
    3. Buscar producto por Id
    4. Salir''')
    opcion = int(input("Proporciona una opción (1-4): "))

    if opcion ==1:

        print("\nInventario del almacén:")
        mostrar_inventario()
    elif opcion == 2:

        print("\n--- Agregando nuevo producto ---")
        Id = input("Id: ")
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))

        if (Id is not None) and (nombre is not None) and (precio is not None) and (cantidad is not None):
            agregar_producto(id=Id, nombre=nombre, precio=precio, cantidad=cantidad)
            print("\nProducto agregado")
        else:
            print("Lo siento no has agregado ningun producto")

    elif opcion == 3:
        print(" \n--- Buscar producto por Id ---")

        no_producto = int(input("Ingrese el Id a buscar: "))
        encontrado = None
        for producto in inventario:
            if producto['id'] == no_producto:
                encontrado = producto
                break

        if encontrado:
                print(f' \nInformación del producto encontrado: '
                  f'\nId: {encontrado.get("id")}, Nombre: {encontrado.get("nombre")}, '
                  f'Precio: {encontrado.get("precio")}, Cantidad: {encontrado.get("cantidad")}')
        else:
             print("Id no encontrado")
    elif opcion == 4:
        print("\nHasta Pronto!")
        break
    else:
        print("\nOpcion inválida, por favor agregue una opción que sea válida")





