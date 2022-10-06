""" Escriba las funciones necesarias para que el programa del archivo
“artistas_C5.py” funcione """

artistas = {
    # nombre: codigo, origen, duracion en minutos de la presentacion)
    'Marco Antonio Solis': (1, 'Estados Unidos', 74),
    'Daddy Yankee': (2, 'Puerto Rico', 70),
    'Myriam Hernandez': (3, 'Chile', 40),
    'Los Charros de Lumaco': (4, 'Chile', 25),
    'Metallica': (5, 'Estados Unidos', 45),
    'U2': (6, 'Irlanda', 80),
    'Justin Bieber': (7, 'Canada', 5),
}

artistas_por_dia = {
    # dia, orden de las presentaciones
    "Lunes": (1, 4, 3, 6, 2, 5),
    "Martes": (2, 5, 1),
    "Miercoles": (3, 6, 2, 4),
    "Jueves": (2, 5),
}

def cantidad_de_artistas(dia):
    return len(artistas_por_dia[dia])

def nombre_primer_artista(dia):
    codigo_artista = artistas_por_dia[dia][0]
    for c,d in artistas.items():
        if d[0] == codigo_artista:
            return (c)

def pais_origen_ultimo(dia):
    codigo_artista = artistas_por_dia[dia][-1]
    for c,d in artistas.items():
        if d[0] == codigo_artista:
            return d[1]

def tiempo_total(dia):
    tiempo = 0
    for artista in artistas_por_dia[dia]:
        for valores in artistas.values():
            if artista == valores[0]:
                tiempo += valores[2]
    return tiempo




dia = input('Ingrese dia: ')
print('Ese dia se presentaran', cantidad_de_artistas(dia), 'artistas')
print('El primer artista del dia sera', nombre_primer_artista(dia))
print('El ultimo artista del dia viene de', pais_origen_ultimo(dia))
print('Ese dia el concierto completo durara', tiempo_total(dia),'minutos')