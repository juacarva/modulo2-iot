""" Considerando el archivo “campeonato_C5.py” con el siguiente diccionario
realice las siguientes funciones:

Escriba la función posiciones(resultados) que reciba como parámetro el
diccionario de resultados, y retorne una lista con los equipos ordenados por
puntaje de mayor a menor. Los equipos que tienen el mismo puntaje deben ser
ordenados por diferencia de goles de mayor a menor. Si tienen los mismos
puntos y la misma diferencia de goles, deben ser ordenados por los goles
anotados.
>>> posiciones(resultados)
['Espana', 'Chile', 'Suiza', 'Honduras'] """

resultados = {
('Honduras', 'Chile'): (0, 1),
('Espana', 'Suiza'): (0, 1),
('Suiza', 'Chile'): (0, 1),
('Espana', 'Honduras'): (3, 0),
('Suiza', 'Honduras'): (0, 0),
('Espana', 'Chile'): (2, 1)
}

def obtener_lista_equipos(resultados):
    lista = []
    for equipo1, equipo2 in resultados:
        if equipo1 not in lista:
            lista.append(equipo1)
        if equipo2 not in lista:
            lista.append(equipo2)
    return lista

def calcular_puntos(equipo, resultados):
    puntos = []
    for partido, resultado in resultados.items():
        if equipo in partido:
            indice_equipo = partido.index(equipo)
            indice_otro = abs(1 - indice_equipo)
            if resultado[indice_equipo] > resultado[indice_otro]:
                puntos.append(3)
            elif resultado[indice_equipo] == resultado[indice_otro]:
                puntos.append(1)
            else:
                puntos.append(0)
    return sum(puntos)

def calcular_diferencia_de_goles(equipo, resultados):
    dif_partido = []
    for partido, resultado in resultados.items():
        if equipo in partido:
            indice_equipo = partido.index(equipo)
            indice_otro = abs(1 - indice_equipo)
            dif_partido.append(resultado[indice_equipo] - resultado[indice_otro])
    return sum(dif_partido)

def goles_anotados(equipo, resultados):
    goles = []
    for partido, resultado in resultados.items():
        if equipo in partido:
            indice_equipo = partido.index(equipo)
            goles.append(resultado[indice_equipo])
    return sum(goles)

def posiciones(resultados):
    estadisticas = []
    posiciones = []
    equipos = obtener_lista_equipos(resultados)
    for equipo in equipos:
        estadisticas.append((calcular_puntos(equipo, resultados), calcular_diferencia_de_goles(equipo, resultados), goles_anotados(equipo, resultados), equipo))
    estadisticas.sort(reverse=True)
    for res in estadisticas:
        posiciones.append(res[-1])
    return posiciones

print(posiciones(resultados))