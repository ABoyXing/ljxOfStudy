#%%
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
data=[[45,65,100],[56,45,50],[67,67,67]]
index=['张三','李四','王五']
columns=['数学','语文','英语']
df=pd.DataFrame(data=data,index=index,columns=columns)
print(df)
print('--------------------------')
# 提取行数据
print(df.loc['张三'])  # 行索引名称
print('--------------------------')
print(df.iloc[0])  # 行索引的编号

print('------提取多行数据------（谁和谁）---')  #张三和王五

print(df.loc[['张三','王五']])

print(df.iloc[[0,2]])

print('--------提取连续的多行数据（从谁到谁）-----------------') # 从张三到王五
print(df.loc['张三':'王五'])   # 行索引名称， 包含王五
print('----------------------------------------')
print(df.iloc[0:2]) # 行索引序号，含0 不含2

print('---------------------------------')
print(df.iloc[1::]) # iloc[start:stop:step]

print('---------------------------------')
print(df.iloc[::2]) # iloc[start:stop:step]  步长为2  从0，1，2   取出0,2


#%%
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
data=[[45,65,100],[56,45,50],[67,67,67]]
index=['张三','李四','王五']
columns=['数学','语文','英语']
df=pd.DataFrame(data=data,index=index,columns=columns)
print(df)
print('--------------------------')
print(df[['数学','英语']]) # 直接使用列名提取

print('------------------------------')
print(df.loc[:,['数学','英语']])  # 逗号的左侧表示的是行，右侧表示的是列  ，所有行的，数学和英语
print('------------------------------')
print(df.iloc[:,[0,2]])

print('--------------提取连续的列-------------------')
print(df.loc[:,'语文':])
print('------------------------------')
print(df.iloc[:,1:])
#%%
# 提取区域数据
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
data=[[45,65,100],[56,45,50],[67,67,67]]
index=['张三','李四','王五']
columns=['数学','语文','英语']
df=pd.DataFrame(data=data,index=index,columns=columns)
print(df)
print(df.loc['张三','数学'],type(df.loc['张三','数学']))
print('------------------------------')
print(df.loc[['张三','王五'],['数学','语文']]) # df.loc[行索引，列索引]
#%%
print('-----------------------------------')
# :为连续，df.iloc[行索引，列索引]
# []为不连续，df.iloc[[行索引，行索引],[列索引，列索引]]
print(df.iloc[0,0]) # 第0 行，第0列
print(df.iloc[0:2,0:2]) # ,的左侧行切片，右侧列切片  ，提取的区域数据为连续的数据

print('------------------------------------')
print(df.iloc[[0,2],[0,2]]) # 第0行和第2行，第0列和第2列
print('----------------------------------') # 提取所有行的第0列
print(df.iloc[:,0])
#%%
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
data=[[45,65,100],[56,45,50],[67,67,67]]
index=['张三','李四','王五']
columns=['数学','语文','英语']
df=pd.DataFrame(data=data,index=index,columns=columns)
print(df)
print(df.loc[df['语文']>=60]) # 提取语文成绩大于等于60的学生信息
# 从个条件之间使用关系运算符

print(df.loc[(df['语文']>=60)  &(df['数学']>=60)   ])

#%%
