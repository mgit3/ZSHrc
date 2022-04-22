from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine,MetaData,  Table, Column, Integer, String, DateTime

path = 'dataset_speedtest/csvHeader.csv'

df = pd.read_csv(path).iloc[:,1:]

def clean(s):
    s = s.replace(' ','_')
    s = s.replace('\n','')
    return s

lst = [clean(x) for x in df.columns]

Server_ID =lst[0]
Sponsor=lst[1]
Server_Name=lst[2]
Timestamp=lst[3]
Distance=lst[4]
Ping=lst[5]
Download=lst[6]
Upload=lst[7]
Share=lst[8]
IP_Adress=lst[9]

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
                {Upload} DECIMAL,
                {IP_Adress} VARCHAR(13));"""

results = connection.execute(stmt)

                # {Share} TEXT,
                # {Server_ID} INTEGER,