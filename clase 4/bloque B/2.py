""" Un supermercado utiliza las siguientes estructuras de datos para manejar su
inventario. Las estructuras se encuentran en el archivo supermercado.py.
Basado en esas estructuras (listas de tuplas), desarrolle las siguientes
funciones:
>>> producto_mas_caro(productos)
‘Vuvuzela’
>>> valor_total_bodega(productos)
1900570
>>> ingreso_total_por_ventas(itemes, productos)
13944 """


productos = [
    #(id_producto, nombre, precio, cantidad_bodega)
    (41419, 'Fideos', 450, 210),
    (70717, 'Cuaderno', 900, 119),
    (78714, 'Jabon', 730, 708),
    (30877, 'Desodorante', 2190, 79),
    (47470, 'Yogur', 99, 832),
    (50809, 'Palta', 500, 55),
    (75466, 'Galletas', 235, 0),
    (33692, 'Bebida', 700, 20),
    (89148, 'Arroz', 900, 121),
    (66194, 'Lapiz', 120, 900),
    (15982, 'Vuvuzela', 12990, 40),
    (41235, 'Chocolate', 3099, 48),
]

itemes = [
    #(num_boleta, id_producto, cantidad)
    (1, 89148, 3),
    (2, 50809, 4),
    (2, 33692, 2),
    (2, 47470, 6),
    (3, 30877, 1),
    (4, 89148, 1),
    (4, 75466, 2),
    (5, 89148, 2),
    (5, 47470, 10),
    (6, 41419, 2),
]

def producto_mas_caro(productos):
    lista = []
    for id, nombre, precio, cantidad in productos:
        lista.append((precio, nombre))
    lista.sort()
    return lista[-1][1]

print(producto_mas_caro(productos))


def valor_total_bodega(prodcutos):
    lista = []
    for id, nombre, precio, cantidad in productos:
        lista.append(precio*cantidad)
    return sum(lista)

print(valor_total_bodega(productos))

def ingreso_total_por_ventas(itemes, productos):
    lista = []
    for _, id_1, cantidad in itemes:
        for id_2, _, precio, _ in productos:
            if id_1 == id_2:
                lista.append(cantidad*precio)
    return sum(lista)

print(ingreso_total_por_ventas(itemes, productos))