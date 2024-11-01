#%%
import pandas as pd
data=[['sun',320.9,100],['mouse',150.3,50],['knife',1.5,200]]
columns=['名称','单价','数量']
df=pd.DataFrame(data=data,columns=columns)
print(df)
#%%
print(df.describe())
#%%
print(df.count())
#%%
print(df.sum())
#%%
print(df.max())
#%%
print(df.min())

#%%
