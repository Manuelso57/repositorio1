nombresProductos=[]
stocksProductos=[]
preciosProductos=[]

opcion="0"

"""
Agregar producto
Buscar producto
Actualizar cantidad/precio
Mostrar inventario completo
Eliminar producto
Salir
"""

while opcion!="6":
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion=input("Ingrese la opción que desea(1-6): ")

    def solicitarProducto():
        nombre=input("Ingrese el nombre del producto: ")
        try:
            stock=int(input("Ingrese el stock del producto: "))
            precio=int(input("Ingrese el precio del producto: "))
            
            if stock<0 or precio <0:
                raise ValueError
                
            else:
                producto=[nombre,precio,stock]
                return producto

        except ValueError:
            print("Debe ingresar valores enteros positivos")
    
    def guardarProducto(nombre,precio,stock):
        if nombre not in nombresProductos:
            nombresProductos.append(nombre)
            preciosProductos.append(precio)
            stocksProductos.append(stock)
            print("Se guardado correctamente el producto")

    def buscarProducto(nombre):
        if nombre in nombresProductos:
            indice= nombresProductos.index(nombre)
            nombre=nombresProductos[indice]
            precio=preciosProductos[indice]
            stock=stocksProductos[indice]
            print("-"*60)
            print(f"Nombre: {nombre} \t Precio: ${precio} \t Stock: {stock} unidades")
            print("-"*60)
            #return [nombre,precio,stock]
            
        else:
            print("No existe un producto con ese nombre")
    
    match opcion:

        case "1":
            nuevoProducto=solicitarProducto()
            if nuevoProducto!= None:
                guardarProducto(nuevoProducto[0],nuevoProducto[1],nuevoProducto[2])
        case "2":
            nombreProducto=input("Ingrese el nombre del producto a buscar: ")
            buscarProducto(nombreProducto)

