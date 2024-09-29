import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Datasets/Chemistry.csv")
print(df.head())
#x=df.head().iloc[:,1]
#y=df.head().iloc[:,2]

print("Missing values in each column:")
print(df.isnull().sum())


#plt.bar(x,y)
#plt.show()

print("statistics:")
print(df.describe())


scores = df.groupby('Name')['Score'].mean().reset_index()
print(scores)


plt.figure(figsize=(10,6))



