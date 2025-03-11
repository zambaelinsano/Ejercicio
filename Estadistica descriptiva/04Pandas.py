import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('./Estadistica descriptiva/housing.csv')
#Mostrar las primeras 5 filas
print(df.head())

#las ultimas 5 filas
print(df.tail())
#quiero una fila en especifico
print(df.iloc[7])

print(df["ocean_proximity"])

#obtener la media de la columna del total de cuartos
medaicuartos=df["total_rooms"].mean()

#OBTENER LA MEDIANA
medianapopularidad=df["population"].median()

print("Media de los cuartos:", medaicuartos)
print("mediana de la popularidad: ", medianapopularidad)

std_age=df["housing_median_age"].std()
print('media edad', std_age)

filtrodeloceano=df[df["ocean_proximity"] == "ISLAND"]
print('Filtro de proximidad del oceano', filtrodeloceano)

#Vamos a crear un grafico de dispersion emtre los registros de la proximidad del oceano vs los precion
plt.scatter(df["ocean_proximity"][:10], df["median_house_value"][:10])

#Hay que definir a x y y
plt.xlabel('Proximidad')
plt.ylabel('Precio')

plt.title('Grafico de dispersion de proximidad al oceani vs precio')
plt.show()
