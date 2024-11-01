#%%
# 相同的列进行合并
import pandas as pd 
df1=pd.read_excel('student1.xlsx')
df2=pd.read_excel('student2.xlsx')
#df1  #测试数据读取
# 数据合并
new_df=pd.merge(df1,df2,on='编号')
new_df

#%%
# 通过索引列进行合并数据
import pandas as pd 
df1=pd.read_excel('student1.xlsx')
df2=pd.read_excel('student2.xlsx')

new_df=pd.merge(df1,df2,left_index=True,right_index=True)
new_df
#%%
# 数据合并之后，去掉重复数据
# 通过索引列进行合并数据
import pandas as pd 
df1=pd.read_excel('student1.xlsx')
df2=pd.read_excel('student2.xlsx')

new_df=pd.merge(df1,df2,left_index=True,right_index=True,on='编号')
new_df
#%%
# 数据合并之后，去掉重复数据
# 通过索引列进行合并数据
import pandas as pd 
df1=pd.read_excel('student1.xlsx')
df2=pd.read_excel('student2.xlsx')

new_df=pd.merge(df1,df2,how='right',on='编号')
new_df
#%%
#多对一合并
import pandas as pd
df1=pd.DataFrame({
    '编号':['msb1001','msb1002','msb1003'],
    '姓名':['张三','李四','王五']
})
df2=pd.DataFrame(
{
    '编号':['msb1001','msb1001','msb1003'],
    '语文':[145,134,146],
    '数学':[149,132,150],
    '英语':[123,134,143],
    '月份':['1月','2月','1月']
})
# 多对一的数据合并
new_df=pd.merge(df1,df2,on='编号')
new_df
#%%
# 多对多的数据合并
import pandas as pd
df1=pd.DataFrame(
{
    '编号':['msb1001','msb1002','msb1003','msb1003','msb1003'],
    '语文':[145,134,143,145,147]
})
df2=pd.DataFrame(
{
    '编号':['msb1001','msb1002','msb1003','msb1001','msb1001'],
    '体育':[34.5,28.4,39.6,34.6,45.5]
})
new_df=pd.merge(df1,df2)
new_df
#%%
# concat方法，数据合并(表结构相同，首尾相连)
import pandas as pd
df1=pd.read_excel('数据合并concat.xlsx',sheet_name='Sheet1')
df2=pd.read_excel('数据合并concat.xlsx',sheet_name='Sheet2')
df3=pd.read_excel('数据合并concat.xlsx',sheet_name='Sheet3')

# 合并
df=pd.concat([df1,df2,df3],keys=['表1','表2','表3'])
df
#%%
# concat横向表连接方式
import pandas as pd
df1=pd.read_excel('数据合并concat.xlsx',sheet_name='Sheet1')
df2=pd.read_excel('数据合并concat.xlsx',sheet_name='Sheet4')
#合并
df=pd.concat([df1,df2],axis=1)
df
#%%
# concat交叉连接
import pandas as pd
df1=pd.read_excel('数据合并concat.xlsx',sheet_name='Sheet1')
df2=pd.read_excel('数据合并concat.xlsx',sheet_name='Sheet4')
#合并
df=pd.concat([df1,df2],axis=1,join='inner')
df
#%%
