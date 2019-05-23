#######I.-
import pandas as pd
import numpy as np

df=pd.read_csv('../ETL/Reservations_Work.csv')
##print(df.shape)
##print(df.head())

area='Nuevo Vallarta'
sitegroup='The Grand Mayan'
roomtype='Grand Mayan Suite'
mix='IN'

df=df[(df['Area']==area) & \
(df['SiteGroup']==sitegroup) & \
(df['RoomType']==roomtype) &\
(df['Mix_NA_IN']==mix)]     

print(df.shape)
print(df.head()) 

ls_cols=[]