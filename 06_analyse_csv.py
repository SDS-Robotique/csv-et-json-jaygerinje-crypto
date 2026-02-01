import pandas as pd

dataPropre = pd.read_csv('03_data.csv')

dataOups = pd.read_csv('05_data.csv')

print(dataPropre.info()) 

print(dataOups.info()) 


