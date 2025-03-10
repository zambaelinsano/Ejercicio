#serie con los datos de las ventas indexadas por los años

import pandas as pd

inicio=int(intput('Introduce el año inicial de venrtas: '))
fin= int(intput('Introduce el año final de ventas:'))
ventas={}
for i in range(inicio, fin+1):
    ventas[i]=float(input('Introduce las ventas del año: ' + str(i) + ': '))
    
ventas= pd.Series(ventas)