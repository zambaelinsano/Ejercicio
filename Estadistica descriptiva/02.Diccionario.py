import pandas as pd
#crear una funcion que se encargue de recibir un diccionario de las notas de los estudiantes de analisis de datos que van a reprobar y obtener su min, max, media y desviacion estandar

def estadistica_notas(notas):
    notas= pd.Series(notas)
    estadistica= pd.Series([notas.min(), notas.max(), notas.mean(),notas.std()], index= ['Min', 'Max', 'Media', 'Desviacion Estandar'])
    return estadistica
notas= {'Juan':9, 'Juanita':5.9, 'pepe':8.2, 'pedro':6.9, 'alberto':4.5 }

def aprobados(notas):
    notas=pd.Series(notas)
    return notas[notas>=6].sort_values(ascending=False)

print (aprobados(notas))
print(estadistica_notas(notas))