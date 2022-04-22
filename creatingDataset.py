#%%
import pandas as pd 

path = 'dataset_speedtest/csvHeader.csv'

df = pd.read_csv(path).iloc[:,1:]

def removeSpace(x):
    return x.replace(' ','')

lst = [removeSpace(x) for x in df.columns]
df
#%%
from sqlalchemy import *

tableName ='speedtest' 
engine = create_engine("sqlite:///dataset_speedtest/main.db")
metadata = MetaData()

speedtest = Table(tableName,metadata,
                Column(lst[0], VARCHAR(5)),
                Column(lst[2], VARCHAR(50)),
                Column(lst[3], VARCHAR(30)),
                Column(lst[4], DATETIME()),
                Column(lst[5], DECIMAL()),
                Column(lst[6], DECIMAL()),
                Column(lst[7], TEXT()),
                Column(lst[8], DECIMAL()),
                Column(lst[9], VARCHAR(13)),
    )

metadata.create_all(engine)
engine.table_names()
# %%
connection = engine.connect()
print(engine.table_names())
    # %%
