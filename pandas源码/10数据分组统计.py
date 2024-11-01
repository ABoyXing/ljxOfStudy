#%%
# 按照一列分组统计
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
df=pd.read_excel(r'pandas源码\电脑配件销售记录.xlsx')
#print(df)
print('-------------------------')
df1=df[['产品名称','数量','标准单价']]
# print(df1)

print(df1.groupby('产品名称',as_index=False).sum()) # 对数量，标准单价都进行求和统计

#%%6
# 按照多列分组统计
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
df=pd.read_excel(r'pandas源码\电脑配件销售记录.xlsx')
#print(df)
df1=df[['产品名称','销售员','数量']]
df1=df1.groupby(['产品名称','销售员']).sum() # 对数量进行求和
print(df1)

#%%
# 分组并按指定列进行计算
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
df=pd.read_excel(r'pandas源码\电脑配件销售记录.xlsx')
#print(df)
df1=df[['产品名称','数量','标准单价']]
print(df1.groupby('产品名称')['数量'].sum()) # 对数量进行求和
#%%
# 分组数据迭代
# 分组并按指定列进行计算
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
df=pd.read_excel(r'pandas源码\电脑配件销售记录.xlsx')

df1=df[['产品名称','数量','标准单价']] #提取数据
print(df1.groupby('产品名称')) #分组之后的数据类型为DataFrameGroupBy
for name,group in df1.groupby('产品名称'):
    print(name)
    print(group)
    print('-------------------------------')
#%%
# 多列分组，数据迭代
# 按照多列分组统计
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
df=pd.read_excel(r'pandas源码\电脑配件销售记录.xlsx')
print(df)
df1=df[['产品名称','销售员','数量']]
#df1=df1.groupby(['产品名称','销售员'])
# print(df1) # DataFrameGroupBy
for (k1,k2),group in df1.groupby(['产品名称','销售员']):
         print(k1,k2)
         print(group)    
         print('-------------------------------')                       
#%%
import pandas as pd
df=pd.read_excel(r'pandas源码\电脑配件销售记录.xlsx')
#print(df.head())
df1=df[['产品名称','数量']]
#print(df1)
print(df1.groupby('产品名称').agg(['sum','mean']))
#%%
#对不同的列采用不同的聚合函数
import pandas as pd
df=pd.read_excel(r'pandas源码\电脑配件销售记录.xlsx')
print(df.head())
df1=df[['产品名称','数量','成交金额']]
df1.groupby('产品名称').agg({'数量':['sum','mean'],'成交金额':['max','min']})
#%%
# 能过自定义的函数实现分组统计
import pandas as pd
df=pd.read_excel(r'pandas源码\电脑配件销售记录.xlsx')
#print(df.head())

#回顾知识点
# print(type(df['产品名称'])) #Series
print(df['产品名称'].value_counts())
maxcount=lambda x:x.value_counts().index[0] #行索引为0的
maxcount.__name__='销量最多的产品' 
df1=df.agg({'产品名称':[maxcount],'数量':['sum']})
print(df1)
#%%
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
df=pd.read_excel('JD手机销售数据.xlsx')
#print(df.head())
df=df.set_index('商品名称') # 设置商品名称为行索引
#print(df)
dict1={'北京出库销量':'华北地区',
       '上海出库销量':'华东地区',
       '广州出库销量':'华南地区',
       '天津出库销量':'华北地区',
       '苏州出库销量':'华东地区',
       '沈阳出库销量':'东北地区',
       '杭州出库销量':'华东地区'    
    
}
df1=df.groupby(dict1,axis=1).sum()
print(df1)


#%%
# 根据Series对象进行分组统计
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
df=pd.read_excel('JD手机销售数据.xlsx')
#print(df.head())
df=df.set_index('商品名称') # 设置商品名称为行索引
#print(df)
dict1={'北京出库销量':'华北地区',
       '上海出库销量':'华东地区',
       '广州出库销量':'华南地区',
       '天津出库销量':'华北地区',
       '苏州出库销量':'华东地区',
       '沈阳出库销量':'东北地区',
       '杭州出库销量':'华东地区'    
    
}
s=pd.Series(dict1) # 构建Series对象
#print(s)

df1=df.groupby(s,axis=1).sum() #分组，按行统计求和
print(df1)
#%%
