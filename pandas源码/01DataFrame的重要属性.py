'''
#DataFrame对象是pandas中的一种数据结构，类似于二维表。
# pd.DataFrame(data,index,column,dtype)

'''


#%%
# 列表方式创建DataFrame对象
import pandas as pd
data=[['小太阳',320.9,100],['鼠标',150.3,50],['小刀',1.5,200]]
columns=['名称','单价','数量']
df=pd.DataFrame(data=data,columns=columns)
print('1',df)
print('查看所有元素的值\n',df.values)
print('查看所有元素的类型\n',df.dtypes)
print('查看所有行名称\n',list(df.index))
print('\n')
df.index=[1,2,3]
print(df)
print('查看列索引\n',df.columns)
df.columns=['商品名称','最新单价','实时数量']
print(df)
#%%
# 行列数据的转换
pd.set_option('display.unicode.east_asian_width',True) # 规整 格式
new_df=df.T
print(new_df)

print('查看前N条数据\n',df.head(1))
print('查看后N条数据\n',df.tail(1))
#%%
# 查看行和列shaple[0]表示行，shape[1]表示列
print(df)
print('行',df.shape[0],'列',df.shape[1])
#%%
print('查看索引、数据类型、内存信息\n',df.info)
#%%
