#%%
import pandas as pd
from tabulate import tabulate
from sqlalchemy import create_engine
from sqlalchemy import MetaData 
from sqlalchemy import Table

# reading the main dataset with pandas
tableName ='speedtest' 
engine = create_engine("sqlite:///dataset_speedtest/main.db")
query = "select * from speedtest"
# Load entire weather table by table name
df = pd.read_sql(query,engine)

print(df)
print(tabulate(df, headers="keys", tablefmt="grid"))
