import time
start = time.time()
#############################################################################
#############################################################################
########### EXTRACTION IN CASE THE SERVER'S NOT AVAILABLE ###################
#############################################################################
#############################################################################

### I.- EXTRACTION
import pandas as pd
import numpy as np

path = 'C:/Users/alexisalvarez/OneDrive - Grupo Vidanta/UPDATE/Work/00. QVDs/Extraction/DBs/'

ls_cols = ['FirstNight','Area','SiteGroup','Roomtype','Semana_Myn']
ls_targ = '%ReservationNumber'
ls_cols = ls_cols + [ls_targ]
df = pd.read_csv(path+'Reservations.csv')
df = df[(df['Año']>=2015) & (df['ReservationStatus']!='Canceled') & (df['Deposits']=='No') & (df['NoShow']=='No')]
df = df.groupby([c for c in ls_cols if c != ls_targ], as_index = False)[[ls_targ]].count()
df.rename(columns = {ls_targ:'Reservations'}, inplace = True)
df.to_csv('training.txt', index = False)

print(time.time()-start)





