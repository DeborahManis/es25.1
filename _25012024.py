
import numpy as np
import pandas as pd
wine = pd.read_csv (r'C:\Users\Debor\Downloads\wine.csv', sep = "," ,encoding="iso-8859-15", header =0)

print(wine.describe())
 # print(wine.count())
media= wine.mean
print(media)
mediana= wine.median(axis=1, numeric_only=True)
print(mediana)
moda= wine.mode(axis=0, numeric_only=True)
print(moda)

#colonna= {'sommario':["Min",  "Max", "Mean","SD","ClassCorrelation"]}
iris= pd.read_csv (r'C:\Users\Debor\Downloads\iris\iris.data')
#COLUMN aggiungiamo colonna con i nomi(?)
print(iris.head(5))
