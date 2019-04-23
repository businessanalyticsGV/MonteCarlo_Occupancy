#### I.- EXTRACCIÓN
import pandas as pd
import numpy as np
pd.set_option('display.max_columns',500)

df = pd.read_csv('../ETL/Reservations_Work.csv')

###### DEJARLO COMO EL LAYOUT #################
area = 'Nuevo Vallarta'
sitegroup = 'The Grand Mayan'
roomtype = 'Grand Mayan Suite'|
mix = 'IN'
season = ['Season Int' if mix == 'IN' else 'Temp Nal' for i in range(1)][0]

df = df[(df['Area'] == area) & \
    (df['SiteGroup'] == sitegroup) & \
    (df['RoomType'] == roomtype) & \
    (df['Mix_NA_IN'] == mix)].reset_index(drop = True)

df['FirstNight'] = pd.to_datetime(df['FirstNight'],format = '%d/%m/%Y')
df['Year'] = [d.year for d in df['FirstNight']]
df['Weekday'] = [d.isoweekday() - 4 if d.isoweekday() >= 5 else \
                 d.isoweekday() + 3 for d in df['FirstNight']]

ls_cols = ['FirstNight',season,'Reservations',
           'Semana_Myn','Weekday','Year']
df = df[ls_cols]
print(df.shape)
print(df.head())

################ ESTO SE BORRA #########################


