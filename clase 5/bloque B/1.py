#El diccionario países asocia cada persona con el país que ha visitado.
paises = {
'Juan': {'Chile', 'Argentina'},
'Pedro': {'Francia', 'Suiza', 'Chile'},
'Diego': {'Chile', 'Italia', 'Francia', 'Peru'}
}
#Escriba una función
#cuantos_en_comun (a, b), que indique cuántos países en común han
#visitado la persona a y la persona b.
#>>> cuantos_en_comun (‘Juan’, ‘
#1
#>>> cuantos_en_comun (‘Diego’, ‘
#2
def cuantos_en_comun(persona1, persona2):
    return len(paises[persona1] & paises[persona2])

print(cuantos_en_comun('Juan', 'Diego'))
print(cuantos_en_comun('Diego', 'Pedro')) 