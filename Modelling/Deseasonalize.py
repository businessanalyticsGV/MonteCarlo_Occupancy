##############################################
########### DESEASONILIZING FRAME ############
##############################################

### 0.- LOADING EXTRACTION
import pandas as pd
import numpy as np
import os
pd.set_option('display.max_columns',500)

os.chdir('../ETL')
file = [f for f in os.listdir() if f[-4:] == '.csv'][0]
df = pd.read_csv(file)
df['FirstNight'] = pd.to_datetime(df['FirstNight'])

##################################################
############## PIVOT #############################
##################################################
# temp = 'IN'
df = df[(df['Area'] == 'Nuevo Vallarta') & (df['SiteGroup'] == 'The Grand Mayan') & \
        (df['Roomtype_Orig'] == 'Grand Mayan Master Room') & (df['Mix_NA_IN'] == 'IN') &\
        (df['FirstNight']>='01/01/2017') & (df['FirstNight']<='31/12/2017')]

# temp = ['Season Int' if temp == 'IN' else 'Temp Nal' for temp in list(df['Mix_NA_IN'])[0]]
# print(temp)
#################################################
##################################################
##################################################

df = df[['FirstNight','Nights','Semana_Myn','Season Int','Reservations']]

#### I.- Savg(t)

# 
df_card = df.groupby(['Season Int'], as_index = False)[['FirstNight']].count()
df_card.rename(columns ={'FirstNight':'Card'}, inplace =True)
print(df_card)
exit()
df = df.merge(df_card,how='left', on = ['Season Int'])

print(df.shape)
print(df.head())
print(min(df['FirstNight']))
print(max(df['FirstNight']))






