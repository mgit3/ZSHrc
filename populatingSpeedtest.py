#%%
from tabulate import tabulate
import pandas as pd
from datetime import datetime
import csv


with open('dataset_speedtest/csvHeader.csv', 'r') as f:
    headerCSV = f.read()

headerCSV = headerCSV.split(",")

def clean(s):
    s = s.replace(' ','_')
    s = s.replace('\n','')
    return s

lstHeader = [clean(x) for x in headerCSV if x != '']

#reading the new file with pandas
tempCSV = 'dataset_speedtest/temp.csv'
df = pd.read_csv(tempCSV,header=None, names=lstHeader)

df['Download'] = df['Download'].astype('float')
df['Upload'] = df['Upload'].astype('float')
df['Timestamp'] = datetime.now()

#change the scale on of the value to be more readable
# Build an insert statement to insert a record into the data table: insert_stmt
df['Download'] = df['Download'] / (100**3)
df['Upload'] = df['Upload'] / (100**3)


#%%
from sqlalchemy import create_engine
from sqlalchemy import MetaData 
from sqlalchemy import Table
from sqlalchemy import insert

# reading the main dataset with pandas
tableName ='speedtest' 
engine = create_engine("sqlite:///dataset_speedtest/main.db")
metadata = MetaData()
# Reflect the census table from the engine: census
myTable = Table(tableName, metadata, autoload=True, autoload_with=engine)

# Print the column names
#%%
tb_cl = myTable.columns.keys()
df = df[tb_cl]
df

lst = []
for x in df.columns:
    lst.append(df[x][0])

#%%

# Print full metadata of census
print(repr(myTable))
# Build an insert statement to insert a record into the data table: insert_stmt
insert_stmt = insert(myTable).values(lst)

result_proxy = engine.execute(insert_stmt)# %%
