'''
# pd.read_excel
# pd.read_csv

'''


#%%
# 导入外部数据
# 导入Excel文件
import pandas as pd 
df=pd.read_excel(r'C:\Users\厉佳星\PycharmProjects\pythonProject2\pandas源码\京东鞋子评论信息.xlsx',sheet_name='码数分析',header=None)
print(df)
#%%
# 导入一列数据
import pandas as pd
df=pd.read_excel(r'pandas源码\02微机原理学员成绩统计.xlsx',sheet_name='02微机原理及格学员名单',usecols=[1])
print(df)
#%%
# 导入多列数据
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
df=pd.read_excel(r'pandas源码\02微机原理学员成绩统计.xlsx',sheet_name='02微机原理及格学员名单',usecols=['姓名','总成绩'])
print(df)
#%%
# 导入CSV文件
import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
df=pd.read_csv(r'pandas源码\京东鞋子评论数据.csv',sep=',',encoding='gbk')
print(df.head())

#%%
# 导入HTML
import pandas as pd
url='http://www.espn.com/nba/salaries'

pd.read_html(url,header=0)
print(df)

# # 保存成CSV文件
df.to_csv('nbasalary.csv',index=False)
#%%

