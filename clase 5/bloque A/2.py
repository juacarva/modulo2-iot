""" Los resultados de un campeonato de fútbol se almacenan en un diccionario. Las
llaves son los partidos, y los valores los resultados. Revise el archivo
“campeonato_C5.py” """



resultados = {
('Honduras', 'Chile'): (0, 1),
('Espana', 'Suiza'): (0, 1),
('Suiza', 'Chile'): (0, 1),
('Espana', 'Honduras'): (3, 0),
('Suiza', 'Honduras'): (0, 0),
('Espana', 'Chile'): (2, 1)
}

""" Escriba las siguientes funciones!

>>> obtener_lista_equipos(resultados)
['Honduras', 'Suiza', 'Espana', 'Chile']

>>> calcular_puntos('Chile', resultados)
6

>>> calcular_puntos('Suiza', resultados)
4 """

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


print(obtener_lista_equipos(resultados))
print(calcular_puntos('Chile', resultados))
print(calcular_puntos('Suiza', resultados))
print(calcular_puntos('Espana', resultados))
print(calcular_puntos('Honduras', resultados))