import regex as re
import unicodedata  
import os
import pandas as pd
import random

#listing the files on the directory
files = os.listdir()


#building a dataframe with information about the files
df = pd.DataFrame(files, columns=['file'])

df.head()

lst_re = [
    (r'_\w_','_'),
    (r'\s|-+', '_'),
    (r'__', '_'),
    (r'\d',''),
    (r'_+\.','.'),
]

def strip_accents(cln):
   cln = str(cln)
   return ''.join(c for c in unicodedata.normalize('NFD', cln)if unicodedata.category(c) != 'Mn')

def regexing(value):
   for string in lst_re:
        value = re.sub(string[0],string[1],value).lower()

   return value
   
lst = []
for x in df:
    for index, _ in enumerate(lst_re):
        x = re.sub(lst_re[index][0], lst_re[index][1], x)
        lst.append(x)

lambs = [
    lambda x:strip_accents(x),
    lambda x:regexing(x),
    lambda x: x[1:] if x[0] == '_' else x,
    lambda x: '_'.join(x.split('_')[-3:]),
]

df['new_name'] = df['file']

for lamb in lambs:
    df['new_name'] = df['new_name'].apply(lamb)

df['new_name'] = df['new_name'].apply(lambda x: str(x).replace('.', f'_{str(random.randint(100,999))}.'))

for i,x in enumerate(df.file):
    os.rename(df.file[i], df.new_name[i])


print(df) 
