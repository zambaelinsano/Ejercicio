import pandas as pd
#vamos a hacer un ejemplo de caa¿da archivo y aplicar minimo, maximo, media y desviacion estandar

def cotizacion(fichero):
    df=pd.read_csv(fichero, sep=';', decimal=',', thousands='.', index_col=0)
    return pd.DataFrame([df.min(), df.max(), df.mean(), df.std()], index= ['Minimo', 'Maximo', 'Media', 'Desviacion estandar'])
cotizacion(('./Estadistica descriptiva/cotizacion.csv'))

print('./Estadistica descriptiva/cotizacion.csv')