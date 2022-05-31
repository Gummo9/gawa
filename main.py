import pandas as pd

oops = pd.read_csv('OceanOPS_animal.csv', header=0)

CMEMS = pd.read_csv('platform_indexCMEMS.csv', sep=';',header=5,low_memory=False)
wmo_CMEMS = CMEMS['wmo_platform_code']

lt = wmo_CMEMS.values.tolist()
# print (lt)
df2 = pd.DataFrame(columns=['COUNTRY','DEPLOYMENT DATE','DEPLOYMENT LAT','DEPLOYMENT LON','LAST LOCATION DATE','MODEL','NAME','NETWORKS','OBSERVING NETWORKS','PROGRAM','REF','SERIAL NUMBER','STATUS','TYPE'])
for i in lt:
   if i in oops['REF'].values:
        arr = (oops.loc[oops['REF'] == i].values)
        list2=[]
        to_append = arr.tolist()
        for o in range(14):
             val = arr[0,o]
             list2.append(val)

        df_length = len(df2)
        df2.loc[df_length] = list2


print (df2['REF'])
df2.to_csv('Test.csv',index=False)

