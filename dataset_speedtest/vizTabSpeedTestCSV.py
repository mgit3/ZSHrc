#%%
from tabulate import tabulate
import pandas as pd
#%%

#giving the name of where the dataset is located
file = 'speedTest.csv'
# reading the Dataset with pandas
df = pd.read_csv(file)

#%%

# filtering the columns
df = df [['Sponsor', 'Server Name', 'Timestamp','Distance', 'Ping', 'Download', 'Upload']]



df['Download'] = df['Download'].astype('float')
df['Upload'] = df['Upload'].astype('float')

#change the scale on of the value to be more readable
df['Download'] = df['Download'] / (100**3)
df['Upload'] = df['Upload'] / (100**3)

#%%

# using the tabulate module to show in a cool way the data on the terminal
print(tabulate(df, headers='keys',tablefmt="grid"))
