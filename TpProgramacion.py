#Objeto para representar el producto, con su codigo, nombre, precio etc.
class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
#Metodo para definir como se muestra en pantalla
    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - ${self.precio} ({self.stock} unidades)"

#Estructura de como seran los nodos
class Nodo:
    def __init__(self, producto):
        self.producto = producto
        self.izq = None
        self.der = None


class ArbolStock:
    def __init__(self):
        self.raiz = None
#Metodo para crear un producto nuevo en el arbol
    def insertar(self, producto):
        if self.raiz is None:
            self.raiz = Nodo(producto)
        else:
            self._insertar(self.raiz, producto)
# Metodo para definir el orden al agregar un producto
    def _insertar(self, nodo, producto):
        if producto.codigo < nodo.producto.codigo:
            if nodo.izq:
                self._insertar(nodo.izq, producto)
            else:
                nodo.izq = Nodo(producto)
        else:
            if nodo.der:
                self._insertar(nodo.der, producto)
            else:
                nodo.der = Nodo(producto)
#Metodo para buscar un producto segun su codigo
    def buscar(self, codigo):
        return self._buscar(self.raiz, codigo)

    def _buscar(self, nodo, codigo):
        if nodo is None:
            return None
        if nodo.producto.codigo == codigo:
            return nodo.producto
        elif codigo < nodo.producto.codigo:
            return self._buscar(nodo.izq, codigo)
        else:
            return self._buscar(nodo.der, codigo)
#Metodo para listar los productos
    def listar_productos(self):
        lista = []
        self._inorden(self.raiz, lista)
        return lista
    def _inorden(self, nodo, lista):
        if nodo:
            self._inorden(nodo.izq, lista)
            lista.append(nodo.producto)
            self._inorden(nodo.der, lista)

#Ejemplo de uso, para agregar productos
inventario = ArbolStock()

inventario.insertar(Producto(105, "Teclado", 4500, 12))
inventario.insertar(Producto(101, "Mouse", 2300, 25))
inventario.insertar(Producto(110, "Monitor", 75000, 5))
inventario.insertar(Producto(103, "Notebook", 250000, 3))

#Codigo para darle funcionalidad al arbol
valor = True
while valor: #Bucle para generar interacción con el usuario
    decision = int(input("Ingrese 1 para consultar el stock de un producto.\n"
                        "Ingrese 2 para agregar un producto.\n"
                        "Ingrese 3 para mostrar la lista de todos los productos.\n"
                        "Ingrese 0 para terminar el programa: "))
    if decision == 1:
        codigo_buscar = int(input("Ingrese el codigo del producto: "))
        resultado = inventario.buscar(codigo_buscar)
        print(f"\n Búsqueda del producto con código {codigo_buscar}:")
        print(resultado if resultado else "Producto no encontrado\n")
        print("")#Print vacio solo para una vision mas limpia cuando se imprime el resultado
    elif decision == 2:
        codigo = int(input("Ingrese el codigo del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        inventario.insertar(Producto(codigo, nombre, precio, stock))
        print(f"Producto {nombre} agregado.\n")
    elif decision == 3:
        print("\n  Productos ordenados por código:")
        for prod in inventario.listar_productos():
            print(prod)
        print("")
    else:
        print("Programa finalizado.")
        valor = False 
