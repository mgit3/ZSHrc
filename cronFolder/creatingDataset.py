from tabulate import tabulate
import pandas as pd 


folderName = 'dataset_speedtest'
file = folderName + '/temp.csv'

columns = 'Server ID,Sponsor,Server Name,Timestamp,Distance,Ping,Download,Upload,Share,IP Address'
lst_columns = columns.split(',')

csvFile = pd.read_csv(file, names=lst_columns)
csvFile = csvFile[lst_columns]
# show = tabulate(csvFile, headers='keys')
excelFile = folderName + '/speedTest.xlsx'
csvFile.to_excel(excelFile)


