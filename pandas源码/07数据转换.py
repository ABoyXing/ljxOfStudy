#%%
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
pd.set_option('display.width',1000)
pd.set_option('display.max_columns',500)
df=pd.read_excel(r'pandas源码\快递发货单.xlsx',usecols=['客户名称','快递地址'])
print(df.head())
#%%
print(type(df['快递地址']))
#%%
new_df=df['快递地址'].str.split(' ',expand=True) # expand=True表示结果转成DataFrame
#%%
print(new_df)
#%%
print(df)
'''
这段代码将new_df中索引为0、1、2的元素分别赋值给df中的'省'、'市'、'区'这三列。
假设new_df是一个Series或列表且至少有三个元素。
如果df中这些列不存在，则会被创建。
'''
df['省']=new_df[0]
df['市']=new_df[1]
df['区']=new_df[2]
#%%
print(df.head())
#%%

import pandas as pd
data={
    
    'a':[1,2,3,4,5],
    'b':[(1,2),(2,3),(3,4),(5,6),(7,8)]
}
df=pd.DataFrame(data=data)
print(df)
#df[['b1','b2']]=df['b'].apply(pd.Series)
#print(df)
#%%
# join()与apply()
'''
这段代码的功能如下：
df['b'].apply(pd.Series)：将df中b列的每个元素转化为一个Series。
df.join(...)：将转化后的结果按列合并回原始DataFrame df。
注意：此操作假设df['b']列的元素是可以展开的结构（如list或dict）。
如果b列的每个元素是一个字典，那么这个操作会将其键值对展开为新的列；
如果是列表，则每个列表元素会成为新列的一行值。
'''
df=df.join(df['b'].apply(pd.Series))
print(df)
#%%
#行列转换，将列索引转成行
import pandas as pd
df=pd.read_excel(r'pandas源码\grade.xlsx')
print(df.head())
#%%
df=df.set_index(['班级','序号'])
print(df.head())
#%%
df=df.stack()
print(df.head(6))
#%%
#行列转换
import pandas as pd
df=pd.read_excel('grade2.xls',sheet_name='英语2')
#print(df.head(6))
df=df.set_index(['班级','序号','Unnamed: 2'])
print(df.unstack())
#%%
import pandas as pd 
df=pd.read_excel('grade3.xlsx')
#print(df.head())
print(df.pivot(index='序号',columns='班级',values='得分'))
#%%
# 将DataFrame转换成字典
import pandas as pd
df=pd.read_excel('电脑配件销售记录.xlsx')
#print(df.head())
df1=df.groupby('产品名称')['数量'].sum() #根据产品名称分组，统计数量

mydict=df1.to_dict() # 将DataFrame转成了字典
for item in mydict:
    print(item,':',mydict[item])
#%%
# 将DataFrame数据转成列表
import pandas as pd
df=pd.read_excel('电脑配件销售记录.xlsx')
#print(df.head())
df1=df[['产品名称']]
lst=df1['产品名称'].values.tolist()
#lst=df1['产品名称'].tolist()
print(lst)
print(type(lst))
#%%
# 将DataFrame转成元组
import pandas as pd
df=pd.read_excel('电脑配件销售记录.xlsx')
#print(df.head())
df1=df[['产品名称','销售员','数量']]
#print(df1)
t=[tuple (x) for x in df1.values]
for item in t:
    print(item)
#print(df1.values)
#%%
import pandas as pd
df=pd.read_excel('电脑配件销售记录.xlsx')
print(df.head())
df.to_html('电脑配件销售记录.html',header=True,index=False)
#%%
