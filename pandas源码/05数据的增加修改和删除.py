#%%
# 数据的增加-按列增加
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
data=[[45,65,100],[56,45,50],[67,67,67]]
index=['张三','李四','王五']
columns=['数学','语文','英语']
df=pd.DataFrame(data=data,index=index,columns=columns)
print(df)

#采用直接赋值的方式
df['政治']=[90,89,100] # 在最后一列增加
print(df)

# 使用loc属性在DataFrame的最后一列增加
df.loc[:,'化学']=[100,30,98]
print(df)

# 在指定的索引位置上插入一列
lst=[100,90,99]
df.insert(1,'历史',lst) # 在索引为1的位置插入一列
print(df)
#%%
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
data=[[45,65,100],[56,45,50],[67,67,67]]
index=['张三','李四','王五']
columns=['数学','语文','英语']
df=pd.DataFrame(data=data,index=index,columns=columns)
print(df)
print('----------------------')
df.loc['陈六']=[56,67,90]
print(df)

# 新建一个DataFrame
new_df=pd.DataFrame(
  data={'数学':[67,69],'语文':[56,78],'英语':[1,99]},
  index=['张丽丽','王一一']
)
#print(new_df)
# df=df.append(new_df) # append()在pandas2.0 废弃了，使用concat()，用法：df=pd.concat([df,new_df],axis=0)
dff =pd.concat([df,new_df],axis=0)
print(dff)
#%%
#修改列标题
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
data=[[45,65,100],[56,45,50],[67,67,67]]
index=['张三','李四','王五']
columns=['数学','语文','英语']
df=pd.DataFrame(data=data,index=index,columns=columns)
print(df)

# (1)直接使用columns属性
df.columns=['数学（上）','语文（上）','英语（上）']
print(df)

# (2)rename  ,inplace参数的作用，是是否直接修改DataFrame
df.rename(columns={'数学（上）':'数学（下）','语文（上）':'语文（下）','英语（上）':'英语（下）'},inplace=True)
print(df)
#%%
# 修改行标题
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
data=[[45,65,100],[56,45,50],[67,67,67]]
index=['张三','李四','王五']
columns=['数学','语文','英语']
df=pd.DataFrame(data=data,index=index,columns=columns)
print(df)


#(1)直接赋值
df.index=list('123')

print(df)

# (2)rename()
df.rename({'1':'一一','2':'二二','3':'三三'},inplace=True,axis=0)
print(df)
#%%
#修改数据
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
data=[[45,65,100],[56,45,50],[67,67,67]]
index=['张三','李四','王五']
columns=['数学','语文','英语']
df=pd.DataFrame(data=data,index=index,columns=columns)
print(df)

#修改一整行
df.loc['张三']=[100,100,120]
print(df)

df.iloc[0,:]=[90,90,90] # 修改第0行的所有列
print(df)

# 修改整列数据
print('-------------------------')
df.loc[:,'数学']=[100,100,100]
print(df)
df.iloc[:,0]=90
print(df)


#修改某一处的数据
df.loc['李四','语文']=100
print(df)

df.iloc[1,1]=80
print(df)
#%%
# 删除数据

import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
data=[[45,65,100],[56,45,50],[67,67,67]]
index=['张三','李四','王五']
columns=['数学','语文','英语']
df=pd.DataFrame(data=data,index=index,columns=columns)
print(df)
print('------------------')
# 删除数学列
#df.drop(['数学'],axis=1,inplace=True)

#df.drop(columns='数学',inplace=True)

#df.drop(labels='数学',axis=1,inplace=True)

# 删除行
#df.drop(['张三'],axis=0,inplace=True)

#df.drop(index='张三',inplace=True)

#df.drop(labels='张三',axis=0,inplace=True)



#带条件的删除，删除数学成绩小于60
df.drop(df[df['数学']<60].index[1],inplace=True)  # 数学成绩中小于60的，有张三和李四，删除行索引1的李四
#print(df[df['数学']<60].index[1])
print(df)
#%%
