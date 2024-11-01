#%%
import pandas as pd
pd.set_option('display.unicode.east_asian.width',True)
# 设置 Pandas 显示选项
pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.max_rows', None)    # 显示所有行
pd.set_option('display.width', None)       # 自动调整宽度
pd.set_option('display.max_colwidth', None) # 显示完整的列内容

df=pd.read_excel(r'pandas源码\msb课程记录.xls')
print(df)
#%%
print('------------------------')
print(df.info()) # 查看是否有缺失值
#%%
print('------------------------------') #判断缺失值
print(df.isnull()) #结果为True或False，　　不为NaN时为False，　
print (df.notnull()) # 结果为True或False，不为NaN时，为True
#%%
#缺失值的处理方式 --删除
import pandas as pd
pd.set_option('display.unicode.east_asian.width',True)
df=pd.read_excel(r'pandas源码\msb课程记录.xls')
print(df)
print('----------------------------')
df=df.dropna() # 删除所有NaN行
print(df)
df2=df.reset_index()
print(df2)
#%%
import pandas as pd
pd.set_option('display.unicode.east_asian.width',True)
df=pd.read_excel(r'pandas源码\msb课程记录.xls')
print(df)
print('----------------------------')
df=df[df['课程总数量'].notnull()] # 提取课程数量中不为NaN 
print(df)
#%%
#缺失值的处理填充
import pandas as pd
pd.set_option('display.unicode.east_asian.width',True)
df=pd.read_excel('msb课程记录.xls')
print(df)
print('----------------------------')
df['课程总数量']=df['课程总数量'].fillna(0)
print(df)
#%%
#重复值的处理
import pandas as pd
pd.set_option('display.unicode.east_asian.width',True)
df=pd.read_excel(r'pandas源码\msb课程记录.xls')
print(df)
print('----------------------------')
# 判断是否具有重复值
print(df.duplicated())

# 去除全部的重复数据
# df=df.drop_duplicates()
# print(df)

# 去除指定列的重复数据 ，保留重复行中的最后一行
# df=df.drop_duplicates(['买家实际支付金额'],keep='last')
# print(df)

# 直接删除，保留一个副本
df1=df.drop_duplicates(['买家实际支付金额'],inplace=False)
print(df1)

print('---------------------------')
print(df)

#%%
