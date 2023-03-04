import os
import pandas as pd


master_file = pd.DataFrame()

for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        master_file = master_file.append(pd.read_csv(file))

master_file.to_csv('MasterFile.csv')
