import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df=pd.read_csv('./Estadistica descriptiva/housing.csv')



#obtener la media de la columna del total de cuartos
medaicuartos=df[["longitude", "latitude","housing_median_age", "total_rooms","total_bedrooms", "population", "households", "median_income", "median_house_value"]].mean()
#OBTENER LA MEDIANA
medianapopularidad=df[["longitude", "latitude","housing_median_age", "total_rooms","total_bedrooms", "population", "households", "median_income", "median_house_value"]].median()

moda=df[["longitude", "latitude","housing_median_age", "total_rooms","total_bedrooms", "population", "households", "median_income", "median_house_value"]].mode()

rango=df[["longitude", "latitude","housing_median_age", "total_rooms","total_bedrooms", "population", "households", "median_income", "median_house_value"]].max()-df[["longitude", "latitude","housing_median_age", "total_rooms","total_bedrooms", "population", "households", "median_income", "median_house_value"]].min()
varianza = df[["longitude", "latitude", "housing_median_age", "total_rooms", "total_bedrooms", "population", "households","median_income", "median_house_value"]].var()

desviacion = df[["longitude", "latitude", "housing_median_age", "total_rooms", "total_bedrooms", "population", "households", "median_income", "median_house_value"]].std()



print("Desviación estándar:\n", desviacion)
print("Varianza:\n", varianza)
print("Media\n", medaicuartos)
print("mediana: \n", medianapopularidad)
print('La moda es:\n' , moda)
print('el rango es:\n' , rango)

mean_value = df['median_house_value'].mean()
df['population_bins'] = pd.cut(df['population'], bins=20) 
grouped = df.groupby('population_bins')['median_house_value'].mean().reset_index()
plt.figure(figsize=(10, 4))
sns.barplot(x=grouped['population_bins'].astype(str), y=grouped['median_house_value'], color='red' )
plt.xticks(rotation=90)
plt.title('Comparación de median house value y population')
plt.xlabel('Population (agrupada)')
plt.ylabel('Median House Value')
plt.legend()
plt.show()