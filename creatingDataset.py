
#%%
import pandas as pd 
#%%
lst_columns = 'Server ID,Sponsor,Server Name,Timestamp,Distance,Ping,Download,Upload,Share,IP Address'.split(",")
print(lst_columns)
#%%
df = pd.DataFrame( columns=lst_columns)

df.to_csv('dataset_speedtest/speedTest.csv')
#%%