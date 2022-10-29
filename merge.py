print("Merge Excel Files")
from doctest import  master
import os
import pandas as pd
master_df=pd.DataFrame()
for file in os.listdir(os.getcwd()):
    if file.endswith(".xlsx"):
        master_df=master_df.append(pd.read_excel(file))

master_df.to_excel('Merged Excel file.xlsx',index=False)

