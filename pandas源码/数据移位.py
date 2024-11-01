#%%
import pandas as pd 
data=[7532,3937,9447,8765,4564]
index=[1,2,3,4,5]
df=pd.DataFrame(data=data,index=index,columns=['OPPO'])
print(df)
df['销量差']=df['OPPO']-df['OPPO'].shift()
print(df)

#print(df['OPPO'].shift())
#%%
