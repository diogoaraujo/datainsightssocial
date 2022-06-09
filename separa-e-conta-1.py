import pandas as pd
from pandas import *
import json
import re

xls = ExcelFile('22-06-01 eng-words-change-1800-2019code-AS-FINAL.xlsx')
df = xls.parse(xls.sheet_names[0])
#print(df[['Function system', 'word']])

xls2 = pd.read_excel(xls, index_col=None, header=None)
#print(xls2)

Function_system = df['Function system'].tolist()
Function_system = list(dict.fromkeys(Function_system))

# print(Function_system)
categorias_0 = json.dumps(Function_system)
categorias_1 = re.sub('"','',categorias_0)
categorias = categorias_1.replace('[', '').replace(']', '')
print(categorias)
#print(type(categorias_1))



#save json to file
with open('categorias.json', 'w') as jsonfile:
    json.dump(categorias, jsonfile)

contando = df.groupby(['Function system'])['word'].count()

# print(contando)

