import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('./Estadistica descriptiva/housing.csv')

#obtener la media de la columna del total de cuartos
medaicuartos=df[["longitude", "latitude","housing_median_age", "total_rooms","total_bedrooms", "population", "households", "median_income", "median_house_value"]].mean()
#OBTENER LA MEDIANA
medianapopularidad=df[["longitude", "latitude","housing_median_age", "total_rooms","total_bedrooms", "population", "households", "median_income", "median_house_value"]].median()

moda=df[["longitude", "latitude","housing_median_age", "total_rooms","total_bedrooms", "population", "households", "median_income", "median_house_value"]].mode()

rango=df[["longitude", "latitude","housing_median_age", "total_rooms","total_bedrooms", "population", "households", "median_income", "median_house_value"]].max()-df[["longitude", "latitude","housing_median_age", "total_rooms","total_bedrooms", "population", "households", "median_income", "median_house_value"]].min()


print("Media", medaicuartos)
print("mediana: ", medianapopularidad)
print('La moda es:\n' , moda)
print('el rango es:' , rango)
