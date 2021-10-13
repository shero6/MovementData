# Import pandas
import pandas as pd
import numpy as np
import os
import glob

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 10000)

df = pd.read_csv("/Users/dermotsheridan/Downloads/UCD/Project /dsa_project/DASDataset/a01/p1/s01.txt", sep=",", header=None)
print(df.head())
print(df.shape)

#4 Open multiple txt file and store as dataframe- This worked!!

#Define relative path to folder containing the text files
files_folder = r'/Users/dermotsheridan/Downloads/UCD/Project /dsa_project/DASDataset/a12/p1/'
files = []
# Create dataframe list by using a list comprehension
files = [pd.read_csv(file, delimiter=',', header= None) for file in glob.glob(os.path.join(files_folder,"*.txt"))]
# Concatenate dataframe list
df_4 = pd.concat(files)
print(df_4.head())
print(df_4.shape)

df_4.columns = ['T_xacc','T_yacc','T_zacc','T_xgyro','T_ygyro','T_zgyro','T_xmag','T_ymag','T_zmag',
                    'RA_xacc','RA_yacc','RA_zacc','RA_xgyro','RA_ygyro','RA_zgyro','RA_xmag','RA_ymag','RA_zmag',
                   'LA_xacc','LA_yacc','LA_zacc','LA_xgyro','LA_ygyro','LA_zgyro','LA_xmag','LA_ymag','LA_zmag',
                   'RL_xacc','RL_yacc','RL_zacc','RL_xgyro','RL_ygyro','RL_zgyro','RL_xmag','RL_ymag','RL_zmag'
                   'LL_xacc','LL_yacc','LL_zacc','LL_xgyro','LL_ygyro','LL_zgyro' ,'LL_xmag','LL_ymag','LL_zmag']