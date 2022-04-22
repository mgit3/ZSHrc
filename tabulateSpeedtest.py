import pandas as pd
from tabulate import tabulate


df=pd.read_csv('dataset_speedtest/speedTest.csv')

lst_columns = 'Server ID,Sponsor,Server Name,Timestamp,Distance,Ping,Download,Upload,Share,IP Address'.split(",") 

df = df[lst_columns]
print(tabulate(df, headers = lst_columns, tablefmt="grid"))


