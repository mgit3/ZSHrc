import pandas as pd
from tabulate import tabulate


df=pd.read_csv('dataset_speedtest/speedTest.csv')

lst_columns = 'Server ID,Sponsor,Server Name,Timestamp,Distance,Ping,Download,Upload,Share,IP Address'.split(",") 

df = df[lst_columns]

df['Download'] = df['Download'].astype('float')
df['Upload'] = df['Upload'].astype('float')

#change the scale on of the value to be more readable
df['Download'] = df['Download'] / (100**3)
df['Upload'] = df['Upload'] / (100**3)

print(tabulate(df, headers = lst_columns, tablefmt="grid"))


