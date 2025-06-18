lista_productos=[]
#producto={"nombre":nombre,"precio":precio,"cantidad":stock,"codigo":codigo}
#el tiene que tener 3 validaciones:
#el codigo debe tener un minimo de 5 caracteres;
#el codigo debe tener al menos 2 mayusculas
#el codigo debe tener al menos 1 numero

opcion="0"

"""
Agregar producto
Buscar producto
Actualizar cantidad/precio
Mostrar inventario completo
Eliminar producto
Salir
"""

def validarCodigo(codigo):
    codigo="Diego"
    contador_mayusculas=0
    contador_numeros=0
    for l in str(codigo):
        if l.isupper():
            contador_mayusculas+=1
        if l.isnumeric():
            contador_numeros+=1
    if contador_mayusculas<2:
        print("el codigo debe tener al menos 2 mayusculas")
        return False
    elif contador_numeros==0:
        print("el codigo debe tener al menos un numero")
        return False
    elif len(codigo) <5:
        print("el codigo debe tener al menos 5 caracteres")
        return False
    else:
        return True
     

def solicitarProducto():
    nombre=input("Ingrese el nombre del producto: ")
    while True:
        codigo=input("ingrese el codigo para el producto")
        if validarCodigo(codigo)==True:
            print("codigo correcto!.")
            break
        else:
            print("el codigo es incorrecto. debe volver a ingresarlo")
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


def guardarProducto(nombre,precio,stock,codigo):
    #producto={"nombre":nombre,"precio":precio,"cantidad":stock,"codigo":codigo}
    productoBuscado=buscarProducto(codigo)
    if productoBuscado!=None:
            print("ese producto ya fue registrado")
            return False
    producto={"nombre":nombre,"precio":precio,"cantidad":stock,"codigo":codigo}
    lista_productos.append(producto)
    return True


def buscarProducto(codigo):
    for producto in lista_productos:
        if codigo==producto["codigo"]:
            return producto

    return None


def mostrarProducto(codigo):
    productoBuscado=buscarProducto(codigo)
    if productoBuscado!=None:
        print("-"*60)
        print(f"Cod: {productoBuscado["codigo"]} \tNombre {productoBuscado["nombre"]} \t Precio: ${productoBuscado["precio"]}")

match opcion:

    case "1":
        nuevoProducto=solicitarProducto()
        if nuevoProducto!= None:
            guardarProducto(nuevoProducto[0],nuevoProducto[1],nuevoProducto[2])
    case "2":
        nombreProducto=input("Ingrese el nombre del producto a buscar: ")
        buscarProducto(nombreProducto)


while opcion!="6":
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion=input("Ingrese la opción que desea(1-6): ")