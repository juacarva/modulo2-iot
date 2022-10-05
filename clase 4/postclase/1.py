""" Considerando las estructuras del ejercicio anterior (supermercado), desarrolle
las siguientes funciones:
>>> producto_con_mas_ingresos(itemes, productos)
‘Arroz’
>>> cliente_que_mas_pago(itemes, productos, clientes)
‘Victor Gamonal’
>>> ingreso_total_por_ventas(itemes, productos)
13944
>>> total_ventas_del_mes(2010, 10, itemes, productos, ventas)
4160
>>> fecha_ultima_venta_producto(47470, itemes, ventas)
(2010, 10, 13) """

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

clientes = [
    #(rut, nombre)
    ('11652624-7', 'Juan Perez'),
    ('8830268-0', 'Sebastian Casanueva'),
    ('7547896-8', 'Victor Gamonal'),
]

ventas = [
    #(num_boleta, fecha_venta, rut_cliente)
    (1, (2010, 9, 12), '8830268-0'),
    (2, (2010, 9, 19), '11652624-7'),
    (3, (2010, 9, 30), '7547896-8'),
    (4, (2010, 10, 1), '8830268-0'),
    (5, (2010, 10, 13), '7547896-8'),
    (6, (2010, 11, 11), '11652624-7'),
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

def producto_con_mas_ingresos(itemes, productos):
    lista = []
    for boleta, id_1, cantidad in itemes:
        for id_2, producto, precio, cantidad_bodega in productos:
            if id_1 == id_2:
                lista.append((cantidad*precio, producto))
    lista.sort()
    return lista[-1][1]

print(producto_con_mas_ingresos(itemes, productos))

def cliente_que_mas_pago(itemes, productos, clientes, ventas):
    boletas_clientes = []#(nombre,num_boleta)
    total_boleta = []#(numero_boleta, total_boleta)
    totalxcliente = []#(total_pago, nombre)
    for rut, nombre in clientes:
        for num_boleta, fecha_venta, rut_cliente in ventas:
            if rut == rut_cliente:
                boletas_clientes.append((nombre, num_boleta))
    for num_boleta, id, cantidad in itemes:
        for id_producto, nombre, precio, cantidad_bodega in productos:
            if id == id_producto:
                total_boleta.append((num_boleta, cantidad*precio))
    for n_boleta, total in total_boleta:
        for nombre, num_boleta in boletas_clientes:
            if n_boleta == num_boleta:
                totalxcliente.append((total, nombre))
    clientes = []#lista de clientes unicos
    pagoTotalCliente = []#(pagoTotal, cliente)
    for total, nombre in totalxcliente:
        if nombre not in clientes:
            clientes.append(nombre)
    for cliente in clientes:
        suma = 0
        for total, nombre in totalxcliente:
            if cliente == nombre:
                suma = suma + total
        pagoTotalCliente.append((suma, cliente))
    pagoTotalCliente.sort()
    return pagoTotalCliente[-1][1]

            
print(cliente_que_mas_pago(itemes, productos, clientes, ventas))

def ingreso_total_por_ventas(itemes, productos):
    lista = []
    for _, id_1, cantidad in itemes:
        for id_2, _, precio, _ in productos:
            if id_1 == id_2:
                lista.append(cantidad*precio)
    return sum(lista)

print(ingreso_total_por_ventas(itemes, productos))


def total_ventas_del_mes(anio, mes, itemes, productos, ventas):
    ventas_mes = []#(boleta, año, mes)
    for boleta, fecha, rut in ventas:
        if fecha[0] == anio and fecha[1]== mes:
            ventas_mes.append((boleta, anio, mes))
    montos_boletas = []#(boleta, monto)
    for num_boleta, id_prod, cantidad in itemes:
        for id_producto, nombre, precio, cantidad_bodega in productos:
            if id_prod == id_producto:
                montos_boletas.append((num_boleta, cantidad*precio))
    total = 0
    for bol, ano, mes in ventas_mes:
        for boleta, montos in montos_boletas:
            if bol == boleta:
                total += montos
    return total

print(total_ventas_del_mes(2010, 10, itemes, productos, ventas))

def fecha_ultima_venta_producto(id_prod, itemes, ventas):
    boletas_item = []#nro boleta del producto solicitado
    for num_boleta, id_producto, cantidad in itemes:
        if id_producto == id_prod:
            boletas_item.append(num_boleta)
    fechas_venta_prod = []
    for num_boleta, fecha_venta, rut_cliente in ventas:
        if num_boleta in boletas_item:
            fechas_venta_prod.append(fecha_venta)
    fechas_venta_prod.sort(reverse=True)
    return fechas_venta_prod[0]

print(fecha_ultima_venta_producto(47470, itemes, ventas))
    