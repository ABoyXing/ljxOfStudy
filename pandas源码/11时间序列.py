#%%
# date_range()函数的使用
import pandas as pd
pd.date_range('2021-1-1',periods=10,freq='W') # 解释：从2021年1月1号开始，生成10个周的日期

#%%
# 将一分钟时间序列转换成3分钟
index=pd.date_range('2021-1-1',periods=9,freq='T') #解释：从2021年1月1号开始，生成9个时间点
print(index)
#%%
s=pd.Series(data=range(9),index=index)
print(s)
#%%
# 产生3分钟的序列
#s.resample(rule='3T',how='sum')
s.resample(rule='3T').sum() # 解释：将时间序列按照3分钟进行分组，并求和
#%%
import pandas as pd
# pd.set_option('display.max_colwidth', None) # 显示完整的列内容
df=pd.read_excel(r'pandas源码/msb课程销售记录.xlsx')
df=df.set_index('订单付款时间')
# df.head()
df1=df.resample('W').sum()
#%%
import pandas as pd
df=pd.read_excel(r'pandas源码/msb课程销售记录.xlsx')
df=df.set_index('订单付款时间')
#df.head()
df.resample('W',closed='left').sum()
#%%
import pandas as pd
index=pd.date_range('2020-1-1',periods=2)
s=pd.Series(range(1,3),index=index)

# 升采样
#s.resample('6H').asfreq()

# 使用前值填充
#s.resample('6H').ffill()

# 使用后值填充
s.resample('6H').bfill()
#%%
# 统计数据的open,close ,high,low的值
import pandas as pd
index=pd.date_range('2020-2-3',periods=12,freq='T')
s=pd.Series(range(12),index=index)
s
#%%
# 统计数据的open,close ,high,low的值
import pandas as pd
index=pd.date_range('2020-2-3',periods=12,freq='T')
s=pd.Series(range(12),index=index)
s.resample('5min').ohlc()
#%%
# 创建淘宝的每日销量数据
import pandas as pd
index=pd.date_range('2020-1-1',periods=15,freq='D')

#创建Series对象
s=pd.Series(data=[3,6,7,4,2,1,3,8,9,10,12,15,13,22,14],index=index)

# 使用rolling函数计算三天的均值
s.rolling(3).mean()
#%%
# 创建淘宝的每日销量数据
import pandas as pd
index=pd.date_range('2020-1-1',periods=15,freq='D')

#创建Series对象
s=pd.Series(data=[3,6,7,4,2,1,3,8,9,10,12,15,13,22,14],index=index)

# 使用rolling函数计算三天的均值
s.rolling(3,min_periods=1).mean()
#%%
