from email import header
from tabulate import tabulate
import pandas as pd 


file = 'csv_folder/temp.csv'
columns = 'Server ID,Sponsor,Server Name,Timestamp,Distance,Ping,Download,Upload,Share,IP Address'
lst_columns = columns.split(',')
csvFile = pd.read_csv(file, names=lst_columns)
show = tabulate(csvFile, headers='keys')

csvFile.to_excel('speedTest.xlsx')

print(show)

