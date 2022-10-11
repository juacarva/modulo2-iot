""" Una consulta médica mantiene un archivo pacientes.csv con los datos
personales de sus pacientes. Cada línea del archivo tiene el rut, nombre y
edad de un paciente, separados por un símbolo ;
Escriba un programa que construya dos nuevos archivos.
- jovenes.csv, con los datos de los pacientes menores de 30 años.
- mayores.csv, con los datos de todos los pacientes mayores de 60 años.  """

archivo = open('pacientes.csv')
jovenes = open('jovenes.csv','w')
mayores = open('mayores.csv','w')

for linea in archivo:
    lista = linea.strip().split(';')
    if int(lista[2])<30:
        jovenes.write(';'.join(lista)+"\n")
    elif int(lista[2])>60:
        mayores.write(';'.join(lista)+"\n")

archivo.close()
jovenes.close()
mayores.close()