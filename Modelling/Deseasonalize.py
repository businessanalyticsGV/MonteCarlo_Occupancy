##############################################
########### DESEASONILIZING FRAME ############
##############################################

### 0.- LOADING EXTRACTION
import pandas as pd
import numpy as np
import os

os.chdir('../ETL')
file = [f for f in os.listdir() if f[-4:] == '.csv'][0]
df = pd.read_csv(file)

##################################################
############## PIVOT #############################
##################################################
df = df[(df['Area'] == 'Nuevo Vallarta') & (df['SiteGroup'] == 'The Grand Mayan') & \
        (df['Roomtype_Orig'] == 'Grand Mayan Master Room')]

df['FirstNight'] = pd.to_datetime(df['FirstNight'])

print(df.shape)
print(df.head())
print(min(df['FirstNight']))
print(max(df['FirstNight']))


# ls_toIter = ['Area','SiteGroup','Roomtype_Orig']

# ls = [(it,list(np.unique(df[it]))) for it in ls_toIter]
# for i in ls:
#     print(i)



