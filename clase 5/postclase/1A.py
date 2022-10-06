""" Considerando el archivo “campeonato_C5.py” con el siguiente diccionario
realice las siguientes funciones: """


resultados = {
('Honduras', 'Chile'): (0, 1),
('Espana', 'Suiza'): (0, 1),
('Suiza', 'Chile'): (0, 1),
('Espana', 'Honduras'): (3, 0),
('Suiza', 'Honduras'): (0, 0),
('Espana', 'Chile'): (2, 1)
}

""" La diferencia de goles de un equipo es el total de goles que anotó menos el total de
goles que recibió.
Escriba la función calcular_diferencia_de_goles(equipo, resultados) que
entregue la diferencia de goles de un equipo.
>>> calcular_diferencia_de_goles('Chile', resultados)
1
>>> calcular_diferencia_de_goles('Honduras', resultados)
-4 """

def calcular_diferencia_de_goles(equipo, resultados):
    dif_partido = []
    for partido, resultado in resultados.items():
        if equipo in partido:
            indice_equipo = partido.index(equipo)
            indice_otro = abs(1 - indice_equipo)
            dif_partido.append(resultado[indice_equipo] - resultado[indice_otro])
    return sum(dif_partido)
    
print(calcular_diferencia_de_goles('Chile', resultados))
print(calcular_diferencia_de_goles('Honduras', resultados))