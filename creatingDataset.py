import pandas as pd
from sqlalchemy import create_engine,MetaData,  Table, Column, Integer, String, DateTime

#this program create a database with the 'csvHeader' file.

#csv file with the column names
path = 'dataset_speedtest/csvHeader.csv'

#reading the csv and transforming into a data frame, ignoring the last column with the iloc.
df = pd.read_csv(path).iloc[:,1:]

#creating a function to clean the string on the column names
def clean(s):
    s = s.replace(' ','_')
    s = s.replace('\n','')
    return s

#using a List comprehension to apply the function to clean the column names and ignore the columns with the IP address
lst = [clean(x) for x in df.columns if 'IP' not in x]

Server_ID =lst[0]
Sponsor=lst[1]
Server_Name=lst[2]
Timestamp=lst[3]
Distance=lst[4]
Ping=lst[5]
Download=lst[6]
Upload=lst[7]
Share=lst[8]

tableName ='speedtest' 
engine = create_engine("sqlite:///dataset_speedtest/main.db")
connection = engine.connect()

stmt = f"""CREATE TABLE speedtest(
                {Sponsor}  VARCHAR(50),
                {Server_Name}  VARCHAR(50),
                {Timestamp} DATETIME,
                {Distance} DECIMAL,
                {Ping} TEXT,
                {Download} DECIMAL,
                {Upload} DECIMAL
                );"""

#executing the command above
results = connection.execute(stmt)             
